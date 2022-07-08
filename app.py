from datetime import datetime
import streamlit as st
import requests
import datetime

'''
# TaxiFareModel Fare Prediction
'''


def get_lonlat(address):
    url = 'https://nominatim.openstreetmap.org/search'
    params = {'q':address, \
            'format':'json'}
    response = requests.get(url,
                        params=params).json()[0]

    return  float(response['lat']), float(response['lon'])


d = st.date_input("Pick-up date:", datetime.date(2019, 7, 6))
t = st.time_input("Pick-up time:", datetime.time(6, 0, 00))

st.metric('Pick-up date and time',f'{d} {t}')

pickup = st.text_input('Pick-up address:', 'Central Park, NYC')
lat1, lon1 = get_lonlat(pickup)
col1, col2, col3 = st.columns(3)
col1.metric("Latitude", lat1)
col2.metric("Longitude", lon1)

dropoff = st.text_input('Drop-off address:', 'Grand Central, NYC')
lat2, lon2 = get_lonlat(dropoff)
col1, col2, col3 = st.columns(3)
col1.metric("Latitude", lat2)
col2.metric("Longitude", lon2)

count=st.slider('Select number of passengers', 1, 10, 2)

params = dict(
  pickup_datetime=f'{d} {t}',
  pickup_longitude=lat1,
  pickup_latitude=lon1,
  dropoff_longitude=lat2,
  dropoff_latitude=lon2,
  passenger_count=count
)

# URL
taxifare_api_url = 'https://taxi-fare-pred-n44uq5j6wa-ew.a.run.app/predict'

# retrieve the response
response = requests.get(taxifare_api_url,params=params).json()

fare=round(response['fare'],2)

st.metric('Predicted Taxi Fare',f"{fare} $")
