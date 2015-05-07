from .webservice import WebService
from .webservicejob import WebServiceJob
from .services import JSWebService, PythonWebService


def webservice_class_for(type):
    if type == 'nodejs':
        return JSWebService
    elif type == 'uwsgi-python':
        return PythonWebService
