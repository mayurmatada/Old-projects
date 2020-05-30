import selenium
from selenium import webdriver

path = 'C:\\Users\\Mayur\\source\\tools\\chromedriver'
webdrive = webdriver.Chrome(executable_path=path)
url = 'https://cookie.riimu.net/speed/'
webdrive.get(url)

button = webdrive.find_element_by_xpath('/html/body/div/div[2]/div[3]/div[1]/img')

while True:
    button.click()

