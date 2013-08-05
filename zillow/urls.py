from django.conf.urls import patterns, include, url


urlpatterns = patterns('zillow.views',
    url(r'neighborhoods\.geojson$', 'neighborhoods', name='neighborhoods'),
)
