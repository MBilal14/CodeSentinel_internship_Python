# Task 5
# Weather Dashboard with API Integration
# Create a Python script that: Asks the user for
# a city nameFetches weather data using the OpenWeatherMap
# API (orsimilar) Displays current temperature, humidity, andconditions
# 🛠 Tools: requests, json, API key handling
# 🎯 Goal: Learn to consume REST APIs and parse JSONdata dynamically.


import requests  # For sending HTTP requests to the weather API


# Function to fetch weather data
def fetch_weather(city, api_key="72ca537713217dc9c78cdd544803749f"):
    """
    Fetches and displays the current weather for a given city
    using the OpenWeatherMap API.
    """

    # Build the API request URL with city, API key, and units in Celsius
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"

    # Send a GET request to the API
    response = requests.get(url)

    # If the request fails (e.g., wrong city name), stop here
    if response.status_code != 200:
        print("Failed to fetch weather data. Please check the city name.")
        return

    # Convert the response to JSON format (Python dictionary)
    data = response.json()

    # Extract useful details from the JSON
    temp = data["main"]["temp"]  # Current temperature in °C
    humidity = data["main"]["humidity"]  # Current humidity in %
    condition = data["weather"][0][
        "description"
    ]  # Weather condition (e.g., "clear sky")

    # Print the results in a nice format
    print(f"\nWeather in {city.capitalize()}:")
    print(f"🌡 Temperature: {temp}°C")
    print(f"💧 Humidity: {humidity}%")
    print(f"☁ Condition: {condition.capitalize()}")


# Main entry point of the program
# Main entry point of the program
if __name__ == "__main__":
    # Ask the user for a city name
    city = input("Please enter the city name: ")

    # Call the function to fetch and display weather info
    fetch_weather(city)
