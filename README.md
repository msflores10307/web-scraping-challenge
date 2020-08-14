# web-scraping-challenge

This repo contains solutions and resources for the web-scraping challenge.

The solutions for this challenge are cointained in the 'Missions_to_Mars' directory.
This directory contains three key files. 

### Solution 
1. scrape_mars.py 
This file contains code to define a python function that performs all the required web scraping.

2. app.py 
This python file contains the definition of the flask endpoints and logic to create, read, update, and delete records
in a mongo database. The mongo database contains the data obtained by web-scraping. 

3. templates/index.html. 
This html file contains a bootstrap-formatted page that displays scraped data. The page is populated by using flask templating to 
display web-scraped data stored in a mongo db. 

The initial exploration and data scraping was conducted in the file 'mission-to-mars.ipynb'

### Screenshots
Screen Shots of the solutions are stored in the directory, 'screenshots'. 
1. landing.png
This image displays what the user sees immediately upon arriving on my page. The button labeled "Scrape the Surface of Mars!"
will launch a refresh of the scraped data and redirect the user to the home page, which now displays updated data. This image shows the 
featured image from the nasa website.

2. display.png
This image shows the various pieces of scraped information: Mars headlines and news snippetrs from the Nasa site, the most recent Mars weather tweet, and the facts table.

3. hemispheres1.png
This image displays the first two hemispheres in a row.

4. hemispheres2.png
This image displays the last two mars hemispheres in a row. 

5. landing_refresh.png
This image displays the website immediately after hitting the "Scrape the Surface of Mars!" button. 
Notice the featured image has change.