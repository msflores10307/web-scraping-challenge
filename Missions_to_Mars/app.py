#import dependencies
from flask import Flask, jsonify, render_template, redirect
from scrape_mars import scrape
import pymongo

# Flask Setup

app = Flask(__name__)


# Mongo Set Up
conn = 'mongodb://localhost:27017'
client = pymongo.MongoClient(conn)

# API Endpoints: The following section of code contains functions to produce api endpoints

# scraper
@app.route("/scrape")
def scraper():

    #define database connection and client
    conn = 'mongodb://localhost:27017'
    client = pymongo.MongoClient(conn)

    # define database and collection
    db = client.MarsDB
    collection = db.mission

    # drop former collection
    collection.drop()
    mission = db.mission.find()

    # generate new document and insert into mongo
    output = scrape()
    db.mission.insert_one(output)

    #return home
    return redirect("/")

# home: 
@app.route("/")
def home():
    # define database connection and client
    conn = 'mongodb://localhost:27017'
    client = pymongo.MongoClient(conn)

    # define database and extract collection document
    db = client.MarsDB
    missions = db.mission.find()

    # extract json
    for mission in missions:
        msg = mission

    # render content to html
    return render_template("index.html", dict = msg)






if __name__ == "__main__":
    app.run(debug=True)