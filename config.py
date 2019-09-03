import os

from pymongo import MongoClient

}

REFRESH_FREQUENCY_FORECAST = 10800
REFRESH_FREQUENCY_CURRENT = 60

APP_ID = os.getenv('WEATHER_API_KEY')
MONGO_URL = os.getenv('WEATHER_MONGO_URL', 'localhost:27017')

DB = MongoClient(MONGO_URL)

CITIES = {
    'Washington DC': {'latitude': 38.8761, 'longitude': -77.0389, 'zip': 20500},
    'Chicago': {'latitude': 41.8726, 'longitude': -87.5844, 'zip': 60601},
    'New York': {'latitude': 40.7244, 'longitude': -74.0561, 'zip': 10005},
    'San Francisco': {'latitude': 37.7827, 'longitude': -122.4467, 'zip': 94104}