from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
import Scrape_mars

app = Flask(__name__)

app.config["MONGO_URI"] = "mongodb://localhost:27017/craigslist_app"
mongo = PyMongo(app)

@app.route("/")
def index():
    mars_data = mongo.db.mars_info.find_one()
    return render_template("index.html", mars_info=mars_info)

@app.route("/scrape")
def scrape():
    mars_info=scrape_mars.scrape_mars_news()
    mars_info=scrape_mars.scrape_mars_image_url()
    mars_info=scrape_mars.scrape_mars_weather()
    mars_info=scrape_mars.scrape_mars_facts()
    return redirect("/", code=302)

if _name_ =="_main_":
    app.run(debug=True)
