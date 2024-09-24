import logging
from rest_framework import serializers
from products.serializers import ProductInCartSerializer
from products.models import Product
from .models import Cart, CartItem


logger = logging.getLogger(__name__)


class ProductInCartField(serializers.PrimaryKeyRelatedField):
    def to_representation(self, value):
        pk = super().to_representation(value)
        try:
            product = Product.objects.get(id=pk)
            serializer = ProductInCartSerializer(product)
            return serializer.data
        except Product.DoesNotExist:
            return None


class CartItemSerializer(serializers.ModelSerializer):
    product = ProductInCartField(queryset=Product.objects.all())

    class Meta:
        model = CartItem
        fields = ["id", "product", "quantity", "total_price"]
        read_only_fields = ["id", "total_price"]

    def create(self, validated_data):
        validated_data['cart'] = self.context['cart']
        return super().create(validated_data)


class CartItemQuantitySerializer(serializers.Serializer):
    quantity = serializers.IntegerField(min_value=1)

    def update(self, instance, validated_data):
        instance.quantity = validated_data['quantity']
        instance.save()
        return instance


class CartSerializer(serializers.ModelSerializer):
    items = CartItemSerializer(many=True)

    class Meta:
        model = Cart
        fields = ["id", "total_price", "items"]
