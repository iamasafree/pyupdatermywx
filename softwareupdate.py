"""
software updater with pyupdater client
"""
import logging
import os
import sys

from pyupdater.client import Client

import pyupdatermywx
from pyupdatermywx.config import update_PyUpdaterClientConfig, CLIENT_CONFIG

stderrHandler = logging.StreamHandler(sys.stderr)
stderrHandler.setFormatter(logging.Formatter(logging.BASIC_FORMAT))


# TODO: подключить нормальный логгер, найти в примерах на pyupdater, можно подключить несколько логгеров
#  переменные, которые доступны в этой функции определены в advanced на pyupdater
#  можно попробовать выводить их в ui форме?
def print_status_info(info):
    total = info.get(u'total')
    downloaded = info.get(u'downloaded')
    status = info.get(u'status')
    print(downloaded, total, status)


class SoftwareUpdate():
    def __init__(self, file_server_port, debug=False):
        self._initialize_logging(debug)
        update_PyUpdaterClientConfig(file_server_port)

    # TODO: не до конца разобрался, как работает логирование во flask
    def _initialize_logging(self, debug=False):
        """
        Initialize logging.
        """
        logger = logging.getLogger(__name__)
        logger.addHandler(stderrHandler)
        if debug or 'WXUPDATEDEMO_TESTING' in os.environ:
            self.level = logging.DEBUG
        else:
            self.level = logging.INFO
        logger.setLevel(self.level)
        logger.setLevel(self.level)

    def check_for_updates(self, debug=False):
        """
        Check for updates.

        Channel options are stable, beta & alpha
        Patches are only created & applied on the stable channel
        """

        assert CLIENT_CONFIG.PUBLIC_KEY is not None
        self.client = Client(CLIENT_CONFIG, refresh=True, progress_hooks=[print_status_info])

        self.app_update = self.client.update_check(CLIENT_CONFIG.APP_NAME,
                                                   pyupdatermywx.__version__,
                                                   channel='stable')

        if self.app_update:
            self.app_update.download()
            if self.app_update.is_downloaded():
                self.app_update.extract_restart()
        else:
            pass
        return 0
