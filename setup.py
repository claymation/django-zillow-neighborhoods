from setuptools import setup, find_packages

setup(
    name = "django-zillow",
    version = "0.2.0",
    author = "Clay McClure",
    author_email = "clay@daemons.net",
    url = 'https://github.com/claymation/django-zillow',
    description = "Django app for importing and querying Zillow's neighborhood data",
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
