from tornado.web import url

from .handlers import HearBeatHandler


__all__ = ('URLsRegistry',)


class URLsRegistry(object):

    _urls = []

    @classmethod
    def register(cls, urls):
        cls._urls.extend(urls)

    @classmethod
    def get(cls):
        return tuple(cls._urls)


URLS = (
    url(r'/heartbeat', HearBeatHandler),
)


URLsRegistry.register(urls=URLS)
