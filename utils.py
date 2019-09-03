from urllib.parse import urlencode

import requests

from config import APP_ID, DB

#Fetch data using the zip 
def fetct_hourly_data_zip(endpoint, zc):
    
    params = urlencode(dict(zip='{0},us'.format(zc), appid=APP_ID))
    url = 'http://api.openweathermap.org/data/2.5/{0}?{1}'.format(endpoint, params)
    return requests.get(url).json()

#Get pymongo client
def get_db():
   
    return DB.weatherUpdate

#Persists data in the database
def persist_data_mongodb(name, json_data):
   
    collection = getattr(get_db(), name)
    collection.insert(json_data)

#Add the start date and end data to assis when retieving the data for graph
def add_field(json_data):
    
    date_stamp_start = json_data['list'][0]['dt']
    date_stamp_end = json_data['list'][-1]['dt']
    json_data['start_date'] = date_stamp_start
    json_data['end_date'] = date_stamp_end
    return json_data

# obtain map url
def open_map_url(map_type, latitude, longitude):
   
    params = urlencode(dict(basemap='map',
                            cities='true',
                            layer=map_type,
                            lat=latitude,
                            lon=longitude,
                            zoom=10))
    url = 'http://openweathermap.org/weathermap?{0}'.format(params)
    return url
