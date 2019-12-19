from selenium import webdriver
from selenium.webdriver.common.keys import Keys
# import bs4
# soup = bs4.BeautifulSoup()
# from bs4 import BeauifulSoup
# soup = BeautifulSoup()

path = './chromedriver.exe'
driver = webdriver.Chrome(path)
driver.get('https://www.google.com/')
search_input = driver.find_element_by_css_selector('#tsf > div:nth-child(2) > div.A8SBwf > div.RNNXgb > div > div.a4bIc > input')
search_input.send_keys('소리나래')
search_input.send_keys(Keys.ENTER)