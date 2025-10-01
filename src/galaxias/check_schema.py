import os

def check_schema(schema='meta.xml',
                 publishing_dir='./data-publish/'):
    """
    Checks whether your schema (``meta.xml``) is formatted correctly.

    Parameters
    ----------
        schema: ``str``
            File name of your schema file (default is ``meta.xml``)
        publishing_dir: ``str``
            Folder where all your finalised data will be published

    Returns
    -------
        A printed report detailing presence or absence of required data.
    """
    if os.path.exists("{}/{}".format(publishing_dir,schema)):
        return True
    else:
        raise ValueError("Cannot find schema file.")