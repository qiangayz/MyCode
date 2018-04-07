import tornado.ioloop
import tornado.web



class MainHandler(tornado.web.RequestHandler):
    def get(self):
        print(111)
        u = self.get_argument('user')
        p = self.get_argument('pwd')
        self.write("OK")


    def post(self, *args, **kwargs):
        u = self.get_argument('user', None)
        p = self.get_argument('pwd', None)
        print(u,  p)
        f = open("index.html",'rb')
        data = f.read()
        self.write(data)


application = tornado.web.Application([
    (r"/index", MainHandler),
])
if __name__ == "__main__":
    application.listen(8888)
    tornado.ioloop.IOLoop.instance().start()
