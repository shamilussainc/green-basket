from django.shortcuts import render
from .models import Product
from .serializers import ProductSerializer
from rest_framework.viewsets import ReadOnlyModelViewSet

class ProductViewSet(ReadOnlyModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

