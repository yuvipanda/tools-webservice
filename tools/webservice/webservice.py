import os


class WebService(object):
    def __init__(self, toolname):
        self.toolname = toolname

    @property
    def release(self):
        if hasattr(self.__class__, 'RELEASE'):
            return self.__class__.RELEASE
        return 'trusty' # default!

    @property
    def type(self):
        try:
            return self.__class__.NAME
        except AttributeError:
            raise AttributeError('WebService subclass needs NAME class attribute')

    @property
    def memlimit(self):
        memlimit_path = '/data/project/.system/config/%s.web-memlimit' % self.toolname
        if os.path.exists(memlimit_path):
            with open(memlimit_path) as f:
                return f.read().strip()
        else:
            return '4G'

    @property
    def queue(self):
        if hasattr(self.__class__, 'QUEUE'):
            return self.__class__.QUEUE
        return 'webgrid-generic'

    def check(self):
        raise NotImplementedError()

    def run(self, port):
        raise NotImplementedError()
