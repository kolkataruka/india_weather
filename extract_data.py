import imdlib as imd
import pandas as pd
import numpy as np
import json

with open('geocodes.json', 'r') as infile:
    cities = json.load(infile)

start_year, end_year = 1952, 2022

rain_data = imd.get_data('rain', start_year, end_year, fn_format='yearwise')
tmin_data = imd.get_data('tmin', start_year, end_year, fn_format='yearwise')
tmax_data = imd.get_data('tmax', start_year, end_year, fn_format='yearwise')

for city in cities:
    rain_data.to_csv(city['city'].split(' ')[0] + '_rain.csv', city['latitude'], city['longitude'], '/Users/anushkakataruka/Desktop/DataJournalismThings/Hindu/India_weather/india_weather/data')
    tmin_data.to_csv(city['city'].split(' ')[0] + '_tmin.csv', city['latitude'], city['longitude'], '/Users/anushkakataruka/Desktop/DataJournalismThings/Hindu/India_weather/india_weather/data')
    tmax_data.to_csv(city['city'].split(' ')[0] + '_tmax.csv', city['latitude'], city['longitude'], '/Users/anushkakataruka/Desktop/DataJournalismThings/Hindu/India_weather/india_weather/data')
    columns = d
