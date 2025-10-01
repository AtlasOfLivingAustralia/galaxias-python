import requests
import json
import time
import zipfile
from .version import __version__

def check_archive(archive='dwca.zip',
                  publishing_dir='./data-publish',
                  username = None,
                  email = None,
                  password = None):
    """
    Checks whether or not your Darwin Core Archive is formatted correctly.

    Parameters
    ----------
        ``archive``: ``str`` 
            Name of your Darwin Core Archive.  Default is ``dwca.zip``.
        ``publishing_dir``: ``str``
            Name of the directory where all your finalised data lives.  Default value is ``'./data-publish/'``.
        ``GBIF``: ``logical`` 
            Flag to check if you are using the GBIF Validation tool.  Default is ``False``.
        ``username``: ``str`` 
            GBIF username.  Default is ``None``.
        ``email``: ``str``
            GBIF registered email.  Default is ``None``.
        ``password``: ``str``
            GBIF password.  Default is ``None``.

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
    
    with open(archive, 'rb') as f:
        files = {
            # added .read() at the end
            'file': ('{}/{}'.format(publishing_dir,archive), f.read(), 'application/zip')  # @RequestPart
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