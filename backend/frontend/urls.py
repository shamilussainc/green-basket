from django.urls import path
from .views import index, shop, product_details

urlpatterns = [
    path("", view=index, name="index-page"),
    path("shop", view=shop, name="shop-page"),
    path("shop/products/<int:id>", view=product_details, name="product-page")
]