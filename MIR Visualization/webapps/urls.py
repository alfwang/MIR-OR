from django.conf.urls import patterns, include, url, handler404
from django.http import Http404

urlpatterns = patterns('',
	url(r'^', include('mir.urls')),
)