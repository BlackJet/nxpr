import os, sys
sys.path.insert(0,'/home/aynu/pyenv/p271/lib/python2.7/site-packages')
'''path = '/home/aynu/Documents/projects/ke'
if path not in sys.path:
    sys.path.append(path)'''
sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)) + '/..')
os.environ['DJANGO_SETTINGS_MODULE'] = 'ke.settings'
import django.core.handlers.wsgi
    
application = django.core.handlers.wsgi.WSGIHandler()