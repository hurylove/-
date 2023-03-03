import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

url = 'https://login.taobao.com/'
path = "C:\Program Files\Google\Chrome\Application\chromedriver.exe"
s = Service(executable_path=path)
browser = webdriver.Chrome(service=s)
browser.get(url)
browser.find_element(By.XPATH, "/html/body/div/div[2]/div[3]/div/div/div/div[2]/div/form/div[5]/a[2]").click()
time.sleep(5)
windows = browser.window_handles
browser.switch_to.window(windows[-1])

browser.find_element(By.XPATH, "/html/body/header/article/nav/div/div/form/div[2]/div/div/div/div/input").send_keys(
    "魁拔之书")
browser.find_element(By.XPATH, "/html/body/header/article/nav/div/div/form/div[1]/button").click()
