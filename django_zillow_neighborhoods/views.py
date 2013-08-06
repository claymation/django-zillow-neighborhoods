import json

from django.contrib.gis.geos import Polygon
from django.conf import settings
from django.http import HttpResponse, HttpResponseBadRequest

from pyproj import Geod

from .models import Neighborhood


# Queries specifying a bounds larger than this (measured diagonally) will be rejected
DEFAULT_MINIMUM_DIAGONAL_IN_METERS = 10**6
MINIMUM_DIAGONAL_IN_METERS = getattr(settings,
                                     'ZILLOW_NEIGHBORHOODS_MINIMUM_DIAGONAL_IN_METERS',
                                     DEFAULT_MINIMUM_DIAGONAL_IN_METERS)


def neighborhoods(request):
    """Return GeoJSON-encoded neighborhood objects matching the query"""
    try:
        bounds = request.GET['bounds']
    except KeyError:
        return HttpResponseBadRequest('Missing `bounds` parameter')

    try:
        bbox = Polygon.from_bbox(bounds.split(','))
    except ValueError:
        return HttpResponseBadRequest('Illegal `bounds` parameter')

    diagonal_in_meters = Geod(ellps='WGS84').inv(*bbox.extent)[2]
    if diagonal_in_meters > MINIMUM_DIAGONAL_IN_METERS:
        return HttpResponseBadRequest('`bounds` parameter out of range')

    neighborhoods = Neighborhood.objects.filter(geom__bboverlaps=bbox)

    features = [neighborhood.feature for neighborhood in neighborhoods]
    feature_collection = {
        'type': 'FeatureCollection',
        'features': features,
    }

    return HttpResponse(json.dumps(feature_collection), content_type='application/json')
