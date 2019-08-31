# Assingment - 1

## List the all files that this program generates.
   - price_list.csv
   - price_list.txt
   - avg_price.txt
   - prices.png

## Describe which types of files this program generates and attach the contents of each file together with its name to your solution.
   
### price_list.csv

Is a csv file that contains multiple rows of information about many different appartments and what they are valued at. Each row contains a "Street", "City", "Price", "Sqm" and "Price pr sqm"

### price_list.txt

Is a txt file that contains multiple rows of information about many different appartments and what they are valued at. Each row contains a "Street", "City", "Price", "Sqm" and "Price pr sqm"

### avg_price.txt

This file contains the average square meter price.

### prices.png

This file is a picture, which shows the square meter prices for all of the houses in one plot.


## What is the output of this program?
   The output of the program is the average square meter price for all of the houses.

## Describe in natural language -- line-by-line of code -- what the Python script is doing.

See the python file "assignment_1.py", we have made comments.

## Write (code) a function in the assignment_1.py file, which plots a histogram of the price data, with -- say -- 7 bins in the histogram.

```python
def generate_histogram(data):
    indx, prices = zip(*data)
    fig = plt.figure(figsize=(10, 10))
    fig.suptitle('Housing prices pr squaremeter')
    plt.xticks(rotation=45)
    plt.ylabel('Amount of houses')
    plt.xlabel('Prices')
    plt.hist(prices,bins = 7,edgecolor='black', linewidth=1.2)
    fig.savefig('./prices-hist.png')
```

## Write (text) a sentence into the assignment_1.py about the result of the histogram.

This histogram show us that 29 appartments are listed at a price point between 1250000 - 4250000. This is 69 % of the houses from the dataset.

![](prices-hist.png?raw=true)