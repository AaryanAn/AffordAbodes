#import
from django.db import models

#storage of the product images in a directory
def product_image_path(instance, filename):
    return f'products/{instance.id}/{filename}'

#defines the product class (in our case housing)
class Product(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to=product_image_path, null=True, blank=True)
    
    city = models.CharField(max_length=100, blank=True, null=True)
    zip_code = models.CharField(max_length=10, blank=True, null=True)
    address = models.CharField(max_length=200, blank=True, null=True)
    num_bedrooms = models.PositiveIntegerField(blank=True, null=True)
    square_feet = models.PositiveIntegerField(blank=True, null=True)
    num_floors = models.PositiveIntegerField(blank=True, null=True)

    #this will represent product object as a string
    def __str__(self):
        return self.title

