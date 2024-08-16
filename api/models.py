from django.contrib.auth.models import AbstractUser
from django.core.validators import MinValueValidator
from django.db import models


class ApiUser(AbstractUser):
    ROLE_CHOICES = [
        ('seller', 'Продавец'),
        ('buyer', 'Покупатель'),
    ]
    group = models.CharField(max_length=10, choices=ROLE_CHOICES, default='buyer')

    def __str__(self):
        return self.username

class Warehouse(models.Model):
    name = models.CharField(max_length=128)
    def __str__(self):
        return f"{self.id}: {self.name}"

class Product(models.Model):
    name = models.CharField(max_length=255, default='Default Name')
    warehouse = models.ForeignKey(Warehouse, related_name="products", on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(validators=[MinValueValidator(1)])
    def __str__(self):
        return f"{self.name}. Warehouse: {self.warehouse.name}. Quantity: {self.quantity}"


class Shipment(models.Model):
    warehouse = models.ForeignKey(Warehouse, related_name="shipments", on_delete=models.CASCADE)
    product = models.ForeignKey(Product, related_name='shipments', on_delete=models.CASCADE)
    #client = models.ForeignKey(get_user_model(), related_name='shipments', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.warehouse.name}; {self.product.name}; {self.product.quantity}"
