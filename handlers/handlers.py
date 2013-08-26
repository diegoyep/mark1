import tornado.web

class MainHandler(tornado.web.RequestHandler):
	def get(self):
		self.render(
			"index.html",
			page_title = " Mark1 Project"
			)


class LoginHandler(tornado.web.RequestHandler):
	def get(self):
		pass
		