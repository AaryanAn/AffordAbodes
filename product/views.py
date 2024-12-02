from django.shortcuts import render
from .models import Product
from .forms import ProductSearchForm
import requests
from EStore.config import REALTY_IN_US_API_KEY, REALTY_IN_US_API_HOST


# Fetches real estate listings using the Realty-in-US API
def fetch_home_listings(postal_code="90004", status=["for_sale"], limit=20, offset=0):
    url = f"https://{REALTY_IN_US_API_HOST}/properties/v3/list"
    payload = {
        "limit": limit,
        "offset": offset,
        "postal_code": postal_code,
        "status": status,
        "sort": {"direction": "desc", "field": "list_date"},
    }
    headers = {
        "Content-Type": "application/json",
        "X-RapidAPI-Key": REALTY_IN_US_API_KEY,
        "X-RapidAPI-Host": REALTY_IN_US_API_HOST,
    }
    try:
        response = requests.post(url, json=payload, headers=headers)
        response.raise_for_status()
        data = response.json()
        print("API Response Data:", data)  # Debugging output
        return data.get('data', {}).get('home_search', {}).get('results', [])
    except requests.exceptions.RequestException as e:
        print(f"API Request failed: {e}")
        return []

# View to display house listings from the API
def house_listings(request):
    properties = fetch_home_listings(postal_code="90004", limit=20)
    return render(request, 'product_list.html', {'properties': properties})

# View to display products with optional search filters
def product_list(request):
    form = ProductSearchForm(request.GET or None)
    products = Product.objects.all()

    if form.is_valid():
        zip_code = form.cleaned_data.get('zip_code')
        city = form.cleaned_data.get('city')
        address = form.cleaned_data.get('address')

        # Apply filters based on form inputs
        if zip_code:
            products = products.filter(zip_code=zip_code)
        if city:
            products = products.filter(city__icontains=city)
        if address:
            products = products.filter(address__icontains=address)

    return render(request, 'product_list.html', {'products': products, 'form': form})

# View to render the homepage
def home(request):
    return render(request, 'home.html')