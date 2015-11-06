from django.conf.urls import patterns, url
from accounts import views

urlpatterns = patterns('',
        url(r'^$', views.index, name='index'),
        url(r'^add_profile_pic/$', views.add_profile_pic, name='add_profile_pic'),
        
        )