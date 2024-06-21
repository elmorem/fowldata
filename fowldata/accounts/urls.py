from django.urls import path, re_path
from accounts import views

app_name = 'accounts'

urlpatterns = [
    path('signup/', views.signup, name="signup"),
    path('login/', views.login, name="login"),
   # path('logout/', name="logout"),
   # path('profile/', views.profile, name="profile"),
   # path('update_profile/', views.update_profile, name="update_profile"),
   # path('signup_thank_you/', views.signup_thank_you, name="signup_thank_you"),
]