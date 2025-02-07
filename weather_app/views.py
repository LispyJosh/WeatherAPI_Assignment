from django.shortcuts import render
import requests  # For making API calls
import datetime  # For formatting timestamps
import os  # For accessing environment variables
from dotenv import load_dotenv  # For loading environment variables from .env file

# Load environment variables from the .env file
load_dotenv()
API_KEY = os.getenv('API_KEY')  # Fetch API key from environment variables

# OpenWeather API URLs
CURRENT_WEATHER_URL = "https://api.openweathermap.org/data/2.5/weather?q={}&appid={}"
HOURLY_FORECAST_URL = "https://pro.openweathermap.org/data/2.5/forecast/hourly?lat={}&lon={}&appid={}"

def fetch_weather_and_forecast(city, api_key):
    """
    Fetch current weather and hourly forecast for a given city.

    Args:
        city (str): The city name.
        api_key (str): API key for OpenWeather.

    Returns:
        tuple: A dictionary with current weather data and a list of hourly forecast dictionaries.
    """
    try:
        # Fetch current weather data
        response = requests.get(CURRENT_WEATHER_URL.format(city, api_key)).json()
        
        # Check for errors in the response
        if response.get("cod") != 200:
            return None, None  # Return None if city is invalid or API call fails
        
        # Extract latitude and longitude for hourly forecast
        lat, lon = response['coord']['lat'], response['coord']['lon']

        # Prepare current weather data dictionary
        weather_data = {
            "city": city,
            "temperature": round(response['main']['temp'] - 273.15, 2),  # Convert from Kelvin to Celsius
            "description": response['weather'][0]['description'],  # Weather description (e.g., "clear sky")
            "icon": response['weather'][0]['icon']  # Weather icon code
        }
        
        # Fetch hourly forecast data
        forecast_response = requests.get(HOURLY_FORECAST_URL.format(lat, lon, api_key)).json()
        
        # Check for errors in the forecast response
        if forecast_response.get("cod") != "200":
            return weather_data, []  # Return current weather data and empty forecast if call fails

        # Extract and format hourly forecast data
        hourly_forecasts = []
        for forecast in forecast_response['list'][:5]:  # Limit to the first 5 forecasts
            hourly_forecasts.append({
                "time": datetime.datetime.fromtimestamp(forecast['dt']).strftime("%I:%M %p"),  # Format time
                "temp": round(forecast['main']['temp'] - 273.15, 2),  # Convert temperature to Celsius
                "description": forecast['weather'][0]['description'],  # Weather description
                "icon": forecast['weather'][0]['icon']  # Weather icon code
            })

        return weather_data, hourly_forecasts  # Return both current weather and hourly forecasts
    except Exception as e:
        print(f"Error fetching data for {city}: {e}")  # Log error for debugging
        return None, None  # Return None if an exception occurs

def index(request):
    """
    Render the weather comparison page. Handles form submissions for city input.

    Args:
        request: The HTTP request object.

    Returns:
        HttpResponse: Renders the index.html template with weather data.
    """
    # Initialize weather and forecast data
    weather_data1, weather_data2 = None, None
    hourly_forecasts1, hourly_forecasts2 = [], []

    # Handle form submission
    if request.method == "POST":
        # Get city names from form inputs
        city1 = request.POST.get("city1")
        city2 = request.POST.get("city2")
        
        # Fetch data for City 1 if provided
        if city1:
            weather_data1, hourly_forecasts1 = fetch_weather_and_forecast(city1, API_KEY)
        
        # Fetch data for City 2 if provided
        if city2:
            weather_data2, hourly_forecasts2 = fetch_weather_and_forecast(city2, API_KEY)

    # Render the template with fetched data
    return render(request, 'weather_app/index.html', {
        "weather_data1": weather_data1,
        "weather_data2": weather_data2,
        "hourly_forecasts1": hourly_forecasts1,
        "hourly_forecasts2": hourly_forecasts2
    })
