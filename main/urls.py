from django.urls import path
from . import views


urlpatterns = [
    path('register/',views.register ,name='register'),
    path('login/',views.logins,name='login'),
    path('',views.deposite_name,name='deposite_name'),
    path('user_ui2/<int:id>/',views.user_UI2,name='user_ui2'),
    path('deposits/<int:id>/',views.Deposits,name ='deposits'),
    path('withdrow/<int:id>/',views.withdrows,name = 'withdrow'),
    path('balance_checks/<int:id>/',views.balance_checks,name = 'balance_checks'),
    path('transfers/<int:id>/',views.transfers,name = 'transfers'),
    path('logout/',views.logouts,name = 'logout')


]