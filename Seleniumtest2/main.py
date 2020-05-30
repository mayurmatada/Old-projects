import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

path = 'C:\\Users\\Mayur\\source\\tools\\chromedriver'
url = 'https://www.google.com'

driver = webdriver.Chrome(executable_path=path)

driver.get(url=url)

search = '/html/body/div/div[4]/form/div[2]/div[1]/div[1]/div/div[2]/input'

searchbar = driver.find_element_by_xpath(search)

searchbar.send_keys('selenium for python')

searchbar.send_keys(Keys.ENTER)

url = '/html/body/div[7]/div[3]/div[10]/div[1]/div[2]/div/div[2]/div[2]/div/div/div[1]/div/div/div/div[1]/a/h3'

link = driver.find_element_by_link_text('Selenium with Python — Selenium Python Bindings 2 ...')
link.click()













