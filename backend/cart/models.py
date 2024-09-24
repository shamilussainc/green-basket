from django.db import models
from django.contrib.auth import get_user_model
from products.models import Product


UserModel = get_user_model()


class Cart(models.Model):
    ACTIVE = "A"
    PENDING = "P"
    COMPLETED = "C"
    STATUS_CHOICES = {
        ACTIVE: "active",
        PENDING: "pending",
        COMPLETED: "completed"
    }

    user = models.ForeignKey(to=UserModel, on_delete=models.CASCADE,)
    status = models.CharField(
        max_length=1,
        choices=STATUS_CHOICES,
        default=ACTIVE
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    @property
    def total_price(self):
        # TODO: code optimization
        price = 0
        for item in self.items.all():
            price += item.total_price

        return price


class CartItem(models.Model):
    cart = models.ForeignKey(to=Cart, related_name='items', on_delete=models.CASCADE)
    product = models.ForeignKey(to=Product, on_delete=models.PROTECT)
    quantity = models.IntegerField(default=1)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    @property
    def total_price(self):
        return self.product.price * self.quantity