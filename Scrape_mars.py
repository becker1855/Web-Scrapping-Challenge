from bs4 import BeautifulSoup as bs
from splinter import Browser
import pandas as pd 
import requests 

def init_browser():
    executable_path = {'executable_path': "chromedriver.exe"}
    return Browser("chrome", ** executable_path, headless=True)

mars_data ={}

def scrape_mars_news():
    browser = init_browser()
    url = "https://mars.nasa.gov/news/"
    browser.visit(url)
    html = browser.html
    soup = BeautifulSoup(html, "html.parser")
    news_title = soup.find("div", class_="content_title").text
    mars_info['news_title']= news_title
    news_p = soup.find('div', class_= "article_teaser_body").text
    mars_data['news_p']= news_p
    return mars_data

def scrape_mars_image_url():
    browser = init_browser()
    featured_image_url = "https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars"
    browser.visit(featured_image_url)
    html_image= browser.html
    soup_image = BeautifulSoup(html_image, 'html.parser')
    image_url = soup_image.find('article')['style'].replace('background-image: url(','').replace(');', '')[1:-1]
    main_url= 'https://www.jpl.nasa.gov'
    image_url=main_url+image_url
    mars_data['image_url']= image_url
    return mars_data

def scrape_mars_weather():
    browser = init_browser()
    mars_weather = 'https://twitter.com/marswxreport?lang=en'
    browser.visit(mars_weather)
    html_weather= browser.html
    soup_weather = BeautifulSoup(html_weather, 'html.parser')
    weather= soup_weather.find('p', class_= 'TweetTextSize').text
    mars_data['weather']= weather
    return mars_data

def scrape_mars_facts():
    browser = init_browser()
    mars_facts = 'https://space-facts.com/mars/'
    mars_read = pd.read_html(mars_facts)
    marsdf = mars_read[0]
    mars_data['marsdf'] = marsdf
    return mars_data
