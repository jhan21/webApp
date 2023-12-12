#!/usr/bin/env python3
import requests
import logging
from flask import Flask, render_template, request, session

app = Flask(__name__)
persistent_variable = 0

'''
Helper function to get temperature
using API
'''


def get_temperature(api_key="53632e174b0242b7939183825230912", city="Boulder"):
    url = f"http://api.weatherapi.com/v1/current.json?key={api_key}&q={city}"
    response = requests.get(url)
    print(response.text)
    print(response.json()["current"]["temp_c"])
    print(response.json()["current"]["condition"])
    return response.json()["current"]["temp_c"]

def calculate_temperature_difference(city1_temperature, city2_temperature):
    return abs(city1_temperature - city2_temperature)

def get_weather_info(api_key="53632e174b0242b7939183825230912", city="Boulder"):
    url = f"http://api.weatherapi.com/v1/current.json?key={api_key}&q={city}"
    response = requests.get(url)
    print(response.text)
    #print(response.json()["current"]["temp_c"])
    print(response.json()["current"]["condition"])
    return response.json()["current"]["condition"]

'''
In main we first get the current temperature and then 
create a new object that we can add to the database. 
'''
if __name__ == "__main__":
    current_temperature = get_temperature()
    current_city = "Boulder"


@app.route("/")
def main():
    return render_template("index.html", message="")

@app.route("/echo_user_input", methods=["POST"])
def echo_input():
    global persistent_variable
    cities = [request.form.get("city1", ""), request.form.get("city2", "")]
    api_key = "53632e174b0242b7939183825230912"  # Replace with your actual API key
    temperatures = []
    weather_info = {}

    for city in cities:
        current_temperature = get_temperature(api_key, city)

        temperatures.append((city, current_temperature))
        persistent_variable = persistent_variable + 1
        weather_info[city] = get_weather_info(api_key, city)
        print(weather_info[city]['code'])
        weather_info[city]['code'] = str(current_temperature) + " C"
    # Calculate temperature difference if both cities are provided
    temperature_difference = None
    if len(temperatures) == 2:
        temperature_difference = calculate_temperature_difference(temperatures[0][1], temperatures[1][1])


    return render_template("index.html", temperatures=temperatures, temperature_difference=temperature_difference, weather_info=weather_info)