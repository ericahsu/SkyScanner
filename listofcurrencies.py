import requests
import json

url = "https://skyscanner-skyscanner-flight-search-v1.p.rapidapi.com/apiservices/reference/v1.0/currencies"

headers = {
    'x-rapidapi-key': "97a2b27303msh623b502d78a9b3cp1f86dcjsne6a41b75adb9",
    'x-rapidapi-host': "skyscanner-skyscanner-flight-search-v1.p.rapidapi.com"
    }

response = requests.request("GET", url, headers=headers)
json_data = response.json() if response and response.status_code == 200 else None
data = json_data['Currencies']

# Formats the currencies into tuples to use as choices in Django form
currencies = []
choice = "("
for currency in data:
    choice = choice + '(' + '"' + f"{currency['Code']}" + '"' + ',' + '"' + f"{currency['Code']}" + '"' + '),'
    currencies.append(currency['Code'])

choice = choice + ')'
print(choice)
print(currencies)
