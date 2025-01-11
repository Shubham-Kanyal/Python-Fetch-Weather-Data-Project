#FETCH WEATHER DATA PROJECT-
""" FEATURE-1: FETCH THE CURRENT WEATHER DATA OF A GIVEN LOCATION USING OPENWEATHER API
    FEATURE-2: ERROR HANDLING FOR INVALID CITY NAME INPUTS/API CALL FALIURES 
"""
import requests, json
import os       #OPTIONAL FOR ENVIRONMENT HANDLING

""" STEP-1: GENERATE AN API-KEY FROM THE WEBSITE TO FBE ABLE TO USE THE OPENWEATHER API TO FETCH WEATHER DATA
FROM ALL AROUND THE GLOBE, BY JUST ENTERING THE CITY NAME/LOCATION """

#API KEY FOR OPENWEATHER API[https://home.openweathermap.org/api_keys]
api_key = "your_api_key" 

def fetchWeather(cityName):
    #WE 'DO NOT' NEED TO CONVERT THE 'CITY NAME' PROVIDED BY THE USER INTO 'LATITUDES' AND 'LONGITUDES'
    #BECAUSE 'OPENWEATHER' API GIVES THE DATA BASED ON 'CITY NAMES' DIRECTLY! :)    
    
    #STEP-1: Construct the URL with CITY NAME and API KEY[URL FOR ACCESSING DATA FROM THE WEBSITE]
    #'metric' for Celsius
    #'imperial' for Farehnheit
    api_url = f"http://api.openweathermap.org/data/2.5/weather?q={cityName}&appid={api_key}&units=metric"
    
    
    #----------------------------------------------------------------------------------------------------
    
    """STEP-2: GET DATA FROM THE WEBSITE[CALL THE API]-THE 'requests.get()' METHOD SENDS THE 'API REQUEST'
       TO THE WEBSITE'S SERVERS, WHICH RETURNS THE WEATHER DATA IN 'JSON' FORMAT.
    """

    response = requests.get(api_url)
    #print(f'\nResponse: {response.text}')

    """ NOTE: THE 'response.text' IS A STRING CONTAINING THE JSON DATA OF THE API CALL. WE CAN 'PARSE' 
        THIS STRING INTO A DICTIONARY USING THE 'json' LIBRARY ('response.json()' FUNCTION)"""
    
    #----------------------------------------------------------------------------------------------------

    #STEP-3: PARSE THE DATA INTO A DICTIONARY
    weather_data = response.json()
    #print(f'\nWeather Data: {weather_data}')

    #----------------------------------------------------------------------------------------------------
    #STEP-4: PRINT THE DATA
    print(f'\nCity: {weather_data["name"]}')
    print(f'Temperature: {weather_data["main"]["temp"]}°C')
    print(f'Humidity: {weather_data["main"]["humidity"]}%')
    print(f'Weather: {weather_data["weather"][0]["description"].upper()}')
    print(f'Pressure: {weather_data["main"]["pressure"]}')  
    print(f'Wind Speed: {weather_data["wind"]["speed"]}km/hr')   
    #----------------------------------------------------------------------------------------------------r

try:
    fetchWeather(input("Enter City Name: "))
except requests.exceptions.RequestException as e:
    print(f"Error while fetching the data: {e}")
except KeyError as e:
    # Handle errors in case the expected data format is not returned
    print(f"Error in response data: Missing key {e}")
except Exception as e:
    # Catch any other unexpected errors
    print(f"An unexpected error occurred: {e}")
