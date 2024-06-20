from django.urls import re_path

from hunts import views

app_name = 'hunts'

urlpatterns = [
    re_path(r'^all_hunts/$', views.all_hunts, name='all_hunts'),
    re_path(r'^create_hunt/$', views.create_hunt, name='create_hunt'),
    re_path(r'^_create_new_hunt/$', views.create_new_hunt, name='create_new_hunt'),
    re_path(r'^get_hunt/$', views.get_hunt, name='get_hunt'),
    re_path(r'^update_hunt/$', views.update_hunt, name='update_hunt'),

]