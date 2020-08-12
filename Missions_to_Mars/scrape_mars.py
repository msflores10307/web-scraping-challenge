def scrape(): 
    #import dependencies
    from bs4 import BeautifulSoup 
    import requests
    import pandas as pd
    from splinter import Browser
    import time


    # Nasa news
    url = 'https://mars.nasa.gov/news/'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    headline = soup.find_all('div',class_='content_title')[0].text.replace('\n','')
    headline_paragraph = soup.find_all('div',class_='slide')[0].text.replace('\n','')

    # driver path
    executable_path = {'executable_path': 'chromedriver.exe'}

    #Featured Image 
    browser = Browser('chrome', **executable_path, headless=False)
    url = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
    browser.visit(url)
    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')
    style_block = soup.find('article', class_='carousel_item')['style']
    index = style_block.index("'")
    index2 = style_block.index(");")
    image_address = style_block[index:index2].replace("'",'')
    image_url = f"https://www.jpl.nasa.gov{image_address}"

    url = url = 'https://twitter.com/marswxreport?lang=en' 
    browser.visit(url)
    time.sleep(10)
    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')
    tweets = soup.find('body').find('div',class_="css-901oao r-hkyrab r-1qd0xha r-a023e6 r-16dba41 r-ad9z0x r-bcqeeo r-bnwqim r-qvutc0").find_all('span',class_="css-901oao css-16my406 r-1qd0xha r-ad9z0x r-bcqeeo r-qvutc0")
    latest_tweet = tweets[0].text

    # mars facts
    pdurl = 'https://space-facts.com/mars/'
    facts = pd.read_html(pdurl)[0].rename(columns={0:'Mars Fact',1:'Quantity'})
    html_string = facts.to_html() #.replace('\n','')
    outfile = open('facts.html','w')
    outfile.write(html_string)
    outfile.close()


    # Mars Hemispheres
    # browser = Browser('chrome', **executable_path, headless=False)                
    url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'

    hemispheres = ['Valles Marineris',"Cerberus","Schiaparelli","Syrtis Major"]
    hemisphere_image_urls = []

    for h in hemispheres:
        browser.visit(url)
        window = browser.windows[0]
        browser.click_link_by_partial_text(f'{h}')
        browser.click_link_by_partial_text('Sample')
        windex = len(browser.windows) - 1
        browser.windows.current = browser.windows[windex]
        target = browser.url
        # print(target)
        img_url = {f'{h}':target}
        hemisphere_image_urls.append(img_url)    
        # print(hemisphere_image_urls)

    out = {"headline": headline, 'headline_paragraph':headline_paragraph,
        "featured_image": image_url,
        "tweet":latest_tweet,
        "facts": html_string,
        "hemispheres":hemisphere_image_urls}

    return(out)
