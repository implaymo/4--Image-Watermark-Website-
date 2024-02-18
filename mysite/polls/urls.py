from django.urls import path
from .views import front_page
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path('front_page/', front_page, name='front_page'),
]
