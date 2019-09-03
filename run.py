import datetime
import threading
import time
import webbrowser

from config import CITIES, REFRESH_FREQUENCY_FORECAST, REFRESH_FREQUENCY_CURRENT
from utils import persist_data_mongodb, fetct_hourly_data_zip, add_field, open_map_url

#forecast for the following 5 days/ 3 hours
def fetch_5day_3hr_forecast():
    
    while True:
        for city in CITIES:
            zip_code = CITIES[city]['zip']
            hour = 'forecast'
            json_data_hourly = fetct_hourly_data_zip(hour, zip_code)
            formatted_hourly = json_data_hourly['list'][0]['weather'][0]['main']
            time_forecast = json_data_hourly['list'][0]['dt_txt']
            persist_data_mongodb('fiveDayUpdate', add_field(json_data_hourly))
            if formatted_hourly != 'Clear':
                print('{0:>27}: {1:>20}: {2} in {3}'.format(time_forecast, 'The weather will be', formatted_hourly,
                                                            city))
        time.sleep(REFRESH_FREQUENCY_FORECAST)

#fetch current weather	
def fetch_current_weather():
   
    while True:
        for city in CITIES:
            zip_code = CITIES[city]['zip']
            current = 'weather'
            json_data_current = fetct_hourly_data_zip(current, zip_code)
            formatted_current = json_data_current['weather'][0]['main']
            current_weather_timestamp = datetime.datetime.now().isoformat()
            persist_data_mongodb('currentUpdate', json_data_current)
            print('{0:>27}: {1:>20}: {2} in {3}'.format(current_weather_timestamp, 'Current Weather',
                                                        formatted_current, city))
        time.sleep(REFRESH_FREQUENCY_CURRENT)





def open_map(map_type):
   
    for city in CITIES:
        latitude = CITIES[city]['latitude']
        longitude = CITIES[city]['longitude']
        url = open_map_url(map_type, latitude, longitude)
        webbrowser.open(url)


def main():
    print("""
The different types of maps you can access are:
clouds
precipitation
temperature
windspeed
    """)

    map_type = 'temperature'

    t1 = threading.Thread(target=fetch_5day_3hr_forecast, args=())
    t2 = threading.Thread(target=fetch_current_weather, args=())
    t3 = threading.Thread(target=open_map, args=(map_type,))
   
    t1.start()
    t2.start()
    t3.start()
    


if __name__ == "__main__":
    main()
