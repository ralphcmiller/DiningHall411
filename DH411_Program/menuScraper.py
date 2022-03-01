"""
Created 2/24/2022
@author: Ralph Miller
"""
from bs4 import BeautifulSoup
from selenium import webdriver
driver = webdriver.Chrome()
driver.get('https://nutrition.sa.ucsc.edu/')
driver.find_element_by_link_text("Colleges Nine & Lewis Dining Hall").click()
pageSource = driver.page_source
soup = BeautifulSoup(pageSource, 'html.parser')
driver.close()

for meal in soup.find_all('div', attrs={"class":"shortmenumeals"}):
    print(meal)
    for item in soup.find_all('div', attrs={"class":"shortmenurecipes"}):
        print(item.text)
    print(" ")
