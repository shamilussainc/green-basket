from django.db import models


class Product(models.Model):
    label = models.CharField(max_length=256, unique=True)
    description = models.TextField(max_length=2048)
    price = models.FloatField()
    weight = models.IntegerField(default=1)
    image = models.ImageField(upload_to='products', blank=True, null=True)

    category = models.ForeignKey(to='Category', on_delete=models.SET_NULL, null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.label


class Category(models.Model):
    label = models.CharField(max_length=256, unique=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.label