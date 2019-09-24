# Business-Intelligence

Group Name : Ill Introduction<br/>
Group Members : Lovro Bilješković, Mikkel Lindstrøm Hansen, Pravien Thaveenrasingam

# Assignment - 3

The source code can be found in [assignment-3](https://github.com/pravien/Business-Intelligence/tree/master/assignment-3).

---

## Requirements

- You need to install Basemap. (not in pip so you have to use conda or something different)
- There are some module's you have to download using pip. All of the needed module's are specified in the top of the notebook or before they are needed for the specific code.

---

## How to run the code

1. Clone the project and cd into it.

2. Open the notebook by running the command jupyter-notebook.

3. Check if you have all of the modules installed. If not install them.

4. Run the code blocks.

---

## Solutions


### Create a plot with the help of Basemap, on which you plot sales records for 2015 which are not farther away than 50km from Copenhagen city center (lat: 55.676111, lon: 12.568333)

we have sat a limit to only show tre, because all of the dots a placed close to each other so it gets messy.

![alt text](https://github.com/pravien/Business-Intelligence/tree/master/assignment-3/basemap.png)

---

### Use folium to plot the locations of the 1992 housing sales for the city centers of Copenhagen (zip code 1000-1499), Odense (zip code 5000), Aarhus (zip code 8000), and Aalborg (zip code 9000), see Assignment 2 onto a map.

See the file large_flat_trades.html

---

### Create a 2D plot, which compares prices per square meter (on the x-axis) and distance to Nørreport st. (y-axis) for all housing on Sjæland for the year 2005 and where the zip code is lower than 3000 and the price per square meter is lower than 80000Dkk. Describe in words what you can read out of the plot. Formulate a hypothesis on how the values on the two axis might be related.

From looking at the plot we can see there are alot of sales close to Nørreport St. Some are cheap and some are expensive. But when you are far away the price drops.<br/>
Hypothesis: The further away you live from Nørreport St. the cheaper the price per square meter is

![alt text](https://github.com/pravien/Business-Intelligence/tree/master/assignment-3/2d-plot.png)

---

### Create a histogram (bar plot), which visualizes the frequency of house trades per zip code area corresponding to the entire dataset of housing sale records.

![alt text](https://github.com/pravien/Business-Intelligence/tree/master/assignment-3/hist.png)