"""
Created 2/24/2022
@author: Ralph Miller
"""
import re
from bs4 import BeautifulSoup
from selenium import webdriver

## Uses headless browser to grab HTML of specific DH menu ##
driver = webdriver.Chrome()
driver.get('https://nutrition.sa.ucsc.edu/')
driver.find_element_by_link_text("College Nine/John R. Lewis Dining Hall").click()
pageSource = driver.page_source
soup = BeautifulSoup(pageSource, 'html.parser')
driver.close()

## Parses HTML with bs4 and find all menu items ##
menuTable = soup.find('table',  {'bordercolor' : '#CCC'})   # Finds meal table
meal = menuTable.findAll("tr")                              # Finds each seperate meal table (Bfast, Lunch, ect)

for meal in menuTable:                                      # For each item in the meal table, strip empty text
    text = meal.text.strip()                                # and save the menu item
    meal.string = re.sub(r"[\n][\W]+[^\w]", "\n", text)
print(meal.text)                                            # print out menu items

