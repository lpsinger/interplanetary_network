from django.core.files import File
from os.path import basename
from urllib.request import urlretrieve, urlcleanup
from urllib.parse import urlsplit
from ipn.models.Lvc_Preliminary import Lvc_Preliminary
from astropy.io import fits

class Fits:
  def download_fits(lvc_preliminary):
    try:
      file_name = str(lvc_preliminary.id) + ".fits"
      filepath, _ = urlretrieve(lvc_preliminary.skymap_fits_url, file_name)
      # file = File(open(filepath, 'rb'))
      lvc_preliminary.skymap = fits.open(filepath)
      lvc_preliminary.save(update_fields=['skymap'])

    # comment this out to persist the file for development purposes
    finally:
      urlcleanup()

  def load_fits(filename):
    return File(open(filename, 'rb'))

