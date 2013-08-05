django-zillow
=============

django-zillow is a Django application providing models and management
commands for working with [Zillow's free neighborhood data](http://www.zillow.com/howto/api/neighborhood-boundaries.htm).


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
