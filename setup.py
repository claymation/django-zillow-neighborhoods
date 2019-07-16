from setuptools import setup, find_packages

setup(
    name = "django-zillow-neighborhoods",
    version = "0.8.1",
    author = "Clay McClure",
    author_email = "clay@daemons.net",
    url = 'https://github.com/claymation/django-zillow-neighborhoods',
    description = "Django app for importing and querying Zillow's neighborhood data",
    keywords = "zillow neighborhood django geodjango postgis",
    packages = find_packages(),
    install_requires = ['django-localflavor', 'pyproj'],
    classifiers = [
        "Development Status :: 4 - Beta",
        "Environment :: Web Environment",
        "Framework :: Django",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: BSD License",
        "Topic :: Internet :: WWW/HTTP",
        "Topic :: Scientific/Engineering :: GIS",
    ],
)
