from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

from main import urls as mainurls

urlpatterns = patterns('',

    url(r'^admin/', include(admin.site.urls)),
    url(r'^', include(mainurls)),
)
