import streamlit as st
import requests

'''
# TaxiFareModel front
'''

st.markdown('''
Remember that there are several ways to output content into your web page...

Either as with the title by just creating a string (or an f-string). Or as with this paragraph using the `st.` functions
''')

'''
## Here we would like to add some controllers in order to ask the user to select the parameters of the ride

1. Let's ask for:
- date and time
- pickup longitude
- pickup latitude
- dropoff longitude
- dropoff latitude
- passenger count
'''

params = dict(
  pickup_datetime='2012-10-06 12:10:20',
  pickup_longitude=40.7614327,
  pickup_latitude=-73.9798156,
  dropoff_longitude=40.6331166,
  dropoff_latitude=-73.8874078,
  passenger_count=2
)

# URL
taxifare_api_url = 'https://taxi-fare-pred-n44uq5j6wa-ew.a.run.app/predict'

# retrieve the response
response = requests.get(taxifare_api_url,params=params)

response.status_code, response.json().get("fare", "no prediction")


'''

2. Let's build a dictionary containing the parameters for our API...

3. Let's call our API using the `requests` package...

4. Let's retrieve the prediction from the **JSON** returned by the API...

## Finally, we can display the prediction to the user
'''
