import requests
import numpy as np
import pandas as pd

def get_GDP(iso_code):
    if pd.isna(iso_code) or isinstance(iso_code,str) == False or iso_code == 'nan':
        return np.nan, np.nan
    else:
        url = f"https://api.worldbank.org/v2/country/{iso_code}/indicators/NY.GDP.MKTP.CD"
        params = {
            'format' : 'json'
        }
        data = requests.get(url, params=params)
        if data.status_code == 200:
            years = []
            values = []
            print()
            if len(data.json()) == 1:
                return np.nan, np.nan
            
            if data.json()[0]['total'] > 0:
                for year in data.json()[1]:
                    years.append(year['date'])
                    values.append(year['value'])
                return years, values
            else:
                return np.nan, np.nan    
        else:
            return np.nan, np.nan

print(get_GDP('BES'))