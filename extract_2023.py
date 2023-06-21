import imdlib as imd
import pandas as pd
import numpy as np
import json

with open('geocodes.json', 'r') as infile:
    cities = json.load(infile)

start_date, end_date = '2023-01-01', '2023-06-20'

rain_data = imd.get_real_data('rain', start_date, end_date, '/Users/anushkakataruka/Desktop/DataJournalismThings/Hindu/India_weather')
tmin_data = imd.get_real_data('tmin', start_date, end_date, '/Users/anushkakataruka/Desktop/DataJournalismThings/Hindu/India_weather')
tmax_data = imd.get_real_data('tmax', start_date, end_date,'/Users/anushkakataruka/Desktop/DataJournalismThings/Hindu/India_weather')

for city in cities:
    rain_data.to_csv(city['city'].split(' ')[0] + '2023_rain.csv', city['latitude'], city['longitude'], '/Users/anushkakataruka/Desktop/DataJournalismThings/Hindu/India_weather/india_weather/data')
    tmin_data.to_csv(city['city'].split(' ')[0] + '2023_tmin.csv', city['latitude'], city['longitude'], '/Users/anushkakataruka/Desktop/DataJournalismThings/Hindu/India_weather/india_weather/data')
    tmax_data.to_csv(city['city'].split(' ')[0] + '2023_tmax.csv', city['latitude'], city['longitude'], '/Users/anushkakataruka/Desktop/DataJournalismThings/Hindu/India_weather/india_weather/data')


