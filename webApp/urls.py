from django.urls import path, include
from django.contrib import admin
from webApp import views as v


urlpatterns = [
    path("", v.home, name="home"),
    path("layout.html", v.home, name="home"),
    path("register/", v.register, name="register"),
    
    path("login/", v.loginrequest, name="login"),
    path("logout/", v.logoutRequest, name="logout"),
    
    path("profile/", v.profile, name="profile"),

    path('', include("django.contrib.auth.urls")),
    path("register/", v.register, name="register"),
    path("editProfile/", v.editProfile, name="editProfile"),
]
