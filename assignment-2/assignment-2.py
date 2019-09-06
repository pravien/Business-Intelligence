import os
from os.path import join
import pandas as pd
from tqdm import tqdm
from geopy.geocoders import Nominatim
from statistics import mean
import requests


def get_locations(address, zip_code):
    try:
        # This removes information about a flats storey
        address_field = address.split(', ')[0]
        # This one removes trailing letters on the city name
        # It seems as if Openstreetmap cannot handle København H
        # but it works with København
        zip_field = ' '.join(zip_code.split(' ')[:-1])
        search_address = ', '.join([address_field, zip_field])

        geolocator = Nominatim()
        location = geolocator.geocode(search_address)
        return location.latitude, location.longitude
    except:
        print('Skipped geocoding of {} {}'.format(address, zip_code))
        return None, None


def remove_city_name(zip_code):
    return ' '.join(zip_code.split(' ')[:-2])


def create_data_frame():
    li = []
    for filename in os.listdir('./boliga_stats'):
        #filename = os.path.join(os.getcwd(),filename)
        df = pd.read_csv(os.path.join('./boliga_stats',filename), index_col=None, header=0)
        li.append(df)

    return pd.concat(li, axis=0, ignore_index=True)


def create_city_csv(dataframe, year):
    cities = {
              'Odense': '5000',
              'København': '1049',
              'Aarhus': '8000',
              'Aalborg': '9000'}
    folder_path = join(os.getcwd(),year)          
    if not os.path.exists(folder_path):
        os.mkdir(folder_path)
        
    for city in cities:
        mask = (dataframe['zip_code_num'] == cities[city])
        dataf = dataframe[mask]
        dataf.to_csv('./' + year + '/' + city + ".csv", index=False,encoding='utf-8')


if __name__ == '__main__':

    # read the csv.
    df = create_data_frame()
    # Add 2 new columns for latitude and longitude and writes i to a csv file.
    df['lat'],df['long']= zip(*df.apply (lambda row: get_locations(row['address'].split(',')[0],row['zip_code']), axis=1))
    df.to_csv("lat-long.csv", index=False,encoding='utf-8')


    
    '''
    #  convert the column to a datetime object.
    df['sell_date'] = pd.to_datetime(df['sell_date'],format='%d-%m-%Y')
    df['zip_code_num'] = df.apply(lambda x: remove_city_name(x['zip_code']), axis=1)
    mask_1992 = ((df['sell_date'].dt.year == 1992) & 
     ((df['zip_code_num'] == '1050') | (df['zip_code_num'] == '1049') | (df['zip_code_num'] == '5000') | 
     (df['zip_code_num'] == '8000') | (df['zip_code_num'] == '9000'))
     )

    mask_2016 = ((df['sell_date'].dt.year == 2016) & 
     ((df['zip_code_num'] == '1050') | (df['zip_code_num'] == '1049') | (['zip_code_num'] == '5000') | 
     (['zip_code_num'] == '8000') | (['zip_code_num'] == '9000'))
     )

    create_city_csv(df[mask_1992], '1992')
    print('Average price per square meter for the year 1992 is {} m\u00b2'.format(mean(df[mask_1992]['price_per_sq_m'])),)
    print('Average price per square meter for the year 2016 is {} m\u00b2'.format(mean(df[mask_2016]['price_per_sq_m'])),)

    '''