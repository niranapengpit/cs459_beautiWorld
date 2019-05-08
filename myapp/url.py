from django.conf.urls import include, url
from myapp.views import home
from django.conf import settings
from django.conf.urls.static import static
urlpatterns=[
    url(r'^cat/(?P<filter>[0-9]+)', home, name = 'home'),
]