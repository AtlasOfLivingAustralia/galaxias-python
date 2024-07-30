import xmlschema
import requests
import pandas as pd
import datetime
import numpy as np
from pandas.api.types import is_string_dtype
from pandas.api.types import is_numeric_dtype
from .get_dwc_noncompliant_terms import get_dwc_noncompliant_terms
from .common_dictionaries import *
from .common_functions import *

def check_all_data(dataframe=None):
    """
    Checks occurrenceIDs, basisOfRecord, scientificName, location information and eventDate.

    Parameters
    ----------
        ``dataframe``: ``pandas`` dataframe
            the dataframe containing occurrences data

    Returns
    -------
        ``errors``: ``dict``
            any errors that were caught separated by category
    """

    # check that dataframe is not None
    if dataframe is None:
        raise ValueError("You need to provide a dataframe")
    
    # get number of columns to check
    num_columns = len(list(dataframe.columns))

    # initialise errors dict
    errors = {
        "Column": list(dataframe.columns),
        "pass": [u'\u2713' for j in range(num_columns)],
        "errors": ['-' for j in range(num_columns)]
    }

    # loop over all data errors
    for nc in range(num_columns):
        try:
            if errors["Column"][nc] in ['occurrenceID', 'catalogNumber','recordNumber']:
                check_occurrenceIDs(dataframe=dataframe)
            elif errors["Column"][nc] == 'basisOfRecord':
                check_basisOfRecord(dataframe=dataframe)
            elif errors["Column"][nc] == 'scientificName':
                check_scientificName(dataframe=dataframe)
            elif errors["Column"][nc] in ['decimalLatitude', 'decimalLongitude', 'geodeticDatum', 'coordinateUncertaintyInMeters','coordinatePrecision']:
                check_coordinates(dataframe=dataframe)
            elif errors["Column"][nc] in ['eventDate', 'day', 'month', 'year', 'time']:
                check_eventDate(dataframe=dataframe)
            else:
                print("Column {} isn't taken into account".format(errors["Column"][nc]))
        except ValueError as e:
            errors["pass"][nc] = u'\u2717'
            if errors["errors"][nc] == '-':
                errors["errors"][nc] = 1
            else:
                errors["errors"][nc] += 1

    # return the errors
    return errors

def check_basisOfRecord(dataframe=None):
    """
    Checks whether or not your basisOfRecord values are valid.

    Parameters
    ----------
        None

    Returns
    -------
        Raises a ``ValueError`` if something is not valid.
    """

    # check if dataframe is provided an argument
    if dataframe is None:
        raise ValueError("You need to provide a dataframe")
    
    # check basisOfRecord values
    if 'basisOfRecord' in dataframe.columns:
        bor_column = list(dataframe["basisOfRecord"])
        types_bor = list(set(list(type(x) for x in bor_column)))
        if len(types_bor) > 1:
            raise ValueError("There are multiple types in the basisOfRecord column - ensure that there are only strings")
        else:
            if types_bor[0] is not str:
                raise ValueError("basisOfRecord column should only contain strings")
            else:
                temp = pd.read_table('https://raw.githubusercontent.com/gbif/parsers/dev/src/main/resources/dictionaries/parse/basisOfRecord.tsv').dropna()
                terms = list(set(temp['PRESERVED_SPECIMEN']))
                terms = snake_to_camel_case(terms)
                if not set(terms).issuperset(set(dataframe['basisOfRecord'])):
                    raise ValueError("there invalid basisOfRecord values.  Valid values are {}".format(', '.join(terms)))
    else:
        raise ValueError("The basisOfRecord column title wasn't set correctly.")

def check_coordinates(dataframe=None):
    """
    Checks whether or not your occurrences data complies with 
    Darwin Core standards.

    Parameters
    ----------
        None

    Returns
    -------
        Raises a ``ValueError`` if something is not valid.
    """

    # check data types for location data
    for c in GEO_REQUIRED_DWCA_TERMS["Australia"]:
        if c in dataframe.columns:
            data_type = dataframe[c].dtypes
            
            if c in ['decimalLatitude','decimalLongitude','coordinatePrecision'] and not is_numeric_dtype(dataframe[c]):
                raise ValueError("Column {} needs to be of type float.  Currently, it is {}.".format(c,data_type))
            else:
                pass

            if c == 'coordinateUncertaintyInMeters' and not is_numeric_dtype(dataframe[c]):
                raise ValueError("Column {} needs to be of type float or type int.  Currently, it is {}.".format(c,data_type))
            else:
                pass

            if c == 'geodeticDatum' and not is_string_dtype(dataframe[c]):
                raise ValueError("Column {} needs to be of type str.  Currently, it is {}.".format(c,data_type))
            else:
                pass
        # elif c in ['geodeticDatum','coordinateUncertaintyInMeters','coordinatePrecision']:
        #     print('We noticed that you have not provided a {}.  We will then assume the default is {}.'.format(c,defaults[c]))
                
    # check range of lat/long are correct
    lat_valid_count = dataframe['decimalLatitude'].astype(float).between(-90, 90, inclusive='both').sum()
    lon_valid_count = dataframe['decimalLongitude'].astype(float).between(-180, 180, inclusive='both').sum()

    if lat_valid_count < len(dataframe['decimalLatitude']):
        raise ValueError("There are some invalid latitude values.  They should be between -90 and 90.")

    if lon_valid_count < len(dataframe['decimalLongitude']):
        raise ValueError("There are some invalid longitude values.  They should be between -180 and 180.")

