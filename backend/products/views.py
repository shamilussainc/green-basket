from django.core.paginator import Paginator
from rest_framework import status, exceptions
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView

from common.pagination import CustomPageNumberPagination
from .models import Product
from .serializers import ProductSerializer


class ProductList(APIView):
    """
    List all products.
    """
    pagination_class = CustomPageNumberPagination

    def get(self, request: Request):
        sort_by = self.request.query_params.get("sort_by")
        if sort_by in {"label", "-label", "price", "-price"}:
            queryset = Product.objects.all().order_by(sort_by)
        else:
            queryset = Product.objects.all().order_by("id")

        # paginate
        paginator = self.pagination_class()
        paginated_queryset = paginator.paginate_queryset(queryset=queryset, request=request)

        serializer = ProductSerializer(paginated_queryset, many=True)

        return paginator.get_paginated_response(serializer.data)


class ProductDetail(APIView):
    """
    Get Product details.
    """
    def get(self, request: Request, pk: int):
        try:
            queryset = Product.objects.get(pk=pk)
        except Product.DoesNotExist:
            raise exceptions.NotFound(detail="product not found.")
        serializer = ProductSerializer(queryset)
        return Response(data=serializer.data, status=status.HTTP_200_OK)


