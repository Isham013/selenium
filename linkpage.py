import time
from selenium import webdriver
driver = webdriver.Chrome('/home/isham/Downloads/chromedriver')  # Optional argument, if not specified will search path.
driver.get('https://www.linkedin.com')
time.sleep(5) # Let the user actually see something!
# time.sleep(25) # Let the user actually see something!

driver.quit()

