# /html/body/div[4]/div[3]/div/a
import time, csv, os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

from selenium.webdriver.common.by import By

path = r"E:/chromedriver.exe"
url, a, b, c, d, e = [], [], [], [], [], []
s = Service(executable_path=path)
driver = webdriver.Chrome(service=s)
driver.get('https://www.guahao.com/expert/all/%E5%85%A8%E5%9B%BD/all/%E4%B8%8D%E9%99%90')
wangye = driver.find_elements(By.XPATH, "/html/body/div[1]/div[2]/div[2]/div[1]/div[2]/ul/li/div[2]/a")
yiyuan = driver.find_elements(By.XPATH, "/html/body/div[1]/div[2]/div[2]/div[1]/div[2]/ul/li/div[1]/dl/dd/p[2]/span")
for i in wangye:
    url.append(i.get_attribute("href"))
for j in range(len(url)):
    driver.get(url[j])
    try:
        windows = driver.window_handles
        driver.switch_to.window(windows[-1])
        driver.find_element(By.XPATH, "/html/body/div[4]/div[3]/div/a").click()
        time.sleep(1)
        n = driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div/div[2]/div/div[1]/div[2]/h1/strong").text
        print(n)

    except:
        windows = driver.window_handles
        driver.switch_to.window(windows[-1])
        time.sleep(1)
        n = driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div/div[2]/div/div[1]/div[2]/h1/strong").text
        print(n)
