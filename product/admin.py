from django.contrib import admin
from .models import Product

# Creating a custom admin class for the Product model
class ProductAdmin(admin.ModelAdmin):
    # Specifying the fields to display in the list view of the admin panel
    list_display = ('title', 'price')  # Displays the title and price fields in the admin list view

    # Adding a search bar to the admin panel for searching by the title field
    search_fields = ('title',)  # Enables searching products by their title

# Registering the Product model with the custom admin class
# This allows the Product model to appear in the Django admin interface
admin.site.register(Product, ProductAdmin)