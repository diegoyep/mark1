from handlers.handlers import *
import os
class Config():

	def __init__(self):
		self.handlers = [
			(r'/',  MainHandler)
			]

		self.settings = dict(
		template_path = os.path.join(os.path.dirname( "main.py") ,  'public\\templates'),
		debug = True
		)

