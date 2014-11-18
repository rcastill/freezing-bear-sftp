from Tkinter import Tk
from frame import *
import sys
# from sftp import *
from util import *

class App():
	def __init__(self):
		DataManager.load()

		if len(sys.argv) == 1:
			# abrir interfaz de configuracion.
			self.master = Frame(DataManager.save)
			self.master.mainloop()
#		else:
			# establecer protocolo de envio de datos.
#			sftp = SFTPHandler(DataManager.data['ip'], DataManager.data['user'], DataManager.data['password'])
#			sftp.send(*sys.argv)

if __name__ == "__main__":
	app = App()