def check_dwca_values(dataframe=None):
    """
    Checks whether or not certain Darwin Core data columns contain correct values 
    (i.e. the values for ``basisOfRecord`` comply with pre-defined values defined 
    by the Darwin Core standard).

    Parameters
    ----------
        None

    Returns
    -------
        Raises a ``ValueError`` if something is wrong, or returns True if it passes.

    Examples
    --------
    Amanda to add here later.
    """
    controlled_vocabs_url = "https://github.com/gbif/parsers/tree/dev/src/main/resources/dictionaries/parse"
    response = requests.get(controlled_vocabs_url)
    import sys
    sys.exit()
    return True

   
def check_emof(self):
    """
    Checks whether or not your extended measurement or fact file complies with 
    Darwin Core standards.

    Parameters
    ----------
        None

    Returns
    -------
        Raises a ``ValueError`` if something is wrong, or returns True if it passes.

    Examples
    --------
    Amanda to add here later.
    """
    
    vocab_check = get_dwc_noncompliant_terms(dataframe = self.emof)
    if len(vocab_check) > 0:
        raise ValueError("Your column names do not comply with the DwC standard: {}".format(vocab_check))
    
    return True

def check_eventDate(dataframe=None):
    """
    Checks whether or not your event dates complies with 
    Darwin Core standards.

    Parameters
    ----------
        None

    Returns
    -------
        Raises a ``ValueError`` if something is not valid.
    """

    if 'eventDate' in dataframe.columns:

        eventDate_column = list(dataframe["eventDate"])
        types_edc = list(set(list(type(x) for x in eventDate_column)))
        if len(types_edc) > 1:
            raise ValueError("There are multiple types in the eventDate column - ensure that there are only datetime objects")
        else:
            if not isinstance(types_edc[0], datetime.datetime):
                if types_edc[0] is str:
                    raise ValueError("Data is not in datetime format.  If you want to convert from string to datetime object, set string_to_datetime to True.")
    else:
        raise ValueError("You need eventDate in your dataframe to use this function.")
    
    # check for other variables
    for var in ['year','month','day','time']:
        if var in dataframe.columns:
            dtypes = dataframe[var].dtypes
            if type(dtypes) is np.dtypes.ObjectDType:
                print("figure something out")
            elif var != 'time' and type(dtypes) is not int:
                raise ValueError("{} is not the correct type.  It should be int".format(var))
            elif var == 'time' and type(dtypes) is not isinstance(dtypes,datetime.date):
                raise ValueError("Time should be converted to a datetime object.")
            else:
                raise ValueError("check the dtypes: {}".format(dtypes))

def check_events(self):
    """
    Checks whether or not certain Darwin Core data columns contain correct values 
    (i.e. the values for ``basisOfRecord`` comply with pre-defined values defined 
    by the Darwin Core standard).

    Parameters
    ----------
        None

    Returns
    -------
        Raises a ``ValueError`` if something is wrong, or returns True if it passes.

    Examples
    --------
    Amanda to add here later.
    """

    required_columns = False

    # check for required columns
    if any(map(lambda v: v in required_columns_event, list(self.events.columns))):

        # check to see if we are missing any columns
        check_missing_fields = set(list(self.events.columns)).issuperset(required_columns_event)
        
        # check for any missing required fields
        if (not check_missing_fields) or (type(check_missing_fields) is not bool and len(check_missing_fields) > 0):
            print("You are missing {}".format(list(set(required_columns_event).difference(set(self.events.columns)))))
            return required_columns
        else:
            required_columns = True
    else:
        return required_columns
    
    # check for 
    event_ids_ok = self.check_unique_event_ids()
    
    if event_ids_ok and required_columns:
        return True
    elif not event_ids_ok:
        list_event_ids = list(self.events['eventID'])
        duplicates = [x for x in list_event_ids if list_event_ids.count(x) >= 2]
        print("There are some duplicate eventIDs: {}".format(duplicates))
        return False
    else:
        return False

def check_locality(dataframe=None):
    """
    Checks whether or not your locality data complies with 
    Darwin Core standards.

    Parameters
    ----------
        None

    Returns
    -------
        Raises a ``ValueError`` if something is wrong, or returns True if it passes.
    """

    continents = ["Africa","Antarctica","Asia","Europe","North America","Oceania","South America"]
    
    for var in ['continent','country','countryCode','stateProvince','locality']:
        if var in dataframe.columns:
            loc_column = list(dataframe[var])
            types_loc = list(set(list(type(x) for x in loc_column)))
            if len(types_loc) > 1:
                raise ValueError("There are multiple types in the eventDate column - ensure that there are only datetime objects")
            else:
                if not isinstance(types_loc[0], str):
                    raise ValueError("Data needs to be in string format.")
                else:
                    if var == 'continent':
                        if not set(continents).issuperset(set(dataframe[var])):
                            raise ValueError("Some of your continent values are incorrect.")

