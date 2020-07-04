"""
software updater with pyupdater client
"""
import logging
import sys

from pyupdater.client import Client

import pyupdatermywx
from pyupdatermywx.config import update_PyUpdaterClientConfig, CLIENT_CONFIG


# TODO: подключить нормальный логгер, найти в примерах на pyupdater, можно подключить несколько логгеров
#  переменные, которые доступны в этой функции определены в advanced на pyupdater
#  можно попробовать выводить их в ui форме?
def print_status_info(info):
    total = info.get(u'total')
    downloaded = info.get(u'downloaded')
    status = info.get(u'status')
    print(downloaded, total, status)


class SoftwareUpdate():
    def __init__(self, file_server_host, file_server_port):
        update_PyUpdaterClientConfig(file_server_host, file_server_port)

    def check_for_updates(self):
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
