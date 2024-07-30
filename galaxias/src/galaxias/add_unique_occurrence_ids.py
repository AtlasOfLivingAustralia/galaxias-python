import uuid

def add_unique_occurrence_IDs(column_name="occurrenceID",
                              dataframe=None):
        """
        Function that automatically adds unique IDs (in the form of uuids) to each of your occurrences.

        Parameters
        ----------
            ``column_name`` : ``str``
                String containing name of column you want to add.  Default is ``occurrenceID``

        Returns
        -------
            ``None``

        Examples
        --------

        .. prompt:: python

            import galaxias
            import pandas as pd
            data = pd.read_csv("occurrences_dwc.csv")
            my_dwca = galaxias.dwca(occurrences=data)
            my_dwca.add_unique_occurrence_IDs()
            my_dwca.occurrences

        .. program-output:: python -c "import galaxias;import pandas as pd;pd.set_option('display.max_columns', None);pd.set_option('display.expand_frame_repr', False);pd.set_option('max_colwidth', None);data = pd.read_csv(\\\"galaxias_user_guide/occurrences_dwc.csv\\\");my_dwca = galaxias.dwca(occurrences=data);my_dwca.add_unique_occurrence_IDs();print(my_dwca.occurrences)"
        """

        if dataframe is None:
            raise ValueError("Please provide a data frame.")
        
        if column_name == "occurrenceID" or column_name == "catalogNumber" or column_name == "recordNumber":
            uuids = [None for i in range(dataframe.shape[0])]
            for i in range(dataframe.shape[0]):
                uuids[i] = str(uuid.uuid4())
            dataframe.insert(0,column_name,uuids)
            return dataframe
        else:
            raise ValueError("Please provide a string with a valid DwCA value for your column name.")