
import requests
import os
from datetime import datetime

user_api = "bf595a2cb1854d988a1f9d26834cd4e2"
complete_api_link = "https://pankaj.cognitiveservices.azure.com/customvision/v3.0/Prediction/c22b7174-dd80-457b-829e-4d05496aee33/classify/iterations/Iteration2/url"
api_link = requests.get(complete_api_link)
api_data = api_link.json()

print(api_data)
#create variables to store and display data
temp_city = ((api_data['main']['temp']) - 273.15)
weather_desc = api_data['weather'][0]['description']
hmdt = api_data['main']['humidity']
wind_spd = api_data['wind']['speed']
date_time = datetime.now().strftime("%d %b %Y | %I:%M:%S %p")

print ("-------------------------------------------------------------")
print ("Weather Stats for - {}  || {}".format(location.upper(), date_time))
print ("-------------------------------------------------------------")

print ("Current temperature is: {:.2f} deg C".format(temp_city))
print ("Current weather desc  :",weather_desc)
print ("Current Humidity      :",hmdt, '%')
print ("Current wind speed    :",wind_spd ,'kmph')
