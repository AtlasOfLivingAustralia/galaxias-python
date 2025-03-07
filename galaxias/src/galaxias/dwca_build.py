import pandas as pd
import os
import zipfile
import shutil
from .read_dwc_terms_links import read_dwc_terms_links
from .build_subelement import build_subelement
from .common_functions import add_file_to_dwca,write_to_zip_and_disk
# from dwca.read import DwCAReader
import xml.etree.ElementTree as ET
from operator import itemgetter
import subprocess
import corella
import delma

class dwca:

    def __init__(self,
                 working_dir = 'dwca_data',
                 data_raw_dir = 'data_raw',
                 data_proc_dir = 'data_processed',
                 dwca_name = 'dwca.zip',
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
                 meta_xml = 'meta.xml'
                 ):

        # initialise variables
        current_dir = subprocess.check_output("pwd",shell=True,text=True).strip()
        self.working_dir = '{}/{}'.format(current_dir,working_dir)
        self.data_raw_dir = '{}/{}/{}'.format(current_dir,working_dir,data_raw_dir)
        self.data_proc_dir = '{}/{}/{}'.format(current_dir,working_dir,data_proc_dir)
        self.dwca_name = '{}/{}/{}'.format(current_dir,working_dir,dwca_name)
        self.occurrences = occurrences
        self.occurrences_archive_filename = occurrences_archive_filename
        self.multimedia = multimedia
        self.multimedia_archive_filename = multimedia_archive_filename
        self.events = events
        self.events_archive_filename = events_archive_filename
        self.emof = emof
        self.metadata_md = '{}/{}/{}'.format(current_dir,working_dir,metadata_md)
        self.emof_archive_filename = emof_archive_filename
        self.eml_xml = eml_xml
        self.meta_xml = meta_xml

        # make the working directory
        folders =  ['working_dir','data_raw_dir','data_proc_dir']
        for folder in folders:
            folder_name = getattr(self,folder)
            if not os.path.isdir(folder_name):
                os.mkdir(folder_name)
        
        # now initialise the data variables
        vars = ['occurrences','multimedia','events','emof']

        # create markdown
        delma.create_md(working_dir = working_dir)

        # loop over all data variables
        for var in vars:

            # get value of variable
            var_value = getattr(self,var)

            # check for valid value of data variable
            if var_value is None or type(var_value) is pd.core.frame.DataFrame:
                # object, attribute, value
                setattr(self,var,var_value) 
                if var == 'occurrences' and var_value is None:
                    print('WARNING: You will need occurrences for both Darwin Core and Event Core Archives.')
            elif type(var_value) is str:
                if any(x in var_value for x in ['txt','csv']):
                    shutil.copy2(var_value,self.data_raw_dir)
                    setattr(self,var,pd.read_csv(var_value))
                else:
                    raise ValueError("If providing a filename, you must provide a csv file")
            else:
                raise ValueError("Only a csv filename or Pandas dataframe will be accepted for {}.".format(var))

    def check_dataset(self):
        """
        Checks whether or not your data (only occurrences for now) meets the predefined Darwin Core 
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
                                       print_report=True)
        if result:
            return result
        print("Your data does not comply with the Darwin Core standard.  Please run galaxias.suggest_workflow().")

    def check_dwca(self):
        """
        Checks whether or not your Darwin Core Archive meets the pre-defined standard.

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
    
    def check_eml_xml(self):
        """
        Checks whether or not your data (only occurrences for now) meets the predefined Darwin Core 
        standard.  Calls the ``corella`` package for this.

        Parameters
        ----------
            None

        Returns
        -------
            A printed report detailing presence or absence of required data.
        """
        if os.path.exists("{}/{}".format(self.working_dir,self.eml_xml)):
            delma.check_eml_xml(eml_xml=self.eml_xml,working_dir=self.working_dir)
        else:
            raise ValueError()
        
    def check_meta_xml(self):
        """
        Checks whether or not your data (only occurrences for now) meets the predefined Darwin Core 
        standard.  Calls the ``corella`` package for this.

        Parameters
        ----------
            None

        Returns
        -------
            A printed report detailing presence or absence of required data.
        """
        if os.path.exists("{}/{}".format(self.working_dir,self.meta_xml)):
            return True
        else:
            raise ValueError()

    def create_dwca(self):
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
        data_check = self.check_dwca()

        # run eml.xml check
        eml_xml_check = self.check_eml_xml()

        # run meta.xml check
        meta_xml_check = self.check_meta_xml()

        # set the boolean for xml_check
        if xml_check is None:
            xml_check = True

        # write dwca if data and xml passes
        if data_check and eml_xml_check and meta_xml_check:
            
            # open archive
            zf = zipfile.ZipFile(self.dwca_name,'w')

            # list for looping
            objects_list = [self.occurrences,self.events,self.multimedia,self.emof]
            filename_list = [self.occurrences_archive_filename,self.events_archive_filename,self.multimedia_archive_filename,self.emof_archive_filename]

            # looping over associated objects and filenames
            for dataframe,filename in enumerate(zip(objects_list,filename_list)):
                print("testing...")
                print(dataframe)
                print(filename)
                import sys
                sys.exit()
                if dataframe is not None:
                    add_file_to_dwca(zf=zf,
                                    dataframe=dataframe,
                                    file_to_write='{}/{}'.format(self.data_proc_dir,filename),
                                    removefile=filename)

            # write eml.xml
            write_to_zip_and_disk(zf=zf,
                                      copyfile="{}/{} .".format(self.working_dir,self.eml_xml),
                                      removefile=self.eml_xml)  
              
            # write meta.xml
            write_to_zip_and_disk(zf=zf,
                        copyfile="{}/{} .".format(self.working_dir,self.meta_xml),
                        removefile=self.meta_xml)
            
            # close zipfile
            zf.close()
    
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
        tree.write("{}/{}".format(self.working_dir,self.meta_xml), xml_declaration=True)

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
        
    def use_abundance(self,
                      individualCount=None,
                      organismQuantity=None,
                      organismQuantityType=None):
        """
        Checks for location information, as well as uncertainty and coordinate reference system.  
        Also runs data checks on coordinate validity.

        Parameters
        ----------
            individualCount: ``str``
                A column name (``str``) that contains your individual counts (should be whole numbers).
            organismQuantity: ``str`` or 
                A column name (``str``) that contains a description of your individual counts.
            organismQuantityType: ``str`` 
                A column name (``str``) that describes what your organismQuantity is.

        Returns
        -------
            None - the occurrences dataframe is updated
        """
        self.occurrences = corella.use_abundance(dataframe=self.occurrences,individualCount=individualCount,
                                                 organismQuantity=organismQuantity,organismQuantityType=organismQuantityType)

    def use_coordinates(self,
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
            decimalLatitude: ``str``
                A column name (``str``) that contains your latitudes (units in degrees).
            decimalLongitude: ``str`` or ``pandas.Series``
                A column name (``str``) that contains your longitudes (units in degrees).
            geodeticDatum: ``str`` 
                A column name (``str``) or a ``str`` with the name of a valid Coordinate 
                Reference System (CRS).
            coordinateUncertaintyInMeters: ``str``, ``float`` or ``int`` 
                A column name (``str``) or a ``str`` with the name of a valid Coordinate 
                Reference System (CRS).
            coordinatePrecision: ``str`` or ``pandas.Series``
                Either a column name (``str``) or a column from the ``occurrences`` argument 
                (``pandas.Series``) that represents the inherent uncertainty of your measurement 
                (unit in degrees).

        Returns
        -------
            None - the occurrences dataframe is updated
        """
        self.occurrences = corella.use_coordinates(dataframe=self.occurrences,decimalLatitude=decimalLatitude,
                                                   decimalLongitude=decimalLongitude,geodeticDatum=geodeticDatum,
                                                   coordinateUncertaintyInMeters=coordinateUncertaintyInMeters,
                                                   coordinatePrecision=coordinatePrecision)

    def use_datetime(self,
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
        """
        if check_events:
            self.events = corella.use_datetime(dataframe=self.occurrences,eventDate=eventDate,year=year,month=month,
                                               day=day,eventTime=eventTime,string_to_datetime=string_to_datetime,
                                               yearfirst=yearfirst,dayfirst=dayfirst,time_format=time_format)
        else:
            self.occurrences = corella.use_datetime(dataframe=self.occurrences,eventDate=eventDate,year=year,month=month,
                                                day=day,eventTime=eventTime,string_to_datetime=string_to_datetime,
                                                yearfirst=yearfirst,dayfirst=dayfirst,time_format=time_format)

    def use_events(self,
                   eventID=None,
                   parentEventID=None,
                   eventType=None,
                   Event=None,
                   samplingProtocol=None,
                   event_hierarchy=None):
        """
        Checks for event-specific information, such as how the data was collected, what type of 
        event it was, and names of events.

        Parameters
        ----------
            eventID: ``str``
                A column name (``str``) that contains a unique ID for your event.
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
        """
        self.events = corella.use_events(dataframe=self.events,eventID=eventID,parentEventID=parentEventID,
                                         eventType=eventType,Event=Event,samplingProtocol=samplingProtocol,
                                         event_hierarchy=event_hierarchy)

    def use_locality(self,
                     continent = None,
                     country = None,
                     countryCode = None,
                     stateProvince = None,
                     locality = None):
        """
        Checks for additional location information, such as country and countryCode.

        Parameters
        ----------
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
        """
        
        self.occurrences = corella.use_locality(dataframe=self.occurrences,continent=continent,
                                                country=country,countryCode=countryCode,
                                                stateProvince=stateProvince,locality=locality)

    def use_occurrences(self,
                        occurrenceID=None,
                        catalogNumber=None,
                        recordNumber=None,
                        basisOfRecord=None,
                        occurrenceStatus=None,
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
            None - the occurrences dataframe is updated
        """
        
        if self.events is None:
            self.occurrences = corella.use_occurrences(dataframe=self.occurrences,occurrenceID=occurrenceID,
                                                       catalogNumber=catalogNumber,recordNumber=recordNumber,
                                                       basisOfRecord=basisOfRecord,occurrenceStatus=occurrenceStatus)
        else:
            self.occurrences = corella.use_occurrences(dataframe=self.occurrences,occurrenceID=occurrenceID,
                                                       catalogNumber=catalogNumber,recordNumber=recordNumber,
                                                       basisOfRecord=basisOfRecord,occurrenceStatus=occurrenceStatus,
                                                       add_eventID=add_eventID,events=self.events,eventType=eventType)

    def use_scientific_name(self,
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
            None - the occurrences dataframe is updated
        """
        self.occurrences = corella.use_scientific_name(dataframe=self.occurrences,scientificName=scientificName,
                                                      taxonRank=taxonRank,scientificNameAuthorship=scientificNameAuthorship)

    def validate_dwca(self):
        """
        """
        print("Amanda write this function")
        n=1

    def write_eml_xml(self):
        """
        """
        delma.write_eml_xml(eml_xml = self.eml_xml, working_dir = self.working_dir)