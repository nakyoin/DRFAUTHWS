from django.db import models
from rest_framework import serializers
from django.contrib.auth.models import User

class Product(models.Model):
    name = models.CharField(max_length=100, default='Безымянный')
    description = models.TextField(max_length=255, default='Без описания')
    price = models.DecimalField(max_digits=100, decimal_places=1)

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'

    def __str__(self):
        return str(self.name)

class Cart(models.Model):
    cartprod = models.ManyToManyField(Product, related_name='prod')
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Корзина'
        verbose_name_plural = 'Корзина'

    def __str__(self):
        return str(self.user)

class Order(models.Model):
    cartprod = models.ManyToManyField(Product, related_name='produc')
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    totalprice = models.DecimalField(max_digits=100, decimal_places=1)

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'

    def __str__(self):
        return str(self.user)