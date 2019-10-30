# Assigment - 2

## **The goal of the assignment**

* Geocode the the entire dataset of Danish housing sales data.
  
    ```python 
    df['lat'],df['long']= zip(*df.apply (lambda row: get_locations(row['address'].split(',')[0],row['zip_code']), axis=1))
    ```
  
* Compute the average price per square meter 
    ```python
    print('Average price per square meter for the year 1992 is {} m\u00b2'.format(mean(df[mask_1992]['price_per_sq_m'])),)
    
    print('Average price per square meter for the year 2016 is {} m\u00b2'.format(mean(df[mask_2016]['price_per_sq_m'])),)
    ```
* Create four new CSV files for the year 1992
  
    ```python
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
    ```

* Create a 2-dimensional scatter plot

    ![](https://github.com/pravien/Business-Intelligence/blob/master/assignment-2/plot-1.png?raw=true)

* Compute the Haversine Distance

```python
for i in zip(df.lat,df.long):
    distances.append(haversine_distance(i,(55.65, 12.083333)))
plt.scatter(df.long,df.lat,c=distances) 
```

![](https://github.com/pravien/Business-Intelligence/blob/master/assignment-2/plot-2.png?raw=true)