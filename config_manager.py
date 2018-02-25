import json
from pprint import pprint

class Config():
	CONFIG_FILE_NAME = 'config.json'
	data = {}

	def __init__(self):
		self.data = self.get_config()

	def get_config(self):
		return json.load(open(self.CONFIG_FILE_NAME))
	def set_config(self):
		with open(self.CONFIG_FILE_NAME, 'w+') as conf:
			json.dump(self.data,conf)

	def add(self,*args):
		for k,v in args:
			self.data[k]=v
	def get(self,*args):
		values = []
		for k in args:
			values.append(self.data[k])
		return values
	def is_set(self, *args):
		return all(map( lambda x: x in self.data.keys(),args ))

	def empty(self):
		self.data = {}

	def __str__(self):
		return self.data.__str__()