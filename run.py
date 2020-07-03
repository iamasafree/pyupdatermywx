"""
run.py

MyPyUpdaterWx demo can be launched by running "python run.py"
"""
import argparse
import logging
import sys

import pyupdatermywx
from pyupdatermywx.main import PyUpdaterMyWxApp

stderrHandler = logging.StreamHandler(sys.stderr)
stderrHandler.setFormatter(logging.Formatter(logging.BASIC_FORMAT))

logger = logging.getLogger(__name__)
logger.addHandler(stderrHandler)

FILE_SERVER_PORT = 50000


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


def run(argv, client_config=None):
    """
    The main entry point.
    """
    args = parse_args(argv)
    if args.version:
        display_version_and_exit()

    # Create the app and run its main loop to process events.
    #
    # If being called by automated testing, the main loop
    # won't be run and the app will be returned.
    app = PyUpdaterMyWxApp(file_server_port=FILE_SERVER_PORT, debug=args.debug)
    if argv[0] != 'RunTester':
        app.MainLoop()
    return app


if __name__ == "__main__":
    run(sys.argv)
