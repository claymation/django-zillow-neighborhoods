from django.conf import settings

def mapbox_id(request):
    return { 'mapbox_id': settings.MAPBOX_ID }
