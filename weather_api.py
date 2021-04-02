
def get_weather_data():
    import requests
    import os
    from datetime import datetime

    user_api = "06b6bf71901352efa72886ce58cc1412"
    #"0c42f7f6b53b244c78a418f4f181282a"
    location = "Delhi"#input("Enter the city name: ")
    #https://api.openweathermap.org/data/2.5/weather?q=Delhi&appid=06b6bf71901352efa72886ce58cc1412
    complete_api_link = "https://api.openweathermap.org/data/2.5/weather?q="+location+"&appid="+user_api
    api_link = requests.get(complete_api_link)
    api_data = api_link.json()

    # print(api_data)
    #create variables to store and display data
    temp_city = (api_data['main']['temp'])
    minm_temp = (api_data['main']['temp_min'])
    maxm_temp = (api_data['main']['temp_max'])
    pressure = (api_data['main']['pressure'])
    feels_like = (api_data['main']['feels_like'])
    weather_desc = api_data['weather'][0]['description']
    humidity = api_data['main']['humidity']
    wind_spd = api_data['wind']['speed']
    date_time = datetime.now().strftime("%d %b %Y | %I:%M:%S %p")

    print ("-------------------------------------------------------------")
    print ("Weather Stats for - {}  || {}".format(location.upper(), date_time))
    print ("-------------------------------------------------------------")
    print("minm_temp:  ", minm_temp)
    print("maxm_temp: ", maxm_temp)
    print("pressure: ", pressure)
    print("humidity: ", humidity)
    print("feels_like: ", feels_like)
    print("weather_desc: ", weather_desc)
    print("wind_spd: ", wind_spd)
    return (minm_temp, maxm_temp, pressure, humidity, weather_desc, wind_spd)


# get_weather_data()