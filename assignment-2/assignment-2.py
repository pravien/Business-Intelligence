import os
import pandas as pd
from tqdm import tqdm
from geopy.geocoders import Nominatim


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
        print('here')
        location = geolocator.geocode(search_address)
        print('after')
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

if __name__ == '__main__':
    df = pd.read_csv('./test.csv', index_col=None, header=0)
    #enable to get geocodes. #df['lat'],df['long']= zip(*df.apply (lambda row: get_locations(row['address'].split(',')[0],row['zip_code']), axis=1))
    #  convert the column to a datetime object.
    df['sell_date'] = pd.to_datetime(df['sell_date'],format='%d-%m-%Y')
    df['zip_code_num'] = df.apply(lambda x: remove_city_name(x['zip_code']), axis=1)
   #print(df['sell_date'][0].year)
    #print(df['zip_code_num'])
    mask_1992 = ((df['sell_date'].dt.year == 1992) & 
     ((df['zip_code_num'] == '1050') | (df['zip_code_num'] == '1049') | (['zip_code_num'] == '5000') | 
     (['zip_code_num'] == '8000') | (['zip_code_num'] == '9000'))
     )

    mask_2016 = ((df['sell_date'].dt.year == 2016) & 
     ((df['zip_code_num'] == '1050') | (df['zip_code_num'] == '1049') | (['zip_code_num'] == '5000') | 
     (['zip_code_num'] == '8000') | (['zip_code_num'] == '9000'))
     )
    print(df[mask_1992])
    