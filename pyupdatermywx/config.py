"""
wxupdatedemo/config.py
"""
# We're using UPPERCASE for class attributes but lowerCamelCase
# for instance attributes.  Pylint doesn't distinguish between them:
# pylint: disable=invalid-name

import os
import sys

import pyupdatermywx

if 'WXUPDATEDEMO_TESTING' in os.environ:
    class ClientConfig(object):
        """Config for PyUpdater client"""
        # pylint: disable=too-few-public-methods
        APP_NAME = 'PyUpdaterMyWx'
        COMPANY_NAME = 'Company Name'
        MAX_DOWNLOAD_RETRIES = 3
        PUBLIC_KEY = None
        UPDATE_URLS = []
else:
    try:
        from client_config import ClientConfig  # pylint: disable=import-error
    except ImportError:
        sys.stderr.write("client_config.py is missing.\n"
                         "You need to run: pyupdater init\n"
                         "See: http://www.pyupdater.org/usage-cli/\n")
        sys.exit(1)

CLIENT_CONFIG = ClientConfig()
if 'WXUPDATEDEMO_TESTING_APP_NAME' in os.environ:
    CLIENT_CONFIG.APP_NAME = os.environ['WXUPDATEDEMO_TESTING_APP_NAME']
if 'WXUPDATEDEMO_TESTING_COMPANY_NAME' in os.environ:
    CLIENT_CONFIG.COMPANY_NAME = os.environ['WXUPDATEDEMO_TESTING_COMPANY_NAME']
if 'WXUPDATEDEMO_TESTING_APP_VERSION' in os.environ:
    pyupdatermywx.__version__ = os.environ['WXUPDATEDEMO_TESTING_APP_VERSION']
if 'WXUPDATEDEMO_TESTING_PUBLIC_KEY' in os.environ:
    CLIENT_CONFIG.PUBLIC_KEY = os.environ['WXUPDATEDEMO_TESTING_PUBLIC_KEY']

def update_PyUpdaterClientConfig(client_config, port):
    """
    Update PyUpdater client config.

    This is the configuration (sometimes stored in client_config.py)
    which tells the application where to look for updates.

    The main role of this method to set the UPDATE_URLS in the
    client config.  Because this demo app uses an ephemeral port
    for its file server, the UPDATE_URLS can't be predetermined.

    When called from an automated test, this method if also used
    to set the application's PUBLIC_KEY, which would otherwise be
    generated by "pyupdater keys -c" and stored in client_config.py
    """
    if client_config:
        CLIENT_CONFIG.APP_NAME = client_config.APP_NAME
        CLIENT_CONFIG.COMPANY_NAME = client_config.COMPANY_NAME
        CLIENT_CONFIG.MAX_DOWNLOAD_RETRIES = client_config.MAX_DOWNLOAD_RETRIES
        CLIENT_CONFIG.PUBLIC_KEY = client_config.PUBLIC_KEY
    update_url = 'http://localhost:%s' % port
    CLIENT_CONFIG.UPDATE_URLS = [update_url]
