from selenium import webdriver
from bs4 import BeautifulSoup


driver = webdriver.Firefox()
driver.get('http://www.python.org')
html = driver.execute_script('return document.documentElement.outHTML')
sel_soup = BeautifulSoup(html, 'html.parser')

images = []
for s in sel_soup.findAll('img'):
  images.append(s)

print(images)