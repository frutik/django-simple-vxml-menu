Install

1. Install from pupy: easy_install django-sentry.
2. Add to installet apps (settings.py):

INSTALLED_APPS = (
...
'simple_vxml_menu',
...
)

3. Add url into urls.py:

urlpatterns = patterns('',
    url(r'^vxml/', include('simple_vxml_menu.urls')),
)

4. Create required tables: python manage.py syncdb

5. That's all... You can create your first vxml menu using django admin
