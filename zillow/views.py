import json

from django.contrib.gis.geos import Polygon
from django.http import HttpResponse, HttpResponseBadRequest

from .models import Neighborhood


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

    neighborhoods = Neighborhood.objects.filter(geom__bboverlaps=bbox)

    features = [neighborhood.feature for neighborhood in neighborhoods]
    feature_collection = {
        'type': 'FeatureCollection',
        'features': features,
    }

    return HttpResponse(json.dumps(feature_collection), content_type='application/json')
