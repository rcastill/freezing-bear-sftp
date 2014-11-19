from const import *
from exceptions import *
from os.path import exists
import json
import re

class NotAValidIPException(Exception):
	def __str__(self):
		return repr('Not a valid IP. Metadata file corrupted.')

def ascii_encode_dict(data):
    ascii_encode = lambda x: x.encode('ascii')
    return dict(map(ascii_encode, pair) for pair in data.items())

class DataManager(object):
	data = { 'ip': '', 'user': '', 'remote': '', 'password': '' }

	@staticmethod
	def load():
		if not exists(META_FILE):
			return

		# asumiendo que el archivo existe.
		with open(META_FILE, 'r') as meta:
			data = json.load(meta, object_hook=ascii_encode_dict)

			DataManager.data['password'] 	= data['password']
			DataManager.data['remote'] 		= data['remote']
			DataManager.data['user'] 		= data['user']
			DataManager.data['ip'] 			= data['ip']

	@staticmethod
	def save(data):
		DataManager.data['password'] 	= data['password']
		DataManager.data['remote'] 		= data['remote']
		DataManager.data['user'] 		= data['user']
		DataManager.data['ip'] 			= data['ip']

		with open(META_FILE, 'w') as meta:
			json.dump(DataManager.data, meta)

	@staticmethod
	def validate_ip(ip):
		return True if re.match(IP_REGEX, ip) is not None else False