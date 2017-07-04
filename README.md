django-zillow-neighborhoods
===========================

Django app for importing and querying [Zillow's free neighborhood data](http://www.zillow.com/howto/api/neighborhood-boundaries.htm).


Demo
----

The [included demo project](https://github.com/claymation/django-zillow-neighborhoods/tree/master/demo) demonstrates how to incorporate `django-zillow-neighborhoods` into a Django project.


Requirements
------------

* Python >= 2.6
* Django >= 1.2
* GeoDjango and its prerequisites:
  * GEOS
  * PROJ.4
  * GDAL
  * a spatial database (e.g., PostGIS)


Installation
------------

1. Install the library

        $ pip install django-zillow-neighborhoods

2. Add 'django_zillow_neighborhoods' to `INSTALLED_APPS`

3. Install the database schema:

        $ django-admin.py syncdb

4. Import the neighborhood shapefiles:

        $ django-admin.py import_zillow_neighborhoods
