from django.urls import path
from .views import index, shop

urlpatterns = [
    path("", view=index, name="index"),
    path("shop", view=shop, name="shop"),
]