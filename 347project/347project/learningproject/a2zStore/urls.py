from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="store"),
    path("products/<int:myid>", views.product, name="Product"),
    path("checkout/", views.checkout, name="Checkout"),
    path("tracker/", views.tracker, name="Tracker"),
]