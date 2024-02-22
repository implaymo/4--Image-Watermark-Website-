from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path("", views.front_page, name="front_page"),
    path("register", views.register, name="register"),
    path("sign_in", views.sign_in, name="sign_in"),
    path("logout", views.logout_user, name="logout_user"),
]