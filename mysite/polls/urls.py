from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path("", views.front_page, name="front_page"),
    path("register", views.register, name="register"),
    path("sign_in", views.signin, name="signin"),
    path("logout", auth_views.LogoutView.as_view(), name="logout"),
]