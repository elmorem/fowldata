from django.urls import re_path
from accounts import views

app_name = 'accounts'

urlpatterns = [
    re_path(r'^create_account/$', views.create_account, name="create_account"),
    ]