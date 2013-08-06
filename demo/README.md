Neighborhoods
=============

A sample Django project demonstrating how to use [django-zillow-neighborhoods](https://github.com/claymation/django-zillow-neighborhoods).


How To
------

These step-by-step instructions will help you get the demo app running locally. I assume you're on a Mac and using [Homebrew](http://brew.sh) (you should be), but most of the commands are appropriate for any *nix variant.

    # Install PostGIS 2.0 using Homebrew (on a Mac)
    $ brew install postgis

    # Make a project directory and virtualenv (using virtualenvwrapper)
    $ mkproject neighborhoods

    # Clone the repo
    $ git clone http://github.com/claymation/neighborhoods.git .

    # Install the requirements: Django, django-zillow, psycopg2, etc
    $ pip install -r requirements.txt

    # Create a database user (needs to be a superuser to install the PostGIS extension)
    $ createuser --superuser neighborhoods

    # Create a database
    $ createdb --owner neighborhoods neighborhoods

    # Install the PostGIS extension
    $ psql -U neighborhoods -d neighborhoods -c 'create extension postgis;'

    # Build the model tables
    $ neighborhoods/manage.py syncdb

    # Import the Zillow neighborhood data
    # NB: Zillow does not have data for all states; expect some 404s
    $ neighborhoods/manage.py import_zillow_neighborhoods
    Importing AL neighborhoods
    Importing AK neighborhoods
    Importing AZ neighborhoods
    Importing AR neighborhoods
    ...

    # Run the development server and launch a browser
    $ (sleep 2 && open http://localhost:8000) & neighborhoods/manage.py runserver

    # Or, using Foreman:
    $ (sleep 2 && open http://localhost:8000) & foreman start


MapBox
------

Many good web map APIs exist, but for this project I've chosen to use [MapBox](http://www.mapbox.com). To use your own MapBox map in this project, simply set the `MAPBOX_ID` environment variable prior to running the development server:

    $ (sleep 2 && open http://localhost:8000) & MAPBOX_ID='your-map-box-id' neighborhoods/manage.py runserver

If you're using [Foreman](http://ddollar.github.io/foreman/), you can set `MAPBOX_ID` in your `.env` file.
