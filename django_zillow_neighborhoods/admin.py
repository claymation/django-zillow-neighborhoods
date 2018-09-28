from django.contrib.gis import admin

from .models import Neighborhood

class NeighborhoodAdmin(admin.OSMGeoAdmin):
  list_display = [
    'name',
    'city',
    'state'
  ]
  list_filter = [
    'state'
  ]

admin.site.register(Neighborhood, NeighborhoodAdmin)
