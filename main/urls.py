from django.urls import path
from . import views


urlpatterns = [
    path('register/',views.register ,name='register'),
    path('login/',views.logins,name='login'),
    path('user_ui/',views.User_UI,name='user_ui'),
    path('',views.user_UI2,name='user_ui2'),
]