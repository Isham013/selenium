import time
import urllib
from selenium import webdriver
import requests
import io
import traceback

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

browser = webdriver.Chrome('/home/isham/Downloads/chromedriver')
browser.get("https://www.linkedin.com/uas/login")
files = open('con.txt')
lines = files.readlines()
username = lines[0]
password = lines[1]
elementID = browser.find_element("id", 'username')
elementID.send_keys(username)
elementID = browser.find_element("id", 'password')
elementID.send_keys(password)
elementID.submit()
time.sleep(100)
link = "https://www.linkedin.com/in/muhammed-anas-896a46169/"
# link = "https://www.linkedin.com/in/p-shalu-3b3b9615b/"
browser.get(link)
time.sleep(5)
# nav= browser.find_element("xpath","//*[@id='nav-settings__dropdown-trigger']/img[1]")
# nav.click()
#
#
# profile = browser.find_elementh("class_name","nav_settings__linkcard-link")
# profile.click()
# time.sleep(5)
# pic = browser.find_element("class_name","profile-photo-edit__preview")
# pic.click()

# with open('shalu.png','wb') as file:
# t = browser.find_element("xpath",'/html/body/div[5]/div[3]/div/div/div[2]/div/div/main/section[1]/div[2]/div[1]/div[1]/div/button/img').get_attribute('src')
# print(t)
# summary = browser.find_element("xpath", 'xpath=//section[@id=ember493]/div[3]/div/div/div/span').get_text('')
# print(browser.find_element(By.XPATH, "//section[@id='ember493']/div[3]/div/div/div/span]").get_text()
# t=(browser.find_element(By.XPATH, "//section[@id='ember493']/div[3]/div/div/div/span]")

#print(summary)
# # summary = browser.find_element("xpath",'/html/body/div[5]/div[3]/div/div/div/div[2]/div/div/main/section[2]/div[3]/div/div/div/span[1]').get_attribute("aria-hidden")
# print(summary)
#pageSource = browser.page_source
#fileToWrite = open("page_source.html", "w")
#fileToWrite.write(pageSource)

#     l = browser.find_element( by=By.xpath, value='//*[@alt]="P Shalu"')
    # l = browser.find_element("class_name","src")
    # l = elementID.get_attribute('img/src')
    # l = browser.find_element("xpath", '//*[@id="ember169"]')
# img_url = 'https://media-exp1.licdn.com/dms/image/D5603AQFFg9J8z_GXkg/profile-displayphoto-shrink_200_200/0/1667192149110?e=1672876800&v=beta&t=sK0aGjaUMRK7HdhyeGlIqSZI4H6C_qRFXdJsLJOvzA8'
#
# l = browser.find_element("xpath",'//*[@alt]="P Shalu"')
# img_url = t
# response = requests.get(img_url)
# if response.status_code:
#     fp = open('ansu', 'wb')
#     fp.write(response.content)
#     fp.close()

# images = browser.find_elements("tag_name",'img')
# # images = browser.img('img')
# for image in images:
#     print(image.get_attribute('src'))


browser.quit()
