import corella

def suggest_workflow(occurrences=None,
                     events=None):
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
            galaxias.suggest_workflow(occurrences=df)
            
        .. program-output:: python -c "import pandas as pd;import galaxias;df = pd.DataFrame({'species': ['Callocephalon fimbriatum', 'Eolophus roseicapilla'], 'latitude': [-35.310, '-35.273'], 'longitude': [149.125, 149.133], 'eventDate': ['14-01-2023', '15-01-2023'], 'status': ['present', 'present']});print(galaxias.suggest_workflow(occurrences=df))"
    """
    corella.suggest_workflow(occurrences=occurrences,
                             events=events)