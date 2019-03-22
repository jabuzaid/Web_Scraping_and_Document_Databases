# Joe J. Abuzaid
# UC Berkely Extension Data Analytics Bootcamp
# UCBSAN20181106DATA
# Homework 12: Web Scrabing & Document Data Bases
# In this assignment, I built a web application that scraped various websites for data related to the Mission to Mars
# and displayed the information in a single HTML page. The following outlines what I did:
#############################################################################
# Step 1 - Scraping

# Mission to Mars Web application
# Dependencies
from splinter import Browser
from bs4 import BeautifulSoup as bs
import requests
import os
import pandas as pd


def init_browser():
    executable_path = {'executable_path': '/usr/local/bin/chromedriver'}
    browser = Browser('chrome', **executable_path, headless=False)


def scrape():
    browser = init_browser()
    # NASA Mars News
    # Retrieve page with the requests module
    url = 'https://mars.nasa.gov/news/'
    browser.visit(url)
    # Create a Beautiful Soup object
    soup = bs(browser.html, 'html.parser')
    # Create a dictionary for all of the scraped data
    mars_data = {}
    # collecting the latest News Title Text.
    news_title = soup.find("div", class_="content_title").text
    # Add the title to the dictionary
    mars_data["mars_news_title"]= news_title
    # collecting the latest Paragraph Text.
    news_p = soup.find("div", class_="article_teaser_body").text
    # Add the summary to the dictionary
    mars_data["summary"]= news_p


    ## Featured Image
    # Visit the url for JPL Featured Space Image
    url = "https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars"
    browser.visit(url)
    browser.click_link_by_partial_text("FULL IMAGE")
    browser.click_link_by_partial_text("more info")
    # Create a Beautiful Soup object
    soup = bs(browser.html, 'html.parser')
    featured_image_url = "https://www.jpl.nasa.gov" + soup.find("img", class_="main_image")["src"]
    # Add the featured image url to the dictionary
    mars_data["featured_image_url"] = featured_image_url


    ## Mars Weather
    # Visiting the Mars Weather Twitter account.
    url = "https://twitter.com/marswxreport?lang=en"
    browser.visit(url)
    # Create a Beautiful Soup object
    soup = bs(browser.html, 'html.parser')
    # Scraping the latest Mars weather tweet from the page.
    mars_weather = soup.find("div", class_="js-tweet-text-container").text
    # Add the weather to the dictionary
    mars_data["mars_weather"] = mars_weather


    # Mars Weather Twitter account.
    url = "http://space-facts.com/mars/"
    df = pd.read_html(url)[0]
    df.columns=['parameter', 'value']
    df.set_index('parameter', inplace =True)
    # Add the Mars facts table to the dictionary
    mars_data["mars_facts"] = df
    html_data = df.to_html()
    # Add the Mars facts table html to the dictionary
    mars_data["mars_facts_html_data"] = html_data


    # Mars Hemispheres
    # Visiting the USGS Astrogeology site.
    url = "https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars)"
    browser.visit(url)
    # Create a Beautiful Soup object
    soup = bs(browser.html, 'html.parser')
    #clicking each of the links to the hemispheres in order to find the 
    # image url to the full resolution image and saving it with the title.
    # Use a Python dictionary to store the data using the keys `img_url` and `title`.
    links = soup.findAll("a", class_="itemLink product-item")
    links
    mars_hemi = []
    for i in links:
        title = i.text
        newlink = "https://astrogeology.usgs.gov/"+i['href']
        if(title):
            print(title)
            print(newlink)
            browser.visit(newlink)
            soup = bs(browser.html, 'html.parser')
            largimage = soup.find("img", class_="wide-image")
            print(largimage['src'])
            mars_hemi.append({"Title":title,"image":largimage['src']})     
    # Add mars_hemi img_url` and `title` to the dictionary        
    mars_data["mars_hemi"] = mars_hemi
    return mars_data