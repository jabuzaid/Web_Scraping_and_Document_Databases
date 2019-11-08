# Mission to Mars

![mission_to_mars](sandbox/Images/mission_to_mars.jpg)

In this assignment, I built a web application that scrapes various websites for data related to the Mission to Mars and displayed the information in a single HTML page. Here are the outlines for what I did.

## Step 1 - Scraping

The initial scraping was done using Jupyter Notebook, BeautifulSoup, Pandas, and Requests/Splinter.

* Created a Jupyter Notebook file called `mission_to_mars.ipynb` and used it to complete all the scraping and analysis tasks. The following outlines what I scraped.

### NASA Mars News

* Scraped the [NASA Mars News Site](https://mars.nasa.gov/news/) and collected the latest News Title and Paragraph Text. Assigned the text to variables that I can reference later.

```python
# Example:
news_title = "NASA's Next Mars Mission to Investigate Interior of Red Planet"

news_p = "Preparation of NASA's next spacecraft to Mars, InSight, has ramped up this summer, on course for launch next May from Vandenberg Air Force Base in central California -- the first interplanetary launch in history from America's West Coast."
```

### JPL Mars Space Images - Featured Image

* Visited the url for JPL Featured Space Image [here](https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars).

* Used splinter to navigate the site and found the image url for the current Featured Mars Image and assigned the url string to a variable called `featured_image_url`.

* found the image url to the full size `.jpg` image.

* Saved the complete url string for this image.

```python
# Example:
featured_image_url = 'https://www.jpl.nasa.gov/spaceimages/images/largesize/PIA16225_hires.jpg'
```

### Mars Weather

* Visited the Mars Weather twitter account [here](https://twitter.com/marswxreport?lang=en) and scraped the latest Mars weather tweet from the page. Saved the tweet text for the weather report as a variable called `mars_weather`.

```python
# Example:
mars_weather = 'Sol 1801 (Aug 30, 2017), Sunny, high -21C/-5F, low -80C/-112F, pressure at 8.82 hPa, daylight 06:09-17:55'
```

### Mars Facts

* Visited the Mars Facts webpage [here](http://space-facts.com/mars/) and used Pandas to scrape the table containing facts about the planet including Diameter, Mass, etc.

* Used Pandas to convert the data to a HTML table string.

### Mars Hemispheres

* Visited the USGS Astrogeology site [here](https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars) to obtain high resolution images for each of Mar's hemispheres.

* I click each of the links to the hemispheres in order to find the image url to the full resolution image.

* I Save both the image url string for the full resolution hemisphere image, and the Hemisphere title containing the hemisphere name. I used a Python dictionary to store the data using the keys `img_url` and `title`.

* Appended the dictionary with the image url string and the hemisphere title to a list. The list will contain one dictionary for each hemisphere.

```python
# Example:
hemisphere_image_urls = [
    {"title": "Valles Marineris Hemisphere", "img_url": "..."},
    {"title": "Cerberus Hemisphere", "img_url": "..."},
    {"title": "Schiaparelli Hemisphere", "img_url": "..."},
    {"title": "Syrtis Major Hemisphere", "img_url": "..."},
]
```

- - -

## Step 2 - MongoDB and Flask Application

I Used MongoDB with Flask templating to create a new HTML page that displayed all of the information that was scraped from the URLs above.

* Started by converting the Jupyter notebook into a Python script called `scrape_mars.py` with the function `scrape` that executed all of the scraping code from above and returned one Python dictionary containing all of the scraped data.

* Next, I created a route called `/scrape` that imported the `scrape_mars.py` script and called it in `scrape` function.

  * Stored the return value in Mongo as a Python dictionary.

* Created a root route `/` to query the Mongo database and passed the mars data into an HTML template to display the data.

* Created a template HTML file called `index.html` that took the mars data dictionary and displayed all of the data in the appropriate HTML elements. I used the following as a guide for what the final product looked like.

![final_app_part1.png](sandbox/Images/final_app_part1.png)
![final_app_part2.png](sandbox/Images/final_app_part2.png)

- - -


## Copyright

Trilogy Education Services © 2017. All Rights Reserved.
