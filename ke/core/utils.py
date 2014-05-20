# -*- coding:utf-8 -*-
from django.http import HttpResponse, Http404
import json
from django.shortcuts import render_to_response
from django.template.context import RequestContext

def render_to_json(func):
    def f(*args, **kwargs):
        result = func(*args, **kwargs)
        if not result: result = dict(success=True)
        return HttpResponse(json.dumps(result, sort_keys=True, indent=2),
            content_type='application/json; charset=UTF-8')
    return f

def get_template(request, template):
    return render_to_response('template/%s.html' % template, context_instance=RequestContext(request))

def view(url):
    def w(viewFunc):
        def before(request,*args,**kwargs):
            return viewFunc(request,*args,**kwargs)
        before.view = dict(url = url)
        return before
    return w