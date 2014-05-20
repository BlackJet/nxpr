__author__ = 'aynu'
import wolf
import inspect

modules = ('wolf',)

for module in modules:
    m = __import__(module)
    m.hello()


