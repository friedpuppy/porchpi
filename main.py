#!/usr/bin/env python3

import requests  # Handles HTTP requests
import time      # Handles time-related tasks
import os        # Handles operating system interactions

# Define the emonCMS API URL
url = "http://192.168.1.74/input/get.json?node=emonth7&apikey=864b0ed9cd360083b6002576ecc43948"

def clear_screen():
    """Clears the console screen."""
    # For Windows
    if os.name == 'nt':
        _ = os.system('cls')
    # For macOS and Linux
    else:
        _ = os.system('clear')

while True:
    try:
        clear_screen()
        # Send GET request to the API
        response = requests.get(url)
        response.raise_for_status()  # Raise an exception for bad status codes

        # Convert the response to JSON format
        data = response.json()

        # Extract the temperature value
        temperature_raw = data["temperature"]["value"]
        # Truncate to one decimal place
        temperature = int(temperature_raw * 10) / 10.0

        # Print the temperature
        print(f"Temperature: {temperature} °C")
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data: {e}")

    # Wait for 60 seconds before the next iteration
    time.sleep(60)