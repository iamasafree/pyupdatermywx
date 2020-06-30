"""
run.py

MyPyUpdaterWx demo can be launched by running "python run.py"
"""
import argparse
import logging
import os
import sys
import time

from pyupdater.client import Client

import pyupdatermywx
from pyupdatermywx.config import update_PyUpdaterClientConfig, CLIENT_CONFIG
from pyupdatermywx.main import PyUpdaterMyWxApp

logger = logging.getLogger(__name__)
STDERR_HANDLER = logging.StreamHandler(sys.stderr)
STDERR_HANDLER.setFormatter(logging.Formatter(logging.BASIC_FORMAT))

FILE_SERVER_PORT = 50000


# TODO: с этим что-то надо сделать
class UpdateStatus(object):
    """Enumerated data type"""
    # pylint: disable=invalid-name
    # pylint: disable=too-few-public-methods
    UNKNOWN = 0
    NO_AVAILABLE_UPDATES = 1
    UPDATE_DOWNLOAD_FAILED = 2
    EXTRACTING_UPDATE_AND_RESTARTING = 3
    UPDATE_AVAILABLE_BUT_APP_NOT_FROZEN = 4
    COULDNT_CHECK_FOR_UPDATES = 5


UPDATE_STATUS_STR = \
    ['Unknown', 'No available updates were found.',
     'Update download failed.', 'Extracting update and restarting.',
     'Update available but application is not frozen.',
     'Couldn\'t check for updates.']


def parse_args(argv):
    """
    Parse command-line args.
    """
    usage = "%(prog)s [options]\n"
    parser = argparse.ArgumentParser(usage=usage)
    parser.add_argument("--debug", help="increase logging verbosity",
                        action="store_true")
    parser.add_argument("--version", action='store_true',
                        help="displays version")
    return parser.parse_args(argv[1:])


def display_version_and_exit():
    """
    Display version and exit.

    In some versions of PyInstaller, sys.exit can result in a
    misleading 'Failed to execute script run' message which
    can be ignored: http://tinyurl.com/hddpnft
    """
    sys.stdout.write("%s\n" % pyupdatermywx.__version__)
    sys.exit(0)


def initialize_logging(debug=False):
    """
    Initialize logging.
    """
    logger.addHandler(STDERR_HANDLER)
    if debug or 'WXUPDATEDEMO_TESTING' in os.environ:
        level = logging.DEBUG
    else:
        level = logging.INFO
    logger.setLevel(level)
    logging.getLogger("pyupdater").setLevel(level)
    logging.getLogger("pyupdater").addHandler(STDERR_HANDLER)


def print_status_info(info):
    total = info.get(u'total')
    downloaded = info.get(u'downloaded')
    status = info.get(u'status')
    print(downloaded, total, status)


def check_for_updates(debug):
    """
    Check for updates.

    Channel options are stable, beta & alpha
    Patches are only created & applied on the stable channel
    """
    assert CLIENT_CONFIG.PUBLIC_KEY is not None
    client = Client(CLIENT_CONFIG, refresh=True, progress_hooks=[print_status_info])

    # assets_update = client.update_check("assets", pyupdatermywx.__version__)
    # print(f"assets_status: {assets_update}")
    # print(f"assets_status.type: {type(assets_update)}")
    #
    # if assets_update:
    #     assets_update.download()
    #     if assets_update.is_downloaded():
    #         assets_status = UpdateStatus.EXTRACTING_UPDATE_AND_RESTARTING
    #         assets_update.extract()
    #         # assets_update.update_folder
    # else:
    #     assets_status = UpdateStatus.NO_AVAILABLE_UPDATES
    #

    app_update = client.update_check(CLIENT_CONFIG.APP_NAME,
                                     pyupdatermywx.__version__,
                                     channel='stable')

    if app_update:
        if hasattr(sys, "frozen"):
            app_update.download()
            if app_update.is_downloaded():
                status = UpdateStatus.EXTRACTING_UPDATE_AND_RESTARTING
                if 'WXUPDATEDEMO_TESTING_FROZEN' in os.environ:
                    sys.stderr.write("Exiting with status: %s\n"
                                     % UPDATE_STATUS_STR[status])
                    sys.exit(0)
                if debug:
                    logger.debug('Extracting update and restarting...')
                    time.sleep(10)
                app_update.extract_restart()
            else:
                status = UpdateStatus.UPDATE_DOWNLOAD_FAILED
        else:
            status = UpdateStatus.UPDATE_AVAILABLE_BUT_APP_NOT_FROZEN
    else:
        status = UpdateStatus.NO_AVAILABLE_UPDATES

    return status


def run(argv, client_config=None):
    """
    The main entry point.
    """
    args = parse_args(argv)
    if args.version:
        display_version_and_exit()
    initialize_logging(args.debug)
    if FILE_SERVER_PORT:
        update_PyUpdaterClientConfig(client_config, FILE_SERVER_PORT)
        status = check_for_updates(args.debug)
    else:
        status = UpdateStatus.COULDNT_CHECK_FOR_UPDATES
    if 'WXUPDATEDEMO_TESTING_FROZEN' in os.environ:
        sys.stderr.write("Exiting with status: %s\n"
                         % UPDATE_STATUS_STR[status])
        sys.exit(0)
    main_loop = (argv[0] != 'RunTester')
    if not 'WXUPDATEDEMO_TESTING_FROZEN' in os.environ:
        return PyUpdaterMyWxApp.Run(
            UPDATE_STATUS_STR[status], main_loop)
    else:
        return None


if __name__ == "__main__":
    run(sys.argv)
