from django.conf.urls import patterns, url
from trips import views

urlpatterns = patterns('',
    url(r'^$', views.my_trips, name='my_trips'),
    url(r'^users/$', views.users, name='users'),
    url(r'^add_trip/$', views.add_trip, name='add_trip'), # NEW MAPPING!
    url(r'^u/(?P<trip_title_slug>[\w\-]+)/$', views.view_my_trip, name='view_my_trip'),  # New!
    url(r'^(?P<user_username>[a-zA-Z0-9]+)/$', views.index, name='index'),
    url(r'^(?P<user_username>[a-zA-Z0-9]+)/(?P<trip_title_slug>[\w\-]+)/$', views.view_trip, name='view_trip'),
    url(r'^(?P<trip_title_slug>[\w\-]+)/add_experience/$', views.add_experience, name='add_experience'),  # New!
    url(r'^(?P<trip_title_slug>[\w\-]+)/(?P<experience_id>\d+)/$', views.view_experience, name='view_experience'),  # New!
    url(r'^(?P<trip_title_slug>[\w\-]+)/(?P<experience_id>\d+)/edit_experience/$', views.edit_experience, name='edit_experience'),  # New!
    url(r'^(?P<trip_title_slug>[\w\-]+)/(?P<experience_id>\d+)/delete_experience/$', views.delete_experience, name='delete_experience'),
    url(r'^(?P<trip_title_slug>[\w\-]+)/(?P<experience_id>\d+)/add_image/$', views.add_image, name='add_image'),  # New!
    )