import os
import csv
import requests
import platform
import statistics
import matplotlib
# makes sure that mathplot only renders PNG
matplotlib.use('agg')
import matplotlib.pyplot as plt

#Takes an URL and downloads from the url to a specified path and creates
# a file and put the downloaded content inside that file
def download_txt(url, save_path='./downloaded'):
    response = requests.get(url)
    with open(save_path, 'wb') as f:
        f.write(response.content)

#This function takes two parameters: text input and the csv output
def generate_csv(txt_input_path, csv_output_path):
    #Opens the file at txt_input_path and read all of the lines
    with open(txt_input_path, encoding='utf-8') as f:
        txt_content = f.readlines()

    rows = [['street', 'city', 'price', 'sqm', 'price_per_sqm']]
    #Loop through each element in txt_content
    for line in txt_content:
        #removes any trailing charachters and replaces "*" with empty.
        line = line.rstrip().replace('  * ', '')
        #Split the line by tab.
        address, price, sqm = line.split('\t')
        #Split the address variable by '; '
        street, city = address.split('; ')
        #The // means that there are no decimals.
        price_per_sqm = int(price) // int(sqm)
        #Makes a tuble.
        row = (street, city, price, sqm, price_per_sqm)
        #Append value to list named row.
        rows.append(row)
    #Checks if the platform is windows if it is, it changes the newline to empty
    if platform.system() == 'Windows':
        newline=''
    else:
        newline=None
    #Open/ creates a file at path csv_output_path in write mode.
    with open(csv_output_path, 'w', newline=newline, encoding='utf-8') as f:
        output_writer = csv.writer(f)
        #Go through each row in rows and write each row to a csv file.
        #Using the csv.writer
        for row in rows:
            output_writer.writerow(row)


def read_prices(csv_input_path):
    with open(csv_input_path, encoding='utf-8') as f:
        #instantiate the csv reader.
        reader = csv.reader(f)
        #We read the new row in the csv file, which is the header.
        _ = next(reader)

        idxs = []
        prices = []
        #Goes though each row in the csv file
        for row in reader:
            #Unpacks the 3. value from the tuple.
            _, _, price, _, _ = row
            #Appends the line number to the idxs list.
            idxs.append(reader.line_num)
            #Appends the price to the prices list.
            prices.append(int(price))
    #return a list consisting of tuple containing the index and price.
    return list(zip(idxs, prices))


def compute_avg_price(data):
    #Unpack the prices from the data variable
    _, prices = zip(*data)
    #Calculates the mean of the list prices.
    avg_price = statistics.mean(prices)
    try:
        with open('./avg_price.txt', 'w', encoding='utf-8') as f:
            f.write(str(avg_price))
            return avg_price
    except:
        print('failed')
        return avg_price

# Generates a scatter plot which is saved as prices.png
def generate_plot(data):
    #Unpacks the data object
    x_values, y_values = zip(*data)
    fig = plt.figure()
    plt.scatter(x_values, y_values, s=100)
    fig.savefig('./prices.png', bbox_inches='tight')

#Generates a histrogram and saves it as prices-hist.png
def generate_histogram(data):
    #Unpacks the data from data. This is posible because data is a tuple.
    indx, prices = zip(*data)
    prices = list(prices)
    print('minimum: ',min(prices),', max: ',max(prices))
    #Set the figure size.
    fig = plt.figure(figsize=(10, 10))
    #Set figure title
    fig.suptitle('Housing prices')
    # Rotate the x label values by 45 degrees.
    plt.xticks(rotation=45)
    # Add y label.
    plt.ylabel('Amount of houses')
    plt.xlabel('Prices')
    #Generetaes the histogram with a edgecolor of black and a linewidth of 1.2.
    #The histogram uses 7 bins.
    plt.hist(prices,bins=range(250000,8000000,1000000),edgecolor='black', linewidth=1.2)
    fig.savefig('./prices-hist.png')

def run():
    file_url = 'https://raw.githubusercontent.com/datsoftlyngby/' \
               'soft2019fall-bi-teaching-material/master/' \
               'week35/data/price_list.txt'
    #Gets the name of the file we are downloading - this produces price_list.txt
    txt_file_name = os.path.basename(file_url)
    # makes a path which will be - ./price_list.txt
    txt_path = os.path.join('./', txt_file_name)
    #Calls the download function.
    download_txt(file_url, txt_path)
    csv_file_name = 'price_list.csv'
    #creates the os path- which will be the "current wokring path/price_list.csv"
    csv_path = os.path.join(os.getcwd(), csv_file_name)
    #Calls the generate_csv function.
    generate_csv(txt_path, csv_path)
    #Calls the read_prices function
    data = read_prices(csv_path)
    #Calls the compute_avg_price
    avg_price = compute_avg_price(data)
    #prints the avrage price.
    print(avg_price)
    # call the functions which generate the scatter and histogram.
    generate_plot(data)
    generate_histogram(data)
#    ...
# This is the part which tells python which code to run when it is called.
# This also makes sure that code there is not within a functions not gets called.
if __name__ == '__main__':
    run()
