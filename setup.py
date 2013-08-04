import os

from setuptools import setup, find_packages

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name = "django-zillow",
    version = "0.1.0",
    author = "Clay McClure",
    author_email = "clay@daemons.net",
    url = 'https://github.com/claymation/django-zillow',
    description = "Django model and management command for working with Zillow's free neighborhood data",
    long_description = read('README'),
    keywords = "zillow neighborhood django geodjango postgis",
    packages = find_packages(),
    install_requires = ['django-localflavor'],
    classifiers = [
        "Development Status :: 3 - Alpha",
        "Environment :: Web Environment",
        "Framework :: Django",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: BSD License",
        "Topic :: Internet :: WWW/HTTP",
        "Topic :: Scientific/Engineering :: GIS",
    ],
)
