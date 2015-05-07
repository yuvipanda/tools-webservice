import subprocess
import os


class WebServiceJob(object):
    def __init__(self, webservice):
        self.webservice = webservice

    def submit(self):
        command = ['qsub',
                   '-e', os.path.expanduser('~/error.log'),
                   '-o', os.path.expanduser('~/error.log'),
                   '-i', '/dev/null',
                   '-q', self.webservice.queue,
                   '-l', 'h_vmem=%s,release=%s' % (self.webservice.memlimit, self.webservice.release),
                   '-b', 'y',
                   '-N', '%s-%s' % (self.webservice.type, self.webservice.toolname),
                   '/usr/bin/webservice-runner --type %s' % self.webservice.type]

        subprocess.check_call(command, stdout=open(os.devnull, 'wb'))
