import lakepy as lk
# for scraping
from selenium import webdriver
from bs4 import BeautifulSoup
import requests
# for data
import pandas as pd
import re

def main():
    page = requests.get("https://developers.google.com/public-data/docs/canonical/countries_csv")
    if page.status_code == 200:
        print( "Open Success!")
        content = page.content
        soup = BeautifulSoup( content, 'html.parser')
    else:
        print( "Error opening webpage")
        exit(1)

    text = soup.find( template="page").get_text()
    lines = text.split("\n")
    parsed = list(filter(lambda a: a != '', lines))

    flag = False
    data = []
    for item in parsed:
        if flag:
            data.append(item)
        if item == "name":
            flag = True
        if "Zimbabwe" == item:
            flag = False

    data.remove('UM')
    data.remove('U.S. Minor Outlying Islands')
    betterData = []

    for val in range( 0, len( data), 4):
        betterData.append( data[ val:val + 4])

    df = pd.DataFrame( betterData, columns = ["Code", "Latitude", "Longitude", "Name"])
    print (df)
    df.to_csv("countrydata.csv")
    print("done :)")

if __name__ == "__main__":
    try:
        main()
    except OSError as e:
        print("[Errno {0}] {1}".format(e.errno, e.strerror))
        
