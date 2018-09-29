from django.contrib.gis.db import models
from django.db.models import Manager as GeoManager

class Neighborhood(models.Model):
    """Auto-generated model for Zillow neighorhood shapefiles"""
    state = models.CharField(max_length=2)
    county = models.CharField(max_length=43)
    city = models.CharField(max_length=64)
    name = models.CharField(max_length=64)
    regionid = models.IntegerField()
    geom = models.MultiPolygonField(geography=True)

    objects = GeoManager()

    def __unicode__(self):
        return '{name}, {city}, {state}'.format(name=self.name, city=self.city, state=self.state)

    @property
    def feature(self):
        """
        Return a GeoJSON Feature object for this neighborhood.

        See: http://www.geojson.org/geojson-spec.html#feature-objects
        """
        return {
            'type': 'Feature',
            'geometry': {
                'type': self.geom.geom_type,
                'coordinates': self.geom.coords,
            },
            'properties': {
                'description': self.name,
            }
        }

# Auto-generated `LayerMapping` dictionary for Neighborhood model
neighborhood_mapping = {
    'state' : 'State',
    'county' : 'County',
    'city' : 'City',
    'name' : 'Name',
    'regionid' : 'RegionID',
    'geom' : 'MULTIPOLYGON',
}
