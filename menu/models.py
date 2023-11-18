from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(max_length=1000, blank=True, null=True)
    
    def __str__(self):
        return self.name
    
        
class MenuItem(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=1000, blank=True, null=True)
    categories = models.ManyToManyField(Category)
    price_small = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    price_medium = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    price_large = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    
    def __str__(self):
        return self.name
    