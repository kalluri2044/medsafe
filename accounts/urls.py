from django.urls import path
from . import views
from notify.views import dashboard, record_user_tablet , add_tablet
urlpatterns = [
    path("login",views.login,name="login"),
    path("logout",views.logout,name="logout"),
    path("register",views.register,name="register"),
    path("dashboard",dashboard,name="dashboard"),
    path('add_tablet',add_tablet, name="addtablet"),
    path('record_tablet', record_user_tablet, name="recordtablet")

]