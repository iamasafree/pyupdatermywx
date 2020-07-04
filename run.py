"""
run.py

MyPyUpdaterWx demo can be launched by running "python run.py"
"""
import argparse
import logging
import os
import sys

import pyupdatermywx
from pyupdatermywx.main import PyUpdaterMyWxApp

stderrHandler = logging.StreamHandler(sys.stderr)
stderrHandler.setFormatter(logging.Formatter(logging.BASIC_FORMAT))


# FILE_SERVER_PORT = 80


def parse_args(argv):
    """
    Parse command-line args.
    """
    usage = "%(prog)s [options]\n"
    parser = argparse.ArgumentParser(usage=usage)
    parser.add_argument("--debug", help="increase logging verbosity", action="store_true")
    parser.add_argument("--version", help="displays version", action='store_true')
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


def _initialize_logging(debug=False):
    """
    Initialize logging.
    """
    logger = logging.getLogger(__name__)
    if debug or 'WXUPDATEDEMO_TESTING' in os.environ:
        level = logging.DEBUG
    else:
        level = logging.INFO
    logger.setLevel(level)
    logging.getLogger("pyupdater").setLevel(level)
    logging.getLogger("pyupdater").addHandler(stderrHandler)


def run(argv, client_config=None):
    """
    The main entry point.
    """
    args = parse_args(argv)
    if args.version:
        display_version_and_exit()

    _initialize_logging(args.debug)

    file_server_host = os.environ.get('PYUPDATER_FILESERVER_HOST')
    if not file_server_host:
        message = 'The PYUPDATER_FILESERVER_HOST environment variable is not set.'
        logging.getLogger(__name__).warning(message)
    else:
        logging.getLogger(__name__).info(f'PYUPDATER_FILESERVER_HOST = {file_server_host}')
    file_server_port = os.environ.get('PYUPDATER_FILESERVER_PORT')
    if not file_server_port:
        message = 'The PYUPDATER_FILESERVER_PORT environment variable is not set.'
        logging.getLogger(__name__).warning(message)
    else:
        logging.getLogger(__name__).info(f'PYUPDATER_FILESERVER_PORT = {file_server_port}')

    # Create the app and run its main loop to process events.
    #
    # If being called by automated testing, the main loop
    # won't be run and the app will be returned.
    # app = PyUpdaterMyWxApp(file_server_port=FILE_SERVER_PORT, debug=args.debug)
    app = PyUpdaterMyWxApp(file_server_host, file_server_port)
    if argv[0] != 'RunTester':
        app.MainLoop()
    return app


if __name__ == "__main__":
    run(sys.argv)
