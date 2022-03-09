"""
Created 2/24/2022
@author: Ralph Miller
         Nils Brown
"""
import sys
import re
import unicodedata
from bs4 import BeautifulSoup
from selenium import webdriver
from dbsetup import createMenuDB, addMenuItem, findMenuItem

# Uses headless browser to grab HTML of specific DH menu #
driver = webdriver.Chrome()
driver.get('https://nutrition.sa.ucsc.edu/')
driver.find_element_by_link_text("College Nine/John R. Lewis Dining Hall").click()
pageSource = driver.page_source
soup = BeautifulSoup(pageSource, 'html.parser')
driver.close()

# Parses HTML with bs4 and find all menu items #
menuTable = soup.find('table',  {'bordercolor': '#CCC'})   # Finds meal table
meal = menuTable.findAll("tr")                              # Finds each seperate meal table (Bfast, Lunch, ect)

for meal in menuTable:                                      # For each item in the meal table, strip empty text
    text = meal.text.strip()                                # and save the menu item
    meal.string = re.sub(r"[\n][\W]+[^\w]", "\n", text)
#print(meal.text)                                            # print out menu items

# split by newline to get each line
#remove \xa0 from string
cleaned = unicodedata.normalize("NFKD", meal.text)
arr = cleaned.split("\n")
print(arr)
sys.exit()
# parse the list line by line and add to database
mealtime = ""
for i in arr:
    # move past "Nutrition Calculator" stuff and headers
    if i == "Nutrition Calculator" or "--" in i:
        continue

    # get the meal time (bfast, lunch, etc)
    if i == "Breakfast":
        mealtime = "Breakfast"
    if i == "Lunch":
        mealtime = "Lunch"
    if i == "Dinner":
        mealtime = "Dinner"
    if i == "Late Night":
        mealtime = "Late Night"

    #  if at this point, add to the database
    addMenuItem("1/1/2022", "college910", i, mealtime)