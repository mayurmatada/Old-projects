import selenium
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys 

path = 'C:\\Users\\Mayur\\source\\tools\\chromedriver'

webdrive = webdriver.Chrome(executable_path=path)

webdrive.get('https://www.google.com')

webdrive.maximize_window()

searchbar = webdrive.find_element_by_xpath('/html/body/div/div[4]/form/div[2]/div[1]/div[1]/div/div[2]/input')

searchbar.send_keys('p')
time.sleep(0.3)
searchbar.send_keys('u')
time.sleep(0.3)
searchbar.send_keys('p')
time.sleep(0.3)
searchbar.send_keys('p')
time.sleep(0.3)
searchbar.send_keys('i')
time.sleep(0.3)
searchbar.send_keys('e')
time.sleep(0.3)
searchbar.send_keys('s')
searchbar.send_keys(Keys.ENTER)

time.sleep(3)

images = webdrive.find_element_by_xpath('/html/body/div[7]/div[3]/div[5]/div/div/div[1]/div/div/div[1]/div/div[2]/a')

images.click()
k = 1

while True:
    pyautogui.press('down')
    time.sleep(2)




