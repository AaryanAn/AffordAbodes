# forms.py
from django import forms

# Form class for searching products based on location-related fields
class ProductSearchForm(forms.Form):
    # Optional field for searching by ZIP code
    zip_code = forms.CharField(required=False)  
    
    # Optional field for searching by city
    city = forms.CharField(required=False)  
    
    # Optional field for searching by address
    address = forms.CharField(required=False)  

# General-purpose form for a single search input
class GeneralSearchForm(forms.Form):
    # Optional field for a general search value
    value = forms.CharField(required=False)  

# Form class for filtering products by price range
class PriceRangeFilterForm(forms.Form):
    # Optional field for specifying the minimum price
    # Ensures the value is a decimal and not less than 0
    min_price = forms.DecimalField(min_value=0, required=False, label="Minimum Price")
    
    # Optional field for specifying the maximum price
    # Ensures the value is a decimal and not less than 0
    max_price = forms.DecimalField(min_value=0, required=False, label="Maximum Price")