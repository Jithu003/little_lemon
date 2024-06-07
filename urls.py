from .views import homeView, BookingView, MenuView, MenuItem
from django.urls import path



urlpatterns = [
    path("home/", homeView, name="home"),
    path("book/", BookingView.as_view(), name="book"),
    path("menu/", MenuView.as_view(), name="menu"),
    path("menu/<int:pk>", MenuItem.as_view(), name="menuItem")
]