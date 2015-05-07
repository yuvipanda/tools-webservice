import os

from .webservice import WebService


class JSWebService(WebService):
    NAME = 'nodejs'
    QUEUE = 'webgrid-generic'

    def check(self):
        package_path = os.path.expanduser('~/www/js/package.json')
        if os.path.exists(package_path):
            return True, ""
        else:
            return False, 'Could not find ~/www/js/package.json. Are you sure you have a ' \
                          'proper nodejs application in ~/www/js?'

    def run(self, port):
        os.chdir(os.path.expanduser('~/www/js'))
        os.execv('/usr/bin/npm', ['/usr/bin/npm', 'start'])

class PythonWebService(WebService):
    NAME = 'uwsgi-python'
    QUEUE = 'webgrid-generic'
    def check(self):
        src_path = os.path.expanduser('~/www/python/src')
        if os.path.exists(src_path):
            return True, ""
        else:
            return False, 'Could not find ~/www/python/src. Are you sure you have a ' \
                          'proper uwsgi application in ~/www/python/src?'
        return os.path.exists(src_path)

    def run(self, port):
        args = [
            '/usr/bin/uwsgi',
            '--plugin', 'python',
            '--http-socket', ':' + str(port),
            '--chdir', os.path.expanduser('~/www/python/src'),
            '--logto', os.path.expanduser('~/uwsgi.log'),
            '--callable', 'app',
            '--manage-script-name',
            '--workers', '4',
            '--mount', '/%s=%s' % (self.toolname, os.path.expanduser('~/www/python/src/app.py')),
            '--die-on-term',
            '--strict',
            '--master'
        ]

        if os.path.exists(os.path.expanduser('~/www/python/venv')):
            args += ['--venv', os.path.expanduser('~/www/python/venv')]

        if os.path.exists(os.path.expanduser('~/www/python/uwsgi.ini')):
            args += ['--ini', os.path.expanduser('~/www/python/uwsgi.ini')]

        os.execv('/usr/bin/uwsgi', args)

