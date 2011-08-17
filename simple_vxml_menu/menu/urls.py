from django.conf.urls.defaults import *

urlpatterns = patterns('',
    url(r'(?P<slug>[-\w]+)/$', 'menu.views.vxml_file'),
)
