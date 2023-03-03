import time, csv, os

from selenium import webdriver
from selenium.webdriver.chrome.service import Service

from selenium.webdriver.common.by import By

path = r"E:/chromedriver.exe"
baocun = './河北省科技成果转化'
if not os.path.exists(baocun):
    os.makedirs(baocun)
a, b = [], []
s = Service(executable_path=path)
driver = webdriver.Chrome(service=s)
driver.get('https://www.hbkjcg.cn/portal/sendPage/nyt/web/user/info/jsxm-list.jsp')
for i in range(1, 6):
    name = driver.find_elements(By.XPATH, "/html/body/div[3]/div[4]/ul/li/a/p[1]/span[1]")
    jianjie = driver.find_elements(By.XPATH, "/html/body/div[3]/div[4]/ul/li/a/p[2]")
    for j in name:
        a.append(j.text.replace("已发布", ''))
    for j in jianjie:
        b.append(j.text)
    time.sleep(1)
    next = driver.find_element(By.LINK_TEXT, "下一页")
    next.click()
    time.sleep(1)
for m in range(len(a)):
    with open("./河北省科技成果转化/" + a[m] + ".txt", 'a+', newline='', encoding='UTF-8') as f_c_csv:
        f_c_csv.write(b[m])
