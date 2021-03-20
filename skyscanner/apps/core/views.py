from django.shortcuts import render, redirect
from .forms import SearchForm
import requests
import json


def frontpage(request):
    currencies = ['AED', 'AFN', 'ALL', 'AMD', 'ANG', 'AOA', 'ARS', 'AUD', 'AWG', 'AZN', 'BAM', 'BBD', 'BDT', 'BGN', 'BHD', 'BIF', 'BMD', 'BND', 'BOB', 'BRL', 'BSD', 'BTN', 'BWP', 'BYN', 'BZD', 'CAD', 'CDF', 'CHF', 'CLP', 'CNY', 'COP', 'CRC', 'CUC', 'CUP', 'CVE', 'CZK', 'DJF', 'DKK', 'DOP', 'DZD', 'EGP', 'ERN', 'ETB', 'EUR', 'FJD', 'GBP', 'GEL', 'GHS', 'GIP', 'GMD', 'GNF', 'GTQ', 'GYD', 'HKD', 'HNL', 'HRK', 'HTG', 'HUF', 'IDR', 'ILS', 'INR', 'IQD', 'IRR', 'ISK', 'JMD', 'JOD', 'JPY', 'KES', 'KGS', 'KHR', 'KMF', 'KPW', 'KRW', 'KWD', 'KYD', 'KZT', 'LAK', 'LBP', 'LKR', 'LRD', 'LSL', 'LYD', 'MAD', 'MDL', 'MGA', 'MKD', 'MMK', 'MNT', 'MOP', 'MRO', 'MUR', 'MVR', 'MWK', 'MXN', 'MYR', 'MZN', 'NAD', 'NGN', 'NIO', 'NOK', 'NPR', 'NZD', 'OMR', 'PAB', 'PEN', 'PGK', 'PHP', 'PKR', 'PLN', 'PYG', 'QAR', 'RON', 'RSD', 'RUB', 'RWF', 'SAR', 'SBD', 'SCR', 'SDG', 'SEK', 'SGD', 'SHP', 'SLL', 'SOS', 'SRD', 'STD', 'SYP', 'SZL', 'THB', 'TJS', 'TMT', 'TND', 'TOP', 'TRY', 'TTD', 'TWD', 'TZS', 'UAH', 'UGX', 'USD', 'UYU', 'UZS', 'VND', 'VUV', 'WST', 'XAF', 'XCD', 'XOF', 'XPF', 'YER', 'ZAR', 'ZMW']
    flights = []
    # Checks if the form as been submitted
    if request.method == 'POST':
        form = SearchForm(request.POST)
        # Checks that all of the required fields are filled in
        if form.is_valid():
            # Assigns variables to all of the fields
            departure = form.cleaned_data['departure']
            destination = form.cleaned_data['destination']
            departure_date = form.cleaned_data['departure_date']
            return_date = form.cleaned_data['arrival_date']
            currency = form.cleaned_data['currency']
            # Prevents app from crashing if a query doesn't work (ex: date is in the wrong format)
            try:
                # Checks if the PlaceId was used
                if "-sky" in departure and "-sky" in destination:

                    # Calls on the API
                    url = f"https://skyscanner-skyscanner-flight-search-v1.p.rapidapi.com/apiservices/browsequotes/v1.0/US/{currency}/en-US/{departure}/{destination}/{departure_date}"

                    querystring = {"inboundpartialdate":f"{return_date}"}

                    headers = {
                        'x-rapidapi-key': {Insert your key here},
                        'x-rapidapi-host': "skyscanner-skyscanner-flight-search-v1.p.rapidapi.com"
                                }

                    response = requests.request("GET", url, headers=headers, params=querystring)
                    json_data = response.json() if response and response.status_code == 200 else None

                    # Initializes lists
                    prices = []
                    price = []
                    carrier = []
                    depart = []
                    arrive = []

                    # Checks that the request returned data
                    if json_data:

                        # Loop through each entry
                        for i in range(len(json_data['Quotes'])):

                            # Format the symbols based on the given information
                            sym = json_data['Currencies'][0]['Symbol']
                            p = str(json_data['Quotes'][i]['MinPrice'])
                            if json_data['Currencies'][0]['SymbolOnLeft']:
                                if json_data['Currencies'][0]['SpaceBetweenAmountAndSymbol']:
                                    p = sym + ' ' + p
                                else:
                                    p = sym + p
                            else:
                                if json_data['Currencies'][0]['SpaceBetweenAmountAndSymbol']:
                                    p = p + ' ' + sym
                                else:
                                    p = p + sym

                            # Add information from the flight to the list
                            current_price = []
                            current_price.append(p)
                            price.append(p)
                            current_price.append("")
                            prices.append(current_price)
                            currentFlight = json_data['Quotes'][i]['OutboundLeg']
                            originId = currentFlight['OriginId']
                            destinationId = currentFlight['DestinationId']
                            carrierId = currentFlight['CarrierIds'][0]

                            # Use the given ids to return and append the name of the airports
                            for place in json_data['Places']:
                                if place['PlaceId'] == originId:
                                    depart.append(place['Name'])
                                elif place['PlaceId'] == destinationId:
                                    arrive.append(place['Name'])

                            # Use the given id to return and append the name of carriers
                            for carr in json_data['Carriers']:
                                if carr['CarrierId'] == carrierId:
                                    carrier.append(carr['Name'])


                else:

                    # Get results from the departure search
                    url = f"https://skyscanner-skyscanner-flight-search-v1.p.rapidapi.com/apiservices/autosuggest/v1.0/US/{currency}/en-US/"

                    querystring = {"query":f"{departure}"}

                    headers = {
                    'x-rapidapi-key': {Insert your key here},
                    'x-rapidapi-host': "skyscanner-skyscanner-flight-search-v1.p.rapidapi.com"
                    }

                    response = requests.request("GET", url, headers=headers, params=querystring)
                    json_data = response.json() if response and response.status_code == 200 else None

                    # Create a list and dictionary of the possible departure airports from the query
                    depPlaceIds = []
                    depPlaceDicts = {}
                    departurePlaces = json_data["Places"]
                    for dep in departurePlaces:
                        if dep['PlaceId'] not in depPlaceIds:
                            depPlaceIds.append(dep['PlaceId'])
                            depPlaceDicts[dep['PlaceId']] = dep

                    # Get results from the destination search
                    url = f"https://skyscanner-skyscanner-flight-search-v1.p.rapidapi.com/apiservices/autosuggest/v1.0/US/{currency}/en-US/"

                    querystring = {"query":f"{destination}"}

                    headers = {
                    'x-rapidapi-key': {Insert your key here},
                    'x-rapidapi-host': "skyscanner-skyscanner-flight-search-v1.p.rapidapi.com"
                    }

                    response = requests.request("GET", url, headers=headers, params=querystring)
                    json_data = response.json() if response and response.status_code == 200 else None

                    # Create a list and dictionary of the possible destination airports from the query
                    destPlaceIds = []
                    destPlaceDicts = {}
                    destinationPlaces = json_data["Places"]
                    for dest in destinationPlaces:
                        if dest['PlaceId'] not in destPlaceIds:
                            destPlaceIds.append(dest['PlaceId'])
                            destPlaceDicts[dest['PlaceId']] = dest

                    # Initialize lists
                    prices = []
                    price = []
                    carrier = []
                    depart = []
                    arrive = []

                    # Submit requests to API
                    for departure in depPlaceIds:
                        for destination in destPlaceIds:

                            url = f"https://skyscanner-skyscanner-flight-search-v1.p.rapidapi.com/apiservices/browsequotes/v1.0/US/{currency}/en-US/{departure}/{destination}/{departure_date}"

                            querystring = {"inboundpartialdate":f"{return_date}"}

                            headers = {
                                'x-rapidapi-key': {Insert your key here},
                                'x-rapidapi-host': "skyscanner-skyscanner-flight-search-v1.p.rapidapi.com"
                                        }

                            response = requests.request("GET", url, headers=headers, params=querystring)
                            json_data = response.json() if response and response.status_code == 200 else None

                            # Check that data is returned
                            if json_data:

                                # Loop through the flights
                                for i in range(len(json_data['Quotes'])):

                                    # Format the prices from the given information
                                    sym = json_data['Currencies'][0]['Symbol']
                                    p = str(json_data['Quotes'][i]['MinPrice'])
                                    if json_data['Currencies'][0]['SymbolOnLeft']:
                                        if json_data['Currencies'][0]['SpaceBetweenAmountAndSymbol']:
                                            p = sym + ' ' + p
                                        else:
                                            p = sym + p
                                    else:
                                        if json_data['Currencies'][0]['SpaceBetweenAmountAndSymbol']:
                                            p = p + ' ' + sym
                                        else:
                                            p = p + sym

                                    # Add information about the flights to the lists
                                    current_price = []
                                    current_price.append(p)
                                    price.append(json_data['Quotes'][i]['MinPrice'])
                                    current_price.append("")
                                    prices.append(current_price)
                                    currentFlight = json_data['Quotes'][i]['OutboundLeg']
                                    originId = currentFlight['OriginId']
                                    destinationId = currentFlight['DestinationId']
                                    carrierId = currentFlight['CarrierIds'][0]

                                    # Find and append the name of the airport based on the id
                                    for place in json_data['Places']:
                                        if place['PlaceId'] == originId:
                                            depart.append(place['Name'])
                                        elif place['PlaceId'] == destinationId:
                                            arrive.append(place['Name'])

                                    # Find and append the name of the carrier based on the id
                                    for carr in json_data['Carriers']:
                                        if carr['CarrierId'] == carrierId:
                                            carrier.append(carr['Name'])

                # Check that the flights exist
                if len(prices) == 0:
                    message = "No flights were found"
                else:
                    message = ""
                    # Find the minimum price
                    minimum_price = min(price)
                    for i in range(len(prices)):
                        if price[i] == minimum_price:
                            prices[i][1] = "min"
                        else:
                            prices[i][1] = ""

                # Zip the lists together
                flights = zip(prices, carrier, depart, arrive)

                context = {'flights': flights, 'currencies': currencies, 'curren': currency, 'message': message}
                return render(request, 'core/frontpage.html', context)
            except:
                return render(request, 'core/frontpage.html', {'currencies': currencies})
        else:
            message = "Please confirm that all the required fields have been filled out correctly"
            return render(request, 'core/frontpage.html', {'currencies': currencies, 'message': message})
    else:
        return render(request, 'core/frontpage.html', {'currencies': currencies})

