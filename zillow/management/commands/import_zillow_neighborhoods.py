import os
import shutil
import tempfile
import urllib2
import zipfile

from django.contrib.gis.gdal import DataSource
from django.contrib.gis.utils import LayerMapping
# TODO -- Replace STATE_CHOICES with US_STATES when 1.3 ships
from django.contrib.localflavor.us.us_states import STATE_CHOICES
from django.core.management.base import NoArgsCommand, CommandError

from zillow.models import Neighborhood, neighborhood_mapping

EXCLUDE_STATES = ('AS', 'DE', 'GU', 'NH', 'ND', 'MP', 'OK', 'PR', 'SC', 'SD', 'VT', 'VI', 'WV', 'WY')

class Command(NoArgsCommand):
    help = "Import Zillow neighborhood boundaries"
    output_transaction = True
    requires_model_validation = False
    
    def handle_noargs(self, **options):
        ZILLOW_SHAPEFILE_URL = 'http://www.zillow.com/static/shp/ZillowNeighborhoods-%s.zip'
        ZILLOW_SHAPEFILE_DIR = tempfile.mkdtemp()

        try:
            # Clear neighborhood table
            Neighborhood.objects.all().delete()

            for abbrev, name in STATE_CHOICES:
                if abbrev in EXCLUDE_STATES:
                    continue

                self.stdout.write('Importing %s neighborhoods\n' % abbrev)

                # Fetch the zipped shapefile from Zillow
                try:
                    url = ZILLOW_SHAPEFILE_URL % abbrev
                    zip_file = download(url)
                except Exception, e:
                    self.stderr.write('Warning: Failed to fetch %s: %s\n' % (url, str(e)))
                    continue

                # Extract and import the shapefile
                try:
                    zipfile.ZipFile(zip_file).extractall(ZILLOW_SHAPEFILE_DIR)
                    shapefile = os.path.join(ZILLOW_SHAPEFILE_DIR, 'ZillowNeighborhoods-%s.shp' % abbrev)
                    import_neighborhoods_shapefile(shapefile)
                finally:
                    zip_file.close()
        finally:
            shutil.rmtree(ZILLOW_SHAPEFILE_DIR)

def import_neighborhoods_shapefile(shapefile):
    """Import Zillow neighborhood boundaries from a shapefile"""

    # Load the shapefile
    ds = DataSource(shapefile)

    # Import the neighborhoods
    lm = LayerMapping(Neighborhood, ds, neighborhood_mapping,
                      transform=False, encoding='iso-8859-1')
    lm.save(strict=True, verbose=False)

def download(url):
    """Helper function to download a file to a temporary location."""
    remote = urllib2.urlopen(url)
    local = tempfile.TemporaryFile()
    try:
        shutil.copyfileobj(remote, local)
    except:
        local.close()
        raise
    finally:
        remote.close()
    return local
