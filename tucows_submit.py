import selenium
from selenium import webdriver

driver = webdriver.Chrome()
driver.get('https://login.hrwize.com/login')

# must be signed into google on your browser
google_login_button = driver.find_element_by_name('google')
google_login_button.click()

