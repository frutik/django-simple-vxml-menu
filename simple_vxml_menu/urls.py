from django.conf.urls.defaults import *

urlpatterns = patterns('',
    url(r'(?P<slug>[-\w]+)/$', 'simple_vxml_menu.views.vxml_file'),
)
