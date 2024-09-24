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
        read_only_fields = ['id', 'label', 'description', 'price', 'weight', 'image', 'category']


class ProductInCartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'label', 'price', 'image']
        read_only_fields = ['id', 'label', 'price', 'image']
