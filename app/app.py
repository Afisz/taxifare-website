import requests
import streamlit as st

'''
# TaxiFareModel front
'''

pickup_date = st.date_input('Pick-up Date')
pickup_time = st.time_input('Pick-up Time')
pickup_datetime = f'{str(pickup_date)} {str(pickup_time)}'
pickup_longitude = st.number_input('Pick Up Longitude', value=-73.989)
pickup_latitude = st.number_input('Pick Up Latitude', value=40.747)
dropoff_longitude = st.number_input('Drop Off Longitude', value=-73.956)
dropoff_latitude = st.number_input('Drop Off Latitude', value=40.802)
passenger_count = st.number_input('Passenger Count', min_value=1, value='min', step=1)

'''
## Your Fare:
'''

url = 'https://taxifare-155214835333.europe-west1.run.app/predict'

if url == 'https://taxifare.lewagon.ai/predict':

    st.markdown('Maybe you want to use your own API for the prediction, not the one provided by Le Wagon...')

data = {
        "pickup_latitude": pickup_latitude,
        "pickup_longitude": pickup_longitude,
        "dropoff_latitude": dropoff_latitude,
        "dropoff_longitude": dropoff_longitude,
        "passenger_count": passenger_count,
        "pickup_datetime": pickup_datetime
      }

response = requests.get(url=url, params=data)

st.write(response.json()["fare"])
