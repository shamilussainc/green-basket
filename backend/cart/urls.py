from django.urls import path
from .views import GetMyCartView, AddCartItemView, UpdateOrDeleteCartItemView


urlpatterns = [
    path('my-cart/', GetMyCartView.as_view(), name='my-cart'),
    path('my-cart/items', AddCartItemView.as_view(), name='my-cart-items'),
    path('my-cart/items/<int:pk>', UpdateOrDeleteCartItemView.as_view(), name='cart-item'),
]
