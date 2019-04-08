import tornado.ioloop
import tornado.web
import json

from write_api import *


class CustomReqHandler(tornado.web.RequestHandler):
    def get(self):

        api_name = self.request.uri.strip('/api').split('?')[0]
        if api_name in API_mappings:
            self.write(json.dumps(API_mappings[api_name](self.get_argument)))
    """
    def post(self):
        username = self.get_argument('username')
        designation = self.get_argument('designation')
        self.write("Wow " + username + " you're a " + designation)
    """

def make_app():
    return tornado.web.Application([ (r"/api/.*", CustomReqHandler)])

if __name__ == "__main__":
    app = make_app()
    app.listen(8888)    # Port Number
    tornado.ioloop.IOLoop.current().start()

