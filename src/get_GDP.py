import requests

def get_GDP(iso_code):
    url = f"https://api.worldbank.org/v2/country/{iso_code}/indicators/NY.GDP.MKTP.CD"
    params = {
        'format' : 'json'
    }
    data = requests.get(url, params=params).json()
    years = []
    values = []
    for year in data[1]:
        years.append(year['date'])
        values.append(year['value'])
    return years, values
