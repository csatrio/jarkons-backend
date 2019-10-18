from common.url_resolver import child_url_resolver
from .views import *

url = child_url_resolver(__file__)
urlpatterns = [
    url('register/', register),
    url('get-filters/', get_filters),
    url('registration-info', registration_info),
    url('search-perusahaan/', SearchPerusahaan.as_view()),
    url('search-produk/', SearchProduk.as_view()),
    url('info-loker/', CrudInfoVacancy.as_view()),
]
