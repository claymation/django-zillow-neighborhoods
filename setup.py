import os
from setuptools import setup

# Utility function to read the README file.
# Used for the long_description.  It's nice, because now 1) we have a top level
# README file and 2) it's easier to type in the README file than to put a raw
# string in below ...
def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name = "django-zillow",
    version = "0.0.1",
    author = "Clay McClure",
    author_email = "clay@daemons.net",
    description = "Django model and management command for working with Zillow's free neighborhood data",
    keywords = "zillow",
    packages = ['zillow'],
    long_description = read('README'),
    classifiers = [
        "Development Status :: 1 - Planning",
        "License :: OSI Approved :: BSD License",
        "Environment :: Web Environment",
        "Framework :: Django",
        "Intended Audience :: Developers",
    ],
)
