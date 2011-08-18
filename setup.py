import ez_setup
ez_setup.use_setuptools()
from setuptools import setup
setup(
    name = "django-simple-vxml-menu",
    version = "0.1",
    packages = "django-simple-vxml-menu",
    author = "Andrew Kornilov",
    author_email = "frutik@gmail.com",
    description = "A package to help manage vxml menus in Django",
    url = "http://github.com/frutik/django-simple-vxml-menu/",
    include_package_data = True
)
