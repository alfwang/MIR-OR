from django.conf.urls import patterns, include, url, handler404
from django.http import Http404

urlpatterns = patterns('',
	url(r'^$', 'mir.views.home', name = 'home'),
    url(r'^result$', 'mir.views.parseResult', name = 'result'),
)

# handler404 = 'mir.views.myView'