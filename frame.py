from Tkinter import *
from strings import *
from util import DataManager

class Frame(Tk):
	def __init__(self, callback):
		Tk.__init__(self)
		self.callback = callback

		self.title(CAPTION)

		self.ip_label = Label(self, text = IP)
		self.user_label = Label(self, text = USER_NAME)
		self.password_label = Label(self, text = PASSWORD)
		self.remote_label = Label(self, text = REMOTE_PATH)

		ip_variable = StringVar(self, DataManager.data['ip'])
		user_variable = StringVar(self, DataManager.data['user'])
		password_variable = StringVar(self, DataManager.data['password'])
		remote_variable = StringVar(self, DataManager.data['remote'])

		self.ip_entry = Entry(self, textvariable = ip_variable)
		self.user_entry = Entry(self, textvariable = user_variable)
		self.password_entry = Entry(self, textvariable = password_variable, show="*")
		self.remote_entry = Entry(self, textvariable = remote_variable)

		self.confirm_button = Button(self, text = CONFIRM, command = self.save)

		self.ip_label.grid(row = 0, column = 0, sticky = E)
		self.ip_entry.grid(row = 0, column = 1)

		self.user_label.grid(row = 1, column = 0, sticky = E)
		self.user_entry.grid(row = 1, column = 1)

		self.password_label.grid(row = 2, column = 0, sticky = E)
		self.password_entry.grid(row = 2, column = 1)

		self.remote_label.grid(row = 3, column = 0, sticky = E)
		self.remote_entry.grid(row = 3, column = 1)

		self.confirm_button.grid(row = 4, columnspan = 2, column = 0, pady = 4)

	def save(self):
		data = {
			'ip': self.ip_entry.get(),
			'user': self.user_entry.get(),
			'password': self.password_entry.get(),
			'remote': self.remote_entry.get()
		}

		self.callback(data)
		self.destroy()