from django.conf import settings
from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone
import uuid

# Create your models here.
class Product(models.Model):
    uuid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    brand_name = models.CharField(max_length=100)
    product_name = models.CharField(max_length=100)
    material_type = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    is_available = models.BooleanField(default=True)
    with_collector = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.brand_name} {self.product_name}"
    
class UserProduct(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
  

    def __str__(self):
        return f"{self.user.username} - {self.product.product_name}"
    
class Collector(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # Add any additional fields for collectors if needed