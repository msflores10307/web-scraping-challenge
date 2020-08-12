#import dependencies
from flask import Flask, jsonify, render_template
from scrape_mars import scrape
import pymongo

# Flask Setup

app = Flask(__name__)
# engine = create_engine("sqlite:///Resources/hawaii.sqlite")
# Base = automap_base()
# Base.prepare(engine,reflect = True)
# measurement = Base.classes.measurement
# station = Base.classes.station

# Mongo Set Up
conn = 'mongodb://localhost:27017'
client = pymongo.MongoClient(conn)

# Define the 'MarsDB' database in Mongo

db = client.MarsDB
collection = db.mission
collection.drop()
mission = db.mission.find()

# API Endpoints: The following section of code contains functions to produce api endpoints

# scraper
@app.route("/scrape")
def scraper():
    output = scrape()
    db.mission.insert_one(output)

    return("Scrape Complete")


# home: 
@app.route("/")
def home():
    # return(jsonify(scrape()))
    return render_template("index.html", var1= "Testing Testing 1 2 3")



if __name__ == "__main__":
    app.run(debug=True)