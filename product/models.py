from django.db import models

# Determines the upload path for product images
def product_image_path(instance, filename):
    return f'products/{instance.id}/{filename}'

class Product(models.Model):
    # Basic product information
    title = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to=product_image_path, null=True, blank=True)
    
    # Location-related fields
    city = models.CharField(max_length=100, blank=True, null=True)
    zip_code = models.CharField(max_length=10, blank=True, null=True)
    address = models.CharField(max_length=200, blank=True, null=True)
    
    # Additional property details
    num_bedrooms = models.PositiveIntegerField(blank=True, null=True)
    square_feet = models.PositiveIntegerField(blank=True, null=True)
    num_floors = models.PositiveIntegerField(blank=True, null=True)

    # String representation of the product
    def __str__(self):
        return self.title