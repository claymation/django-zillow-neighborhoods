from django.contrib.gis import admin

from .models import Neighborhood

admin.site.register(Neighborhood, admin.OSMGeoAdmin)
