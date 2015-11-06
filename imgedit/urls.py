from django.conf.urls import patterns, url
from imgedit import views

urlpatterns = patterns('',
    url(r'^rotate_image_right/$', views.rotate_image_right, name='rotate_right'),
    url(r'^change_image_color/$', views.change_image_color, name='change_color'),
 )