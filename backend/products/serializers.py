from rest_framework import serializers
from .models import Product, Category


class CategoryBaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'label']


class ProductSerializer(serializers.ModelSerializer):
    category = CategoryBaseSerializer(read_only=True)

    class Meta:
        model = Product
        fields = ['id', 'label', 'description', 'price', 'weight', 'image', 'category']
