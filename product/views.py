def fetch_home_listings(state="FL", city=None, limit=100, offset=0):
    """
    Fetches real estate listings from the Realty-in-US API.
    Defaults to fetching properties in Florida with up to 100 results.
    """
    url = f"https://{REALTY_IN_US_API_HOST}/properties/list-for-sale"
    querystring = {
        "state_code": state,
        "offset": str(offset),
        "limit": str(limit),
        "sort": "relevance"
    }

    # Add city to the query if specified
    if city:
        querystring["city"] = city

    headers = {
        "X-RapidAPI-Key": REALTY_IN_US_API_KEY,
        "X-RapidAPI-Host": REALTY_IN_US_API_HOST
    }

    response = requests.get(url, headers=headers, params=querystring)
    if response.status_code == 200:
        return response.json().get('listings', [])
    else:
        return []


def house_listings(request):
    """
    Displays house listings fetched from the Realty-in-US API.
    Fetches all properties in Florida by default.
    """
    # Pull data for all of Florida, limit to 100 homes
    properties = fetch_home_listings(state="FL", limit=100)

    return render(request, 'product_list.html', {'properties': properties})
