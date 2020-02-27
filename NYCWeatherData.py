
import requests
from datetime import date
import pandas as pd
import io
import json

def get_noaa_data(url, params, header):

    r = requests.get(url, params, headers=header).text
    rawData = pd.read_csv(io.StringIO(r))
    return rawData

def get_forecast_data(url):
    r = requests.get(url)
    json1_data = json.loads(r.text)
    df = pd.DataFrame(json1_data['properties']['periods'])
    print(r.text)
    return df


if __name__ == '__main__':

    today = date.today()

    # Historical NYC's weather data from NCEI Data Service API
    token = 'YourToken'
    creds = dict(token=token)
    params = {'dataset': 'daily-summaries', 'stations': 'USW00014732','startDate': '2018-01-01',\
         'endDate': str(today),  'dataTypes': ['AWND', 'PRCP', 'SNOW', 'TAVG', 'WT01'], 'units': 'standard'}
    url = 'https://www.ncei.noaa.gov/access/services/data/v1'

    urlData = get_noaa_data(url, params, creds)
    urlData.to_csv('weatherData.csv', index=False)

    # Forecast NYC's weather data from National Weather Service API
    forecast_url = 'https://api.weather.gov/gridpoints/OKX/41,74/forecast?units=us'
    forecast_data = get_forecast_data(forecast_url)

    forecast_data.to_csv('forecast.csv', index=False)


