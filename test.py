import csv, time, os

from selenium import webdriver
from selenium.webdriver.common.by import By

path = './代码'
if not os.path.exists(path):
    os.makedirs(path)
dirver = webdriver.Chrome("E:\chromedriver.exe")
dirver.get('https://www.runoob.com/python3/python3-upper-lower.html')
windows = dirver.window_handles
dirver.switch_to.window(windows[-1])
url, name = [], []
daima = dirver.find_elements(By.XPATH, "/html/body/div[4]/div/div[2]/div/div[3]/div/pre[1]")
for j in daima:
    print(j.text)