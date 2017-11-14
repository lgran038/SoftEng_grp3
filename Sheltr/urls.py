from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r"^shelter/", include("shelter.urls")),
    url(r"^user/", include("user.urls")),
    url(r'^admin/', admin.site.urls),
]
