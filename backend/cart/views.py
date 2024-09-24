import logging
from django.shortcuts import render
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import NotFound, PermissionDenied
from .models import Cart, CartItem
from .serializers import CartSerializer, CartItemSerializer, CartItemQuantitySerializer


logger = logging.getLogger(__name__)


class GetMyCartView(APIView):
    """
    Get cart details for the authenticated user.
    """
    permission_classes = [IsAuthenticated,]

    def get(self, request):
        cart, is_created = Cart.objects.get_or_create(user=request.user, status=Cart.ACTIVE)
        if is_created:
            logger.info(f"New cart created for user_id: {request.user.id}")
        serializer = CartSerializer(cart)
        return Response(serializer.data, status=status.HTTP_200_OK)


class AddCartItemView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        cart, is_created = Cart.objects.get_or_create(user=request.user, status=Cart.ACTIVE)
        if is_created:
            logger.info(f"New cart created for user_id: {request.user.id}")
        
        serializer = CartItemSerializer(data=request.data, context={'cart': cart})
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


# patch /my-cart/items/<item_id>
class UpdateOrDeleteCartItemView(APIView):
    permission_classes = [IsAuthenticated]

    def get_object(self, pk):
        try:
            return CartItem.objects.get(id=pk, cart__user=self.request.user)
        except CartItem.DoesNotExist:
            raise NotFound(detail="Cart item not found.")


    def patch(self, request, pk):
        cart_item = self.get_object(pk=pk)        
        serializer = CartItemQuantitySerializer(cart_item, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(data=serializer.data, status=status.HTTP_200_OK)
    
    def delete(self, request, pk):
        cart_item = self.get_object(pk=pk)
        cart_item.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
