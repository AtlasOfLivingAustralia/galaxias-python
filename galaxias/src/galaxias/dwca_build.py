import pandas as pd
import os
import zipfile
from .version import __version__
from .read_dwc_terms_links import read_dwc_terms_links
from .build_subelement import build_subelement
from .common_functions import add_file_to_dwca
import json
import xml.etree.ElementTree as ET
from operator import itemgetter
import subprocess
import time
import requests
import webbrowser
import corella
import delma

class dwca:

    def __init__(self,
                 working_dir = './',
                 publishing_dir = 'data-publish',
                 dwca_name = 'dwca.zip',
                 create_md = True,
                 xml_url = None,
                 occurrences = None,
                 occurrences_archive_filename = 'occurrences.txt',
                 multimedia = None,
                 multimedia_archive_filename = 'multimedia.txt',
                 events = None,
                 events_archive_filename = 'events.txt',
                 emof = None,
                 emof_archive_filename = 'extendedMeasurementOrFact.txt', # was .csv
                 metadata_md = 'metadata.md',
                 eml_xml = 'eml.xml',
                 meta_xml = 'meta.xml',
                 print_notices = True):

        # initialise variables
        current_dir = subprocess.check_output("pwd",shell=True,text=True).strip()
        if working_dir[0] != '.' or working_dir[0:2] != './':
            self.working_dir = '{}/{}'.format(current_dir,working_dir)
        else:
            self.working_dir = working_dir
        self.publishing_dir = publishing_dir
        self.dwca_name = '{}/{}/{}'.format(self.working_dir,publishing_dir,dwca_name)
        self.occurrences = occurrences
        self.occurrences_archive_filename = occurrences_archive_filename
        self.multimedia = multimedia
        self.multimedia_archive_filename = multimedia_archive_filename
        self.events = events
        self.events_archive_filename = events_archive_filename
        self.emof = emof
        self.emof_archive_filename = emof_archive_filename
        self.metadata_md = metadata_md
        self.eml_xml = eml_xml
        self.meta_xml = meta_xml

        # create directory for publishing
        if not os.path.isdir(publishing_dir):
            os.mkdir(publishing_dir)
        
        # now initialise the data variables
        vars = ['occurrences','multimedia','events','emof']

        # optionally create markdown
        if create_md:
            delma.create_md(metadata_md = metadata_md, working_dir = self.working_dir, 
                            xml_url = xml_url)

        # loop over all data variables
        for var in vars:

            # get value of variable
            var_value = getattr(self,var)

            # check for valid value of data variable
            if var_value is None or type(var_value) is pd.core.frame.DataFrame:
                # object, attribute, value
                setattr(self,var,var_value) 
                if var == 'occurrences' and var_value is None:
                    if print_notices:
                        print('WARNING: You will need occurrences for both Darwin Core and Event Core Archives.')
            elif type(var_value) is str:
                if any(x in var_value for x in ['txt','csv']):
                    setattr(self,var,pd.read_csv(var_value))
                else:
                    raise ValueError("If providing a filename, you must provide a csv-formatted file file")
            else:
                raise ValueError("Only a csv-formatted filename or Pandas dataframe will be accepted for {}.".format(var))

    def build_archive(self,
                      print_report=True):
        """
        Checks all your files for Darwin Core compliance, and then creates the 
        Darwin Core archive in your working directory.

        Parameters
        ----------
            None

        Returns
        -------
            Raises a ``ValueError`` if something is wrong, or returns ``None`` if it passes.
        """
        # run basic checks on data
        data_check = self.check_dataset(print_report=print_report)

        # run eml.xml check
        eml_xml_check = self.check_metadata()

        # run meta.xml check
        self.make_meta_xml()
        meta_xml_check = self.check_meta_xml()

        # set the boolean for xml_check
        if eml_xml_check is None and meta_xml_check:
            xml_check = True
        else:
            xml_check = False

        # write dwca if data and xml passes
        if data_check and xml_check:
            
            # open archive
            zf = zipfile.ZipFile(self.dwca_name,'w')

            # list for looping
            objects_list = [self.occurrences,self.events,self.multimedia,self.emof]
            filename_list = [self.occurrences_archive_filename,self.events_archive_filename,self.multimedia_archive_filename,self.emof_archive_filename]

            # looping over associated objects and filenames
            # for i,(dataframe,filename) in enumerate(zip(objects_list,filename_list)):
            for i,(dataframe,filename) in enumerate(zip(objects_list,filename_list)):
                if dataframe is not None:
                    add_file_to_dwca(zf=zf,
                                     dataframe=dataframe,
                                     publishing_dir=self.publishing_dir,
                                     file_to_write=filename)

            # write eml.xml
            zf.write("{}/{}".format(self.publishing_dir,self.eml_xml))
            
            # write meta.xml
            zf.write("{}/{}".format(self.publishing_dir,self.meta_xml))
            
            # close zipfile
            zf.close()
        
        else:
            raise ValueError("You need to check your data or metadata for errors.")
    
    def check_archive(self,
                      username = None,
                      email = None,
                      password = None):
        """
        Checks whether or not your Darwin Core Archive is formatted correctly.

        Parameters
        ----------
            None

        Returns
        -------
            Raises a ``ValueError`` if something is wrong, or returns True if it passes.
        """

        version_string = 'galaxias-python v{}'.format(__version__)

        # create URL
        validate_url = 'http://api.gbif.org/v1/validation'
        result_url = 'https://api.gbif.org/v1/validation/{key}'

        validation_request = {
            "sourceId": "string",
            "installationKey": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
            "notificationEmail": [email]
        }

        archive = self.dwca_name
        
        with open(archive, 'rb') as f:
            files = {
                # added .read() at the end
                'file': (archive, f.read(), 'application/zip')  # @RequestPart
            }

        validator_response = requests.post(validate_url, 
                                 files=files, 
                                 data={'validationRequest': json.dumps(validation_request)}, 
                                 auth=(username, password), 
                                 headers={})

        response_json = validator_response.json()
        key = response_json['key']
        result_response = requests.get(result_url.replace('{key}',key),
                                       auth=(username, password))
        result_response_json = result_response.json()

        if result_response_json['status'] == 'QUEUED':
            while result_response_json['status'] == 'QUEUED':
                time.sleep(5)
                result_response = requests.get(result_url.replace('{key}',key),
                                        auth=(username, password))
                result_response_json = result_response.json()

        if result_response_json['status'] == 'FAILED':
            print("Number of errors: {}\n".format(len(result_response_json['metrics']['files'])))
            for f in result_response_json['metrics']['files']:
                if 'fileName' in f:
                    print('{}: {}'.format('fileName',f['fileName']))
                    if len(f['issues'][0]['samples']) < 1:
                        print('{}: {}'.format('issues',f['issues'][0]['samples']))
                    else:
                        print('{}: {}'.format('issues',f['issues'][0]['samples'][0]['relatedData']))
                if 'rowType' in f:
                    print('{}: {}'.format('rowType',f['rowType']))
                    print('{}: {}'.format('issues',f['issues'][0]['samples'][0]['relatedData']))
                print()
        elif result_response_json['status'] == 'PASSED':
            print("Congratulations! Your archive passed validation.")
        else:
            print("status not in galaxias")
            print(result_response_json['status'])

    def check_dataset(self,
                      print_report=True):
        """
        Checks whether or not your data meets the predefined Darwin Core 
        standard.  Calls the ``corella`` package for this.

        Parameters
        ----------
            None

        Returns
        -------
            A printed report detailing presence or absence of required data.
        """
        result = corella.check_dataset(occurrences=self.occurrences,
                                       events=self.events,
                                       # multimedia=self.multimedia,
                                       # emof=self.emof,
                                       print_report=print_report)
        if result:
            return result
        
    def check_dwca(self):
        """
        Checks whether or not your Darwin Core Archive is formatted correctly.

        Parameters
        ----------
            None

        Returns
        -------
            Raises a ``ValueError`` if something is wrong, or returns True if it passes.
        """

        # get all variables
        vars_dict = vars(self)
        self_vars = list(vars(self).keys())
        data_vars = [x for x in self_vars if 'xml' not in x and 'name' not in x and 'md' not in x]
        
        # determine what type of archive it is
        data_files = list(itemgetter(*data_vars)(vars_dict))
        
        # check for empty archive
        if all(type(x) == type(data_files[0]) for x in data_files):
            raise ValueError("You have no data in your DwCA.  Please at least add occurrences")
        
        result = corella.check_data(occurrences=self.occurrences,
                                    events=self.events,
                                    # multimedia=self.multimedia,
                                    # emof=self.emof,
                                    print=False)
        if result:

            if os.path.exists("{}/{}".format(self.working_dir,self.meta_xml)) and os.path.exists("{}/{}".format(self.working_dir,self.eml_xml)):
                return True
            else:
                raise ValueError('You need to include the meta.xml and eml.xml file in your DwCA.')

        else:
            raise ValueError("Some of your data does not comply with the Darwin Core standard.  Please run corella.check_data() and/or corella.suggest_workflow().")
    
    def check_metadata(self):
        """
        Checks whether or not the metadata xml is formatted correctly.  Calls ``delma`` 
        for this.

        Parameters
        ----------
            None

        Returns
        -------
            A printed report detailing presence or absence of required data.
        """
        if os.path.exists("{}/{}".format(self.publishing_dir,self.eml_xml)):
            delma.check_metadata(eml_xml=self.eml_xml,eml_dir=self.publishing_dir)
        else:
            raise ValueError()
        
    def check_meta_xml(self):
        """
        Checks whether your schema (``meta.xml``) is formatted correctly.

        Parameters
        ----------
            None

        Returns
        -------
            A printed report detailing presence or absence of required data.
        """
        if os.path.exists("{}/{}".format(self.publishing_dir,self.meta_xml)):
            return True
        else:
            raise ValueError("Cannot find meta.xml file.")

    def display_metadata_as_dataframe(self):
        """
        Writes the ``eml.xml`` file from the metadata markdown file into your current working directory.  
        The ``eml.xml`` file is the metadata file containing things like authorship, licence, institution, 
        etc.

        Parameters
        ----------
            ``metadata_md``: ``str``
                Name of the markdown file that you want to convert to EML.  Default value is ``'metadata.md'``.
            ``working_dir``: ``str``
                Name of your working directory.  Default value is ``'./'``.
                    
        Returns
        -------
            ``pandas dataframe`` denoting all the information in the metadata file
        """
        return delma.display_as_dataframe(metadata_md = self.metadata_md,
                                          working_dir = self.working_dir)

    def make_meta_xml(self):
        """
        Makes the ``metadata.xml`` file from your ``eml.xml`` file and information from your ``occurrences`` 
        / other included extensions.  The ``metadata.xml`` file is your descriptor file, in that it describes 
        what is in the DwCA.

        Parameters
        ----------
            ``None``

        Returns
        -------
            ``None``
        """

        # check for at least occurrences
        if self.occurrences is None:
            raise ValueError("You need to have a passing, valid occurrence dataframe for this")
        
        # get list
        mylist = sorted(list(self.occurrences.columns),
                    key=lambda x: x == 'occurrenceID',
                    reverse=True)
        self.occurrences = self.occurrences[mylist]

        # get dwc terms
        dwc_terms_info = read_dwc_terms_links()

        # initialise metadata
        metadata = ET.Element("archive")
        metadata.set('xmlns', 'http://rs.tdwg.org/dwc/text/')
        metadata.set('metadata',self.eml_xml)

        # set the core of the archive and for
        core = ET.SubElement(metadata,"core")

        # check if it is an eventCore or an occurrenceCore
        if self.events is not None:
            core = build_subelement(element=core,
                                    row_type='http://rs.tdwg.org/dwc/terms/Occurrence',
                                    filename=self.occurrences_archive_filename,
                                    data=self.occurrences,
                                    dwc_terms_info=dwc_terms_info)
            ext = ET.SubElement(metadata,"extension")
            ext = build_subelement(element=ext,
                                    row_type='http://rs.tdwg.org/dwc/terms/Event',
                                    filename=self.events_archive_filename,
                                    data=self.events,
                                    dwc_terms_info=dwc_terms_info)
        else:
            core = build_subelement(element=core,
                                    row_type='http://rs.tdwg.org/dwc/terms/Occurrence',
                                    filename=self.occurrences_archive_filename,
                                    data=self.occurrences,
                                    dwc_terms_info=dwc_terms_info)

        # Extensions
        if self.multimedia is not None:
            ext = ET.SubElement(metadata,"extension")
            ext = build_subelement(element=ext,
                                    row_type='http://rs.tdwg.org/dwc/terms/Multimedia',
                                    filename=self.multimedia_archive_filename,
                                    data=self.multimedia,
                                    dwc_terms_info=dwc_terms_info)

        if self.emof is not None:
            ext = ET.SubElement(metadata,"extension")
            ext = build_subelement(element=ext,
                                    row_type='http://rs.tdwg.org/dwc/terms/MeasurementOrFact',
                                    filename=self.emof_archive_filename,
                                    data=self.emof,
                                    dwc_terms_info=dwc_terms_info)

        # write metadata
        tree = ET.ElementTree(metadata)
        ET.indent(tree, space="\t", level=0)
        tree.write("{}/{}".format(self.publishing_dir,self.meta_xml), xml_declaration=True)

    def set_abundance(self,
                      individualCount=None,
                      organismQuantity=None,
                      organismQuantityType=None):
        """
        Checks for location information, as well as uncertainty and coordinate reference system.  
        Also runs data checks on coordinate validity.

        Parameters
        ----------
            dataframe: ``pandas.DataFrame``
                The ``pandas.DataFrame`` that contains your data to check
            individualCount: ``str``
                A column name that contains your individual counts (should be whole numbers).
            organismQuantity: ``str``
                A column name that contains a number or enumeration value for the quantity of organisms.  
                Used together with ``organismQuantityType`` to provide context.
            organismQuantityType: ``str`` 
                A column name or phrase denoting the type of quantification system used for ``organismQuantity``.

        Returns
        -------
            ``pandas.DataFrame`` with the updated data.

        Examples
        ----------
            `set_abundance vignette <../../html/galaxias_user_guide/independent_observations/set_abundance.html>`_
        """
        self.occurrences = corella.set_abundance(dataframe=self.occurrences,individualCount=individualCount,
                                                 organismQuantity=organismQuantity,organismQuantityType=organismQuantityType)

    def set_collection(self,
                       datasetID=None,
                       datasetName=None,
                       catalogNumber=None):
        """
        Checks for location information, as well as uncertainty and coordinate reference system.  
        Also runs data checks on coordinate validity.

        Parameters
        ----------
            dataframe: ``pandas.DataFrame``
                The ``pandas.DataFrame`` that contains your data to check
            datasetID: ``str``
                A column name or other string denoting the identifier for the set of data. May be a global unique 
                identifier or an identifier specific to a collection or institution.
            datasetName: ``str``
                A column name or other string identifying the data set from which the record was derived.
            catalogNumber: ``str`` 
                A column name or other string denoting a unique identifier for the record within the data set or collection.

        Returns
        -------
            ``pandas.DataFrame`` with the updated data.

        Examples
        ----------
            `set_collection vignette <../../html/galaxias_user_guide/independent_observations/set_collection.html>`_
        """
        self.occurrences = corella.set_collection(dataframe=self.occurrences,datasetID=datasetID,
                                                    datasetName=datasetName,catalogNumber=catalogNumber)

    def set_coordinates(self,
                        decimalLatitude=None,
                        decimalLongitude=None,
                        geodeticDatum=None,
                        coordinateUncertaintyInMeters=None,
                        coordinatePrecision=None):
        """
        Checks for location information, as well as uncertainty and coordinate reference system.  
        Also runs data checks on coordinate validity.

        Parameters
        ----------
            dataframe: ``pandas.DataFrame``
                The ``pandas.DataFrame`` that contains your data to check
            decimalLatitude: ``str``
                A column name that contains your latitudes (units in degrees).
            decimalLongitude: ``str``
                A column name that contains your longitudes (units in degrees).
            geodeticDatum: ``str`` 
                A column name or a ``str`` with he datum or spatial reference system 
                that coordinates are recorded against (usually "WGS84" or "EPSG:4326"). 
                This is often known as the Coordinate Reference System (CRS). If your 
                coordinates are from a GPS system, your data are already using WGS84.
            coordinateUncertaintyInMeters: ``str``, ``float`` or ``int`` 
                A column name (``str``) or a ``float``/``int`` with the value of the 
                coordinate uncertainty. ``coordinateUncertaintyInMeters`` will typically 
                be around ``30`` (metres) if recorded with a GPS after 2000, or ``100`` 
                before that year.
            coordinatePrecision: ``str``, ``float`` or ``int``
                Either a column name (``str``) or a ``float``/``int`` with the value of the 
                coordinate precision. ``coordinatePrecision`` should be no less than 
                ``0.00001`` if data were collected using GPS.

        Returns
        -------
            ``pandas.DataFrame`` with the updated data.

        Examples
        ----------
            `set_coordinates vignette <../../html/galaxias_user_guide/independent_observations/set_coordinates.html>`_
        """
        self.occurrences = corella.set_coordinates(dataframe=self.occurrences,decimalLatitude=decimalLatitude,
                                                   decimalLongitude=decimalLongitude,geodeticDatum=geodeticDatum,
                                                   coordinateUncertaintyInMeters=coordinateUncertaintyInMeters,
                                                   coordinatePrecision=coordinatePrecision)

    def set_datetime(self,
                     check_events=False,
                     eventDate=None,
                     year=None,
                     month=None,
                     day=None,
                     eventTime=None,
                     string_to_datetime=False,
                     yearfirst=True,
                     dayfirst=False,
                     time_format='%H:%m:%S'):
        """
        Checks for time information, such as the date an occurrence occurred.  Also runs checks 
        on the validity of the format of the date.

        Parameters
        ----------
            check_events: ``logical``
                If ``True``, will check the events file.  If ``False``, will check occurrences file.  Default is ``False``.
            eventDate: ``str``
                A column name (``str``) denoting the column with the dates of the events, or a ``str`` or 
                ``datetime.datetime`` object denoting the date of the event.
            year: ``str`` or ``int``
                A column name (``str``) denoting the column with the dates of the events, or an ``int`` denoting
                the year of the event.
            month: ``str`` or ``int``
                A column name (``str``) denoting the column with the dates of the events, or an ``int`` denoting
                the month of the event.
            day: ``str`` or ``int``
                A column name (``str``) denoting the column with the dates of the events, or an ``int`` denoting
                the day of the event.
            eventTime: ``str``
                A column name (``str``) denoting the column with the dates of the events, or a ``str`` denoting
                the time of the event.
            string_to_datetime: ``logical``
                An argument that tells ``corella`` to convert dates that are in a string format to a ``datetime`` 
                format.  Default is ``False``.
            yearfirst: ``logical``
                An argument to specify whether or not the day is first when converting your string to datetime.  
                Default is ``True``.
            dayfirst: ``logical``
                An argument to specify whether or not the day is first when converting your string to datetime.  
                Default is ``False``.
            time_format: ``str``
                A ``str`` denoting the original format of the dates that are being converted from a ``str`` to a 
                ``datetime`` object.  Default is ``'%H:%m:%S'``.

        Returns
        -------
            None - the occurrences dataframe is updated
        
        Examples
        ----------
            `set_datetime vignette <../../html/galaxias_user_guide/independent_observations/set_datetime.html>`_
        """
        if check_events:
            self.events = corella.set_datetime(dataframe=self.events,eventDate=eventDate,year=year,month=month,
                                               day=day,eventTime=eventTime,string_to_datetime=string_to_datetime,
                                               yearfirst=yearfirst,dayfirst=dayfirst,time_format=time_format)
        else:
            self.occurrences = corella.set_datetime(dataframe=self.occurrences,eventDate=eventDate,year=year,month=month,
                                                day=day,eventTime=eventTime,string_to_datetime=string_to_datetime,
                                                yearfirst=yearfirst,dayfirst=dayfirst,time_format=time_format)

    def set_events(self,
                   eventID=None,
                   parentEventID=None,
                   eventType=None,
                   Event=None,
                   samplingProtocol=None,
                   event_hierarchy=None,
                   sep='-'):
        """
        Identify or format columns that contain information about an Event. An "Event" in Darwin Core Standard refers to an action that occurs at a place and time. Examples include:

        - A specimen collecting event
        - A survey or sampling event
        - A camera trap image capture
        - A marine trawl
        - A camera trap deployment event
        - A camera trap burst image event (with many images for one observation)

        Parameters
        ----------
            dataframe: ``pandas.DataFrame``
                The ``pandas.DataFrame`` that contains your data to check
            eventID: ``str``, ``logical``
                A column name (``str``) that contains a unique identifier for your event.  Can also be set 
                to ``True`` to generate values.  Parameters for these values can be specified with the arguments 
                ``sequential_id``, ``add_sequential_id``, ``composite_id``, ``sep`` and ``random_id``
            sep: ``char``
                Separation character for composite IDs.  Default is ``-``.
            parentEventID: ``str``
                A column name (``str``) that contains a unique ID belonging to an event below 
                it in the event hierarchy.
            eventType: ``str`` 
                A column name (``str``) or a ``str`` denoting what type of event you have.
            Event: ``str`` 
                A column name (``str``) or a ``str`` denoting the name of the event.
            samplingProtocol: ``str`` or 
                Either a column name (``str``) or a ``str`` denoting how you collected the data, 
                i.e. "Human Observation".
            event_hierarchy: ``dict``
                A dictionary containing a hierarchy of all events so they can be linked.  For example, 
                if you have a set of observations that were taken at a particular site, you can use the 
                dict {1: "Site Visit", 2: "Sample", 3: "Observation"}.

        Returns
        -------
            None - the occurrences dataframe is updated

        Examples
        ----------
            `set_events vignette <../../html/galaxias_user_guide/longitudinal_studies/set_events.html>`_
        """
        self.events = corella.set_events(dataframe=self.events,eventID=eventID,parentEventID=parentEventID,
                                         eventType=eventType,Event=Event,samplingProtocol=samplingProtocol,
                                         event_hierarchy=event_hierarchy)

    def set_individual_traits(self,
                              individualID=None,
                              lifeStage=None,
                              sex=None,
                              vitality=None,
                              reproductiveCondition=None):
        
        """
        Checks for location information, as well as uncertainty and coordinate reference system.  
        Also runs data checks on coordinate validity.

        Parameters
        ----------
            dataframe: ``pandas.DataFrame``
                The ``pandas.DataFrame`` that contains your data to check
            individualID: ``str``
                A column name containing an identifier for an individual or named group of 
                individual organisms represented in the Occurrence. Meant to accommodate 
                resampling of the same individual or group for monitoring purposes. May be 
                a global unique identifier or an identifier specific to a data set.
            lifeStage: ``str``
                A column name containing the age, class or life stage of an organism at the time of occurrence.
            sex: ``str`` 
                A column name or value denoting the sex of the biological individual.
            vitality: ``str``
                A column name or value denoting whether an organism was alive or dead at the time of collection or observation.
            reproductiveCondition: ``str``
                A column name or value denoting the reproductive condition of the biological individual.
            
        Returns
        -------
            ``pandas.DataFrame`` with the updated data.

        Examples
        ----------
            `set_individual_traits vignette <../../html/galaxias_user_guide/independent_observations/set_individual_traits.html>`_
        """
        self.occurrences = corella.set_individual_traits(dataframe=self.occurrences,individualID=individualID,
                                                         lifeStage=lifeStage,sex=sex,vitality=vitality,
                                                         reproductiveCondition=reproductiveCondition)

    def set_license(self,
                    license=None,
                    rightsHolder=None,
                    accessRights=None):
        """
        Checks for location information, as well as uncertainty and coordinate reference system.  
        Also runs data checks on coordinate validity.

        Parameters
        ----------
            dataframe: ``pandas.DataFrame``
                The ``pandas.DataFrame`` that contains your data to check
            license: ``str``
                A column name or value denoting a legal document giving official 
                permission to do something with the resource. Must be provided as a 
                url to a valid license.
            rightsHolder: ``str``
                A column name or value denoting the person or organisation owning or 
                managing rights to resource.
            accessRights: ``str``
                A column name or value denoting any access or restrictions based on 
                privacy or security.

        Returns
        -------
            ``pandas.DataFrame`` with the updated data.

        Examples
        ----------
            `set_license vignette <../../html/galaxias_user_guide/independent_observations/set_license.html>`_
        """
        self.occurrences = corella.set_license(dataframe=self.occurrences,license=license,rightsHolder=rightsHolder,
                                               accessRights=accessRights)

    def set_locality(self,
                     check_events = False,
                     continent = None,
                     country = None,
                     countryCode = None,
                     stateProvince = None,
                     locality = None):
        """
        Checks for additional location information, such as country and countryCode.

        Parameters
        ----------
            check_events: ``logical``
                Check to see if user wants to edit ``events`` dataframe.  Default is ``False``.
            continent: ``str``
                Either a column name (``str``) or a string denoting one of the seven continents.
            country: ``str`` or ``pandas.Series``
                Either a column name (``str``) or a string denoting the country.
            countryCode: ``str`` or ``pandas.Series``
                Either a column name (``str``) or a string denoting the countryCode.
            stateProvince: ``str`` or ``pandas.Series``
                Either a column name (``str``) or a string denoting the state or province.
            locality: ``str`` or ``pandas.Series``
                Either a column name (``str``) or a string denoting the locality.
        Returns
        -------
            None - the occurrences dataframe is updated

        Examples
        ----------
            `set_locality vignette <../../html/galaxias_user_guide/independent_observations/set_locality.html>`_
        """
        
        if check_events:
            self.events = corella.set_locality(dataframe=self.events,continent=continent,
                                               country=country,countryCode=countryCode,
                                               stateProvince=stateProvince,locality=locality)
        else:
            self.occurrences = corella.set_locality(dataframe=self.occurrences,continent=continent,
                                                    country=country,countryCode=countryCode,
                                                    stateProvince=stateProvince,locality=locality)

    def set_observer(self,
                     recordedBy=None,
                     recordedByID=None):
        """
        Checks for the name of the taxon you identified is present.

        Parameters
        ----------
            dataframe: ``pandas.DataFrame``
                The ``pandas.DataFrame`` that contains your data to check
            recordedBy: ``str``
                A column name or name(s) of people, groups, or organizations responsible 
                for recording the original occurrence. The primary collector or observer should be 
                listed first.
            recordedByID: ``str``
                A column name or the globally unique identifier for the person, people, groups, or organizations 
                responsible for recording the original occurrence.

        Returns
        -------
            ``pandas.DataFrame`` with the updated data.

        Examples
        ----------
            `set_observer vignette <../../html/galaxias_user_guide/independent_observations/set_observer.html>`_
        """
        self.occurrences = corella.set_observer(dataframe=self.occurrences,recordedBy=recordedBy,recordedByID=recordedByID)

    def set_occurrences(self,
                        occurrenceID=None,
                        catalogNumber=None,
                        recordNumber=None,
                        basisOfRecord=None,
                        occurrenceStatus=None,
                        sep='-',
                        add_eventID=False,
                        eventType=None):
        """
        Checks for unique identifiers of each occurrence and how the occurrence was recorded.

        Parameters
        ----------
            occurrenceID: ``str`` or ``bool``
                Either a column name (``str``) or ``True`` (``bool``).  If a column name is 
                provided, the column will be renamed.  If ``True`` is provided, unique identifiers
                will be generated in the dataset.
            catalogNumber: ``str`` or ``bool``
                Either a column name (``str``) or ``True`` (``bool``).  If a column name is 
                provided, the column will be renamed.  If ``True`` is provided, unique identifiers
                will be generated in the dataset.
            recordNumber: ``str`` or ``bool``
                Either a column name (``str``) or ``True`` (``bool``).  If a column name is 
                provided, the column will be renamed.  If ``True`` is provided, unique identifiers
                will be generated in the dataset.
            sep: ``char``
                Separation character for composite IDs.  Default is ``-``.
            basisOfRecord: ``str``
                Either a column name (``str``) or a valid value for ``basisOfRecord`` to add to 
                the dataset.
            occurrenceStatus: ``str``
                Either a column name (``str``) or a valid value for ``occurrenceStatus`` to add to 
                the dataset.
            add_eventID: ``logic``
                Either a column name (``str``) or a valid value for ``occurrenceStatus`` to add to 
                the dataset.
            eventType: ``str``
                Either a column name (``str``) or a valid value for ``eventType`` to add to 
                the dataset.

        Returns
        -------
            ``pandas.DataFrame`` with the updated data.

        Examples
        ----------
            `set_occurrences vignette <../../html/galaxias_user_guide/independent_observations/set_occurrences.html>`_
        """
        self.occurrences = corella.set_occurrences(dataframe=self.occurrences,occurrenceID=occurrenceID,sep=sep,
                                                   catalogNumber=catalogNumber,recordNumber=recordNumber,
                                                   basisOfRecord=basisOfRecord,occurrenceStatus=occurrenceStatus,
                                                   add_eventID=add_eventID,events=self.events,eventType=eventType)

    def set_scientific_name(self,
                            scientificName=None,
                            taxonRank=None,
                            scientificNameAuthorship=None):
        """
        Checks for the name of the taxon you identified is present.

        Parameters
        ----------
            scientificName: ``str``
                A column name (``str``) denoting all your scientific names.
            taxonRank: ``str``
                A column name (``str``) denoting the rank of your scientific names (species, genus etc.)
            scientificNameAuthorship: ``str``
                A column name (``str``) denoting who originated the scientific name.

        Returns
        -------
            ``pandas.DataFrame`` with the updated data.

        Examples
        ----------
            `set_scientific_name vignette <../../html/galaxias_user_guide/independent_observations/set_scientific_name.html>`_
        """
        self.occurrences = corella.set_scientific_name(dataframe=self.occurrences,scientificName=scientificName,
                                                      taxonRank=taxonRank,scientificNameAuthorship=scientificNameAuthorship)

    def set_taxonomy(self,
                     kingdom=None,
                     phylum=None,
                     taxon_class=None, 
                     order=None,
                     family=None,
                     genus=None,
                     specificEpithet=None,
                     vernacularName=None):
        """
        Adds extra taxonomic information.  Also runs checks on whether or not the names are the 
        correct data type.

        Parameters
        ----------
            dataframe: ``pandas.DataFrame``
                The ``pandas.DataFrame`` that contains your data to check
            kingdom: ``str``,``list``
                A column name, kingdom name (``str``) or list of kingdom names (``list``).
            phylum: ``str``,``list``
                A column name, phylum name (``str``) or list of phylum names (``list``).
            taxon_class: ``str``,``list``
                A column name, class name (``str``) or list of class names (``list``).
            order: ``str``,``list``
                A column name, order name (``str``) or list of order names (``list``).
            family: ``str``,``list``
                A column name, family name (``str``) or list of family names (``list``).
            genus: ``str``,``list``
                A column name, genus name (``str``) or list of genus names (``list``).
            specificEpithet: ``str``,``list``
                A column name, specificEpithet name (``str``) or list of specificEpithet names (``list``).
                **Note**: If ``scientificName`` is *Abies concolor*, the ``specificEpithet`` is *concolor*.
            vernacularName: ``str``,``list``
                A column name, vernacularName name (``str``) or list of vernacularName names (``list``).

        Returns
        -------
            ``pandas.DataFrame`` with the updated data.

        Examples
        ----------
            `set_taxonomy vignette <../../html/galaxias_user_guide/independent_observations/set_taxonomy.html>`_
        """
        self.occurrences = corella.set_taxonomy(dataframe=self.occurrences,kingdom=kingdom,phylum=phylum,taxon_class=taxon_class,
                                                order=order,family=family,genus=genus,specificEpithet=specificEpithet,
                                                vernacularName=vernacularName)

    def submit_archive(self):
        """
        Checks whether or not your Darwin Core Archive is formatted correctly.

        Parameters
        ----------
            None

        Returns
        -------
            Raises a ``ValueError`` if something is wrong, or returns True if it passes.
        """

        temp = webbrowser.open('https://github.com/AtlasOfLivingAustralia/data-publication/issues/new?template=new-dataset.md', new=2)

    def suggest_workflow(self):
        """
        Suggests a workflow to ensure your data conforms with the pre-defined Darwin Core standard.

        Parameters
        ----------
            None

        Returns
        -------
            A printed report detailing presence or absence of required data.

        Examples
        --------
            Suggest a workflow for a small dataset

            .. prompt:: python

                import pandas as pd
                import galaxias
                df = pd.DataFrame({'species': ['Callocephalon fimbriatum', 'Eolophus roseicapilla'], 'latitude': [-35.310, '-35.273'], 'longitude': [149.125, 149.133], 'eventDate': ['14-01-2023', '15-01-2023'], 'status': ['present', 'present']})
                my_dwca = galaxias.dwca(occurrences=df)
                my_dwca.suggest_workflow()
                
            .. program-output:: python -c "import pandas as pd;import galaxias;df = pd.DataFrame({'species': ['Callocephalon fimbriatum', 'Eolophus roseicapilla'], 'latitude': [-35.310, '-35.273'], 'longitude': [149.125, 149.133], 'eventDate': ['14-01-2023', '15-01-2023'], 'status': ['present', 'present']});my_dwca = galaxias.dwca(occurrences=df);print(my_dwca.suggest_workflow())"
        """
            
        corella.suggest_workflow(occurrences=self.occurrences,
                                 events=self.events)

    def write_eml(self):
        """
        Writes the ``eml.xml`` file from the metadata markdown file into your publishing directory.  
        The ``eml.xml`` file is the metadata file containing things like authorship, licence, institution, 
        etc.

        Parameters
        ----------
            None
                    
        Returns
        -------
            ``pandas.DataFrame`` with the updated data.

        Examples
        ----------
            `write_eml vignette <../../html/galaxias_user_guide/independent_observations/write_eml_xml.html>`_
        """
        delma.write_eml(eml_xml = self.eml_xml, working_dir = self.working_dir, publishing_dir = self.publishing_dir)
