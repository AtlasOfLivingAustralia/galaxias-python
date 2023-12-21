import configparser,os
import pandas as pd

def readConfig():
    configFile=configparser.ConfigParser()
    inifile = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'config.ini')
    configFile.read(inifile)
    return configFile

def galaxias_config(atlas=None):
    """
    The galaxias package supports the creation of Darwin Core Archives for multiple atlases, including the ALA and GBIF. 
    The ``galah_config()`` function provides a way to let galaxias know which atlas you plan on submitting your data, so
    it can change its requirements for a valid Darwin Core Archive where necessary.

    Parameters
    ----------
        atlas : string
            Living Atlas to point to, ``Australia`` by default.
            
    Returns
    -------
        - No arguments: A ``pandas.DataFrame`` of all current configuration options.
        - >=1 arguments: None

    Examples
    --------

    .. prompt:: python

        import galaxias
        galaxias.galaxias_config(atlas="Australia")
    """

    # open the config parser
    configParser = configparser.ConfigParser()

    # read the config file
    inifile = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'config.ini')
    configParser.read(inifile)

    if atlas is None:

        # create dictionary for pandas dataframe 
        settings_dict = {"Configuration": [], "Value": []}
        for entry in configParser["galaxiasSettings"]:
            settings_dict["Configuration"].append(entry)
            settings_dict["Value"].append(configParser["galaxiasSettings"][entry])
        
        # return options
        return pd.DataFrame.from_dict(settings_dict)
    
    else:

        if atlas is not None:
            configParser["galaxiasSettings"]["atlas"] = atlas

        # write to file
        with open(inifile,"w") as fileObject:
            configParser.write(fileObject)