#imports
from django import forms

#defines the class for searching for housing based on certain attributes (like zipcode, city, and address)
class ProductSearchForm(forms.Form):
    zip_code = forms.CharField(required=False)
    city = forms.CharField(required=False)
    address = forms.CharField(required=False)

#generic form for searching
class GeneralSearchForm(forms.Form):
    value = forms.CharField(required=False)

#this is for filtering products (another future implementation)
class PriceRangeFilterForm(forms.Form):
    min_price = forms.DecimalField(min_value=0, required=False, label="Minimum Price")
    max_price = forms.DecimalField(min_value=0, required=False, label="Maximum Price")