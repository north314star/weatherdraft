print("Enter 'q' any time to quit")

city_name= input('Enter a city name you want to look at:')
zipcode= input('Enter a city name you want to look at:')
import requests
import math


w = city_name
s = zipcode
u = ('us')
api_key ='dd29fda4360eb6271e53bbe6a6e445ce'

def get_weather(api_key, city):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={w}&appid={api_key}"

    response = requests.get(url).json()

    temp = response ['main']['temp']
    temp = math.floor((temp * 1.8)- 459.67)
    print(temp)

get_weather(api_key, zipcode)

def get_weather(api_key, zip):
    url = f"http://api.openweathermap.org/data/2.5/weather?zip={s},{u}&appid={api_key}"

    r = requests.get(url).json()

    temp = response ['main']['temp']
    temp = math.floor((temp * 1.8)- 459.67)
    print(temp)
    

get_weather(api_key, city_name)

