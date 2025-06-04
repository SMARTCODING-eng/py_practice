import requests
def get_weather():
    api_key = "c481d27ff53a4618ade221833250406"
    location = input("Enter your current location: ")
    url = "https://api.weatherapi.com/v1/current.json"
    params = {
        "key": api_key,
        "q": location,
        "aqi": "no"
    }
    response = requests.get(url,params=params)
    if response.status_code  == 200:
        data = response.json()
        current = data['current']
        location_data = data['location']
        weather_info = {
            "location": f"{location_data['name']}, {location_data['country']}",
            "temperature_c": current['temp_c'],
            "temperature_f": current['temp_f'],
        }
        return weather_info
    else:
        return {"error": f"Unanle to fetch weather data.{response.status_code}"}
    
if __name__ =="__main__":
    weather =get_weather()
    print("location:", weather['location'])
    print("Temperature (C):", weather['temperature_c'])
    print("Temperature (F):", weather['temperature_f'])
    
    