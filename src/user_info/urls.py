from common.url_resolver import child_url_resolver
from .views import *

url = child_url_resolver(__file__)
urlpatterns = [
    url('register/', register),
    url('search-perusahaan/', SearchPerusahaan.as_view()),
    url('search-produk/', SearchProduk.as_view()),
    url('get-filters/', get_filters),
    url('registration-info', registration_info),
    url('info-loker', InfoLoker.as_view()),
]
