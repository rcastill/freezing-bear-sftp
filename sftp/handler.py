__author__ = 'Rodolfo'

import paramiko
from constants import *

class SFTPHandler(paramiko.Transport):
    def __init__(self, host, username, password, callback=None):
        paramiko.Transport.__init__((host, DEFAULT_PORT))
        self.connect(username=username, password=password)
        self._sftp = paramiko.SFTPClient.from_transport(self)
        self._callback = callback

    def set_callback(self, callback):
        self._callback = callback

    def send(self, rpath, *fpaths):
        for fpath in fpaths:
            self._sftp(fpath, rpath, callback=self._callback)

    def close(self):
        self._sftp.close()
        self.close()
