from django.urls import path
from . import views

urlpatterns = [
    path("", views.home2, name="home"),
    path("members/", views.home4, name="members-list"),
    path("add/", views.home5, name="add-member"),
]