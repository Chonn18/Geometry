from django.db import models
from django.core.validators import MaxValueValidator

# Create your models here.
class Problem(models.Model):
    description = models.TextField(blank=True, null=True)
    solve = models.TextField(blank=True, null=True)
    image = models.TextField(blank=True, null=True)
    file = models.TextField(blank=True, null=True)

# class Product(models.Model) : 
#     title = models.CharField(max_length=100, null=True)
#     price = models.FloatField(null=True)
    
#     # Foreign key
#     rating = models.OneToOneField(Rating, on_delete=models.CASCADE,default=None, blank=True, null=True)
    
#     stock = models.IntegerField(default=0)
#     image = models.TextField(blank=True, null=True)
#     description = models.TextField(blank=True, null=True)
    
#     CATEGORY_CHOICES = (
#         ('male', 'Male'),
#         ('female', 'Female'),
#         ('couple', 'Couple'),
#     )
    
#     category = models.CharField(max_length=6, choices=CATEGORY_CHOICES, default='male')
    
#     date_created = models.DateTimeField(auto_now_add=True)
    
#     image_file_name = models.TextField(blank=True, null=True)
    
#     favorite = models.BooleanField(default=False, null=True)

#     def __str__(self) :
#         return self.title