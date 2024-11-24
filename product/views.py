from django.shortcuts import render
from .models import Product
from .forms import ProductSearchForm
import requests
from EStore.config import REALTY_IN_US_API_KEY, REALTY_IN_US_API_HOST



def fetch_home_listings(postal_code="90004", status=["for_sale"], limit=20, offset=0):
    """
    Fetches real estate listings using the Realty-in-US API's POST /properties/v3/list endpoint.
    Defaults to properties in postal code 90004 with 'for_sale' status.
    """
    url = f"https://{REALTY_IN_US_API_HOST}/properties/v3/list"
    
    payload = {
        "limit": limit,
        "offset": offset,
        "postal_code": postal_code,
        "status": status,
        "sort": {
            "direction": "desc",
            "field": "list_date"
        }
    }

    headers = {
        "Content-Type": "application/json",
        "X-RapidAPI-Key": REALTY_IN_US_API_KEY,
        "X-RapidAPI-Host": REALTY_IN_US_API_HOST,
    }

    try:
        response = requests.post(url, json=payload, headers=headers)
        response.raise_for_status()  # Raise an error for bad status codes
        data = response.json()
        print("API Response Data:", data)  # Debugging
        return data.get('data', {}).get('home_search', {}).get('results', [])
    except requests.exceptions.RequestException as e:
        print(f"API Request failed: {e}")
        return []

def house_listings(request):
    """
    Displays house listings fetched from the Realty-in-US API.
    Defaults to properties in postal code 90004.
    """
    properties = fetch_home_listings(postal_code="90004", limit=20)

    return render(request, 'product_list.html', {'properties': properties})


def product_list(request):
    """
    Displays a list of products based on optional search filters from the database.
    """
    form = ProductSearchForm(request.GET or None)
    products = Product.objects.all()

    if form.is_valid():
        zip_code = form.cleaned_data.get('zip_code')
        city = form.cleaned_data.get('city')
        address = form.cleaned_data.get('address')

        # Apply filters to the query
        if zip_code:
            products = products.filter(zip_code=zip_code)
        if city:
            products = products.filter(city__icontains=city)
        if address:
            products = products.filter(address__icontains=address)

    return render(request, 'product_list.html', {'products': products, 'form': form})


def home(request):
    """
    Home view that renders the homepage.
    """
    return render(request, 'home.html')
