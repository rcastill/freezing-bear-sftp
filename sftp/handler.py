__author__ = 'Rodolfo'

import paramiko
from constants import *
from os import path

class SFTPHandler():
    def __init__(self, host, username, password, callback=None):
        self._transport = paramiko.Transport((host, DEFAULT_PORT))
        self._transport.connect(username=username, password=password)
        self._sftp = paramiko.SFTPClient.from_transport(self._transport)
        self._callback = callback

    def set_callback(self, callback):
        self._callback = callback

    def send(self, rpath, *fpaths):
        for fpath in fpaths:
            self._sftp.put(fpath, rpath+path.split(fpath)[-1], callback=self._callback)

    def close(self):
        self._sftp.close()
        self._transport.close()

if __name__ == '__main__':
    from sys import argv

    handler = SFTPHandler("ssh2.inf.utfsm.cl", "rcastill", "nw0ikariaM")
    handler.send("/home/rcastill/", *argv[1:])
    print "Files sent"
    handler.close()
    print "Handler closed."
    raw_input()