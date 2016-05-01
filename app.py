from project.common import URLsRegistry
from project.settings import settings

from tornado.ioloop import IOLoop
from tornado.web import Application as BaseApplication


class Application(BaseApplication):

    def __init__(self, **kwargs):
        kwargs['debug'] = settings.DEBUG
        super(Application, self).__init__(handlers=URLsRegistry.get(), **kwargs)


if __name__ == '__main__':

    application = Application()
    application.listen(port=settings.PORT)

    IOLoop.instance().start()
