from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("<int:route_id>/", views.detail, name="detail"),
    path("<int:route_id>/book/", views.book, name="book"),
    path("<int:route_id>/unbook/", views.unbook, name="unbook"),
    path("register/", views.register, name="register"),
]