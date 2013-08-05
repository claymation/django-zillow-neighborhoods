django-zillow
=============

Django app for importing and querying [Zillow's free neighborhood data](http://www.zillow.com/howto/api/neighborhood-boundaries.htm).


Demo
----

The [Neighborhoods project](https://github.com/claymation/neighborhoods) demonstrates how to incorporate django-zillow into a Django project.


Requirements
------------

* Python >= 2.6
* Django >= 1.2
* GeoDjango's required geospatial libraries: GEOS, PROJ.4, GDAL


Installation
------------

1. Setup GeoDjango (see: http://docs.djangoproject.com/en/dev/ref/contrib/gis/install/)

2. Add 'zillow' to `INSTALLED_APPS`

3. Install the database schema:

        $ django-admin.py syncdb

4. Import the neighborhood shapefiles:

        $ django-admin.py import_zillow_neighborhoods
