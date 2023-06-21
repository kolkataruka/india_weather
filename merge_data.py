import imdlib as imd
import pandas as pd
import numpy as np
import json

with open('geocodes.json', 'r') as infile:
    cities = json.load(infile)

overall_frames = []

for city in cities:
    name = city['city'].split(' ')[0]
    lat = str(round(city['latitude'], 2))
    long = str(round(city['longitude'],2))
    if (lat[-3] != '.'):
        lat = lat + '0'
    if (long[-3] != '.'):
        long = long + '0'
    lat_long = lat + '_' + long
    rain = pd.read_csv('data/' + name + '_rain_' + lat_long + '.csv')
    tmax = pd.read_csv('data/' + name + '_tmax_' + lat_long + '.csv')
    tmin = pd.read_csv('data/' + name + '_tmin_' + lat_long + '.csv')
    rain23 = pd.read_csv('data/' + name + '2023_rain_' + lat_long + '.csv')
    tmax23 = pd.read_csv('data/' + name + '2023_tmax_' + lat_long + '.csv')
    tmin23 = pd.read_csv('data/' + name + '2023_tmin_' + lat_long + '.csv')
    columns = list(rain)

    archive_data = pd.DataFrame()
    archive_data['City'] = city['city']
    archive_data['Date'] = rain[columns[0]]
    archive_data['Rain'] = rain[columns[1]]
    archive_data['T-Max'] = tmax[columns[1]]
    archive_data['T-Min'] = tmin[columns[1]]

    data_23 = pd.DataFrame()
    archive_data['City'] = city['city']
    data_23['Date'] = rain23[columns[0]]
    data_23['Rain'] = rain23[columns[1]]
    data_23['T-Max'] = tmax23[columns[1]]
    data_23['T-Min'] = tmin23[columns[1]]

    frames = [archive_data, data_23]
    final_data = pd.concat(frames, ignore_index=True)
    overall_frames.append(final_data)
    data_printed = final_data.to_csv('final_data/' + name[:-1] + '.csv')

overall_data = pd.concat(overall_frames, ignore_index=True)
final_print = overall_data.to_csv('final_data/all_cities.csv')


