import corella
import pandas as pd

def check_dataset(occurrences=None,
                  events=None,
                  occurrences_filename='occurrences.csv',
                  events_filename='events.csv',
                  publishing_dir='./data-publish',
                  # multimedia=None,
                  # emof=None,
                  print_report=True):
        """
        Checks whether or not your data meets the predefined Darwin Core 
        standard.  Calls the ``corella`` package for this.

        Parameters
        ----------
            ``occurrences``: ``pandas DataFrame`` 
                This is the dataframe holding your occurrence data.  Default is ``None``.
            ``events``: ``pandas DataFrame`` 
                This is the dataframe holding your occurrence data.  Default is ``None``.
            ``publishing_dir``: ``str``
                Name of the directory where all your processed data lives.  Default value is ``'./data-publish/'``.
            ``print_report``: ``str``
                Print your data report to screen.  Default value is ``'True'``.

        Returns
        -------
            A printed report detailing presence or absence of required data.
        """
        # then, check dataset
        result = corella.check_dataset(occurrences=occurrences,
                                       events=events,
                                       # multimedia=multimedia,
                                       # emof=emof,
                                       occurrences_filename=occurrences_filename,
                                       events_filename=events_filename,
                                       publishing_dir=publishing_dir,
                                       print_report=print_report)
        if result:
            return result
        
def check_variable_type(var=None,
                        publishing_dir='./data-publish/'):
    
    if isinstance(var, pd.DataFrame):
        return var
    elif isinstance(var, str):
        return pd.read_csv('{}/{}',format(publishing_dir,var))
    else:
        raise ValueError('Variable {} needs to be a file name or a pandas Dataframe with your data.'.format(var))