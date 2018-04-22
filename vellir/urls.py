from django.conf.urls import url, include
from django.contrib import admin
from django.conf import settings
import debug_toolbar

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'', include('sparkvellir.urls')),
]


if settings.DEBUG:
    urlpatterns = [
        url(r'^__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns