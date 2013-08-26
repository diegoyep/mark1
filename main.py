import tornado.httpserver
import tornado.web
import tornado.ioloop
import tornado.options
import os.path
 
from config.config import Config

config = Config() 

# class Application(tornado.web.Application):
# 	def __init__(self):
		# handlers = [
		# 	(r'/', MainHandler)
		# 	]

		# settings = dict(
		# 		template_path = os.path.join(os.path.dirname(__file__),  'public\\templates'),
		# 		debug = True
		# 		)

# 		#tornado.web.Application.__init__(self,handlers, **settings)

class MainHandler(tornado.web.RequestHandler):
	def get(self):
		self.render(
			"index.html",
			page_title = " Mark1 Project"
			)


if __name__ == '__main__':
	tornado.options.parse_command_line()
	server = tornado.httpserver.HTTPServer(tornado.web.Application(
	 config.handlers, **config.settings))
	server.listen(8000)
	tornado.ioloop.IOLoop.instance().start()
			 	