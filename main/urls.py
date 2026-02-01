from django.urls import path
from . import views


urlpatterns = [
    path('register/',views.register ,name='register'),
    path('login/',views.logins,name='login'),
    path('',views.User_UI,name='user_ui'),
]