def check_multimedia(self):
    """
    Checks whether or not your multimedia file complies with 
    Darwin Core standards.

    Parameters
    ----------
        None

    Returns
    -------
        Raises a ``ValueError`` if something is wrong, or returns True if it passes.
    """
    
    vocab_check = get_dwc_noncompliant_terms(dataframe = self.multimedia)
    if len(vocab_check) > 0:
        raise ValueError("Your column names do not comply with the DwC standard: {}".format(vocab_check))
            
    return True

def check_occurrenceIDs(dataframe=None):
    """
    Checks whether or not you have unique ids for your occurrences.

    Parameters
    ----------
        None

    Returns
    -------
        Raises a ``ValueError`` if something is not valid.
    """
    list_terms = list(dataframe.columns)
    unique_id_columns = ['occurrenceID','catalogNumber','recordNumber']
    for id in unique_id_columns:
        if id in list_terms:
            if len(list(set(dataframe[id]))) < len(list(dataframe[id])):
                raise ValueError("There are duplicate {}s".format(id))   

def check_occurrences(dataframe=None):
        """
        Checks whether or not your occurrences data complies with 
        Darwin Core standards.

        Parameters
        ----------
            None

        Returns
        -------
            Raises a ``ValueError`` if something is not valid.
        """

        # run basic checks
        vocab_check = get_dwc_noncompliant_terms(dataframe = dataframe)
        if len(vocab_check) > 0:
            raise ValueError("Your column names do not comply with the DwC standard.")
        
        # TODO: check all values in vocab are there
        values_check = check_dwca_values(dataframe=dataframe)
        if type(values_check) is not bool:
            raise ValueError("The values in some of your columns do not comply with the DwC standard.")
        
        # check for presence of occurrenceID
        if 'occurrenceID' not in list(dataframe):
            raise ValueError("You need to add unique identifiers into your occurrences.")
        
        # check for unique ids
        unique_id_check = check_occurrenceIDs(dataframe=dataframe)
        if not unique_id_check:
            list_event_ids = list(dataframe['occurrenceID'])
            duplicates = [x for x in list_event_ids if list_event_ids.count(x) >= 2]
            raise ValueError("There are some duplicate eventIDs: {}".format(duplicates))
        
        return True

def check_scientificName(dataframe=None):
    """
    Checks whether or not your scientific names are in string format.

    Parameters
    ----------
        None

    Returns
    -------
        Raises a ``ValueError`` if something is not valid.
    """

    if dataframe is None:
        raise ValueError("You need to provide a dataframe")

    for item in ['scientificName','scientificNameRank','scientificNameAuthorship']:
        if item in dataframe.columns:
            sn_column = list(dataframe[item])
            types_data = list(set(list(type(x) for x in sn_column)))
            if len(types_data) > 1:
                raise ValueError("There are multiple types in the {} column - ensure that there are only strings".format(item))
            else:
                if types_data[0] is not str:
                    raise ValueError("{} column should only contain strings".format(item))
        elif item == 'scientificName': 
            raise ValueError("The scientificName column title wasn't set correctly.")

def check_unique_event_ids(dataframe=None):
    """
    Checks whether or not your occurrences data complies with 
    Darwin Core standards.

    Parameters
    ----------
        None

    Returns
    -------
        Raises a ``ValueError`` if something is not valid.
    """

    if len(list(set(dataframe['eventID']))) < len(list(dataframe['eventID'])):
        return False
    else:
        return True
        
def check_xmls(dwca=None):
    """
    Checks whether or not your ``eml.xml`` file is formatted correctly for GBIF.

    Parameters
    ----------
        None

    Returns
    -------
        Raises a ``ValueError`` if something is wrong, or returns True if it passes.

    Examples
    --------
    Amanda to add here later.
    """

    try:
        check = xmlschema.validate("{}/{}".format(dwca.working_dir,dwca.eml_xml), 'http://rs.gbif.org/schema/eml-gbif-profile/1.1/eml-gbif-profile.xsd')
        return check
    except xmlschema.validators.exceptions.XMLSchemaChildrenValidationError as e:
        print("children error")
        print("There is an error with your eml.xml file:\n")
        if "value doesn't match any pattern of" in e.reason:
            value = str(e.elem).split(" ")[1]
            print("Please provide a value to {}".format(value))
            print()
        else:
            print(e.reason)
        breakpoint
    except xmlschema.validators.exceptions.XMLSchemaValidationError as e:
        print("schema validation")
        print("There is an error with your eml.xml file:\n")
        if "value doesn't match any pattern of" in e.reason:
            value = str(e.elem).split(" ")[1]
            print("Please provide a value to {}".format(value))
            print()
        elif "character data between child elements not allowed" in e.reason:
            value = str(e.elem).split(" ")[1]
            print("Please remove the value you've provided for {}".format(value))
            print()
        else:
            print(str(e.elem).split(" ")[1])
            print(e.reason)
        breakpoint