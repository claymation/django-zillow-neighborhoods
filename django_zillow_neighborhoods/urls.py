from django.conf.urls import patterns, include, url


urlpatterns = patterns('django_zillow_neighborhoods.views',
    url(r'neighborhoods\.geojson$', 'neighborhoods', name='neighborhoods'),
)
