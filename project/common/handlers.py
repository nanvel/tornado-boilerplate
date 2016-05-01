from tornado.web import RequestHandler


__all__ = ('HearBeatHandler',)


class HearBeatHandler(RequestHandler):

    def get(self):
        self.write("Alive.")
