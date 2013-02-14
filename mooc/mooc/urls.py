from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.views.generic.base import TemplateView

# This kicks off the admin panel.
admin.autodiscover()

# Base URL patterns. The rule is that except for "front", these go to their
# respective apps.
urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'mooc.views.home', name='home'),
    # url(r'^mooc/', include('mooc.foo.urls')),
    
    # Use a basic TemplateView to get the index page.
    # We might make it into a fancy blog feed one day (maybe import the
    # tumblr RSS as a planet-like thing).
    url(r'^$', TemplateView.as_view(template_name="index.html"), name='index'),

    # Django-admin panel
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),
)

