import webbrowser

def submit_archive(self):
    """
    Currently opens a Github issue on the ALA to place your data.

    Parameters
    ----------
        None

    Returns
    -------
        Raises a ``ValueError`` if something is wrong, or returns True if it passes.
    """

    temp = webbrowser.open('https://github.com/AtlasOfLivingAustralia/data-publication/issues/new?template=new-dataset.md', new=2)