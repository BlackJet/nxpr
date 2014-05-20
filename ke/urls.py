from django.conf.urls.defaults import patterns, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
#admin.autodiscover()
from ke import settings
import inspect
import importlib
urls = []
for moduleName in settings.VIEWS:
    module = importlib.import_module(moduleName)
    for objectName in dir(module):
        object = getattr(module,objectName)
        if inspect.isfunction(object) and hasattr(object,'view'):
            urls.append(url(object.view['url'],object))

urlpatterns = patterns('',*urls)
urlpatterns += patterns('',url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}))


#urlpatterns = patterns('',
#      url(r'^$', user_view.get_home),
#      url(r'^register/$', direct_to_template,{'template':'register.html'},),
#      url(r'^profile/$', user_view.get_home),
#
#      url(r'^profile_part/$', direct_to_template,{'template':'profile_part.html'},),
#      url(r'^profile_edit/$', user_view.get_home, name="profile_edit"),
#      url(r'^profile_edit_part/$', direct_to_template,{'template':'profile_edit.html'},),
#      url(r'^template/([a-z0-9_]+)/$', Utils.get_template,),
#      url(r'^story/$', user_view.get_home),
#      url(r'^story_part/$', story_view.index,),
##      url(r'^story/(?P<page>\w{0,50})$', story_view.index,),
#      url(r'^story/(\d+)$', story_view.get_story,),
#
#      url(r'^api/', include('api.urls')),
#
#      url(r'^test/', direct_to_template,{'template':'test.html'}),
#      url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),

    #      url(r'^account/', include('ke.core.account.urls')),
    # Examples:
    # url(r'^$', 'nx.views.home', name='home'),
    # url(r'^nx/', include('nx.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^ad min/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
#)
