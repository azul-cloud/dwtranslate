from django.conf.urls import patterns, include, url

from main import views

urlpatterns = patterns('',
    url(r'^$', views.home, name="home"),
    url(r'^about/$', views.about, name="about"),
    url(r'^experience/$', views.experience, name="experience"),
    url(r'^contact/$', views.contact, name="contact"),
)