import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path=r"C:\Users\orel.briga\Downloads\chromedriver_win32\chromedriver.exe")

driver.get("https://www.youtube.com/")

driver.find_element(by=By.XPATH, value='/html/body/ytd-app/div[1]/div/ytd-masthead/div[3]/div[2]/ytd-searchbox/form\
/div[1]/div[1]/input').send_keys('tell me why brooklyn 99')
time.sleep(5)
driver.find_element(by=By.XPATH, value='/html/body/ytd-app/div[1]/div/ytd-masthead/div[3]/div[2]/ytd-searchbox/\
button/yt-icon').click()
time.sleep(5)
driver.find_element(by=By.XPATH, value='/html/body/ytd-app/div[1]/ytd-page-manager/ytd-search/div[1]/ytd-two-column\
-search-results-renderer/div/ytd-section-list-renderer/div[2]/ytd-item-section-renderer/div[3]/ytd-video-\
renderer[1]/div[1]/div/div[1]/div/h3/a/yt-formatted-string').click()
time.sleep(5)
driver.find_element(by=By.XPATH, value='//*[@id="top-level-buttons-computed"]/ytd-toggle-button-renderer[1]/a').click()


