from django.conf.urls import include, url
from django.contrib import admin

from printing_app import urls as printing_app_urls

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', include(printing_app_urls)),
]
