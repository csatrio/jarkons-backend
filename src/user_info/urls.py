from common.url_resolver import child_url_resolver
from .views import *

url = child_url_resolver(__file__)
urlpatterns = [
    url('register/', register),
    url('search-perusahaan/', search_perusahaan.as_view()),
    url('search-produk/', search_produk.as_view()),
]
