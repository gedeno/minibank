from django.urls import path
from . import views


urlpatterns = [
    path('register/',views.register ,name='register'),
    path('login/<int:uss_id>/',views.logins,name='login'),
    path('/<int:uss_id>/',views.user_UI2,name='user_ui2'),
    path('deposits/<int:uss_id>/',views.Deposits,name ='deposits')

]