import csv,time,os

from selenium import webdriver
from selenium.webdriver.common.by import By

path = './代码'
if not os.path.exists(path):
    os.makedirs(path)
dirver = webdriver.Chrome("C:\Program Files\Google\Chrome\Application\chromedriver.exe")
dirver.get('https://www.runoob.com/python3/python3-examples.html')
windows = dirver.window_handles
dirver.switch_to.window(windows[-1])
url, name = [], []
wangye=dirver.find_elements(By.XPATH,"/html/body/div[4]/div/div[2]/div/div[3]/div/ul/li/a")
for i in wangye:
    url.append(i.get_attribute("href"))
    name.append(i.text.replace("/", ' '))
for i in range(len(url)):
    dirver.get(url[i])
    windows = dirver.window_handles
    dirver.switch_to.window(windows[-1])
    time.sleep(1)
    if name[i] == 'Python 字符串大小写转换':
        daima = dirver.find_elements(By.XPATH, "/html/body/div[4]/div/div[2]/div/div[3]/div/pre[1]")
    else:
        daima = dirver.find_elements(By.XPATH, "/html/body/div[4]/div/div[2]/div/div[3]/div/div/div")
    for j in daima:
        print(j.text)
        with open('./代码/'+name[i]+'.py', 'w', encoding='utf-8') as f:
            f.write(j.text)