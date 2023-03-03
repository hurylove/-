import time, csv, os

from selenium import webdriver
from selenium.webdriver.chrome.service import Service

from selenium.webdriver.common.by import By

path = r"E:/chromedriver.exe"
a, b = [], []
s = Service(executable_path=path)
driver = webdriver.Chrome(service=s)
driver.get('https://cgk.kxjs.tj.gov.cn/navigation.do')
time.sleep(1)
driver.find_element(By.XPATH,"/html/body/div/div/div[3]/div[1]/div/ul/li[7]/a").click()
windows = driver.window_handles
driver.switch_to.window(windows[-1])
time.sleep(1)
for i in range(1, 6):
    name = driver.find_elements(By.XPATH, "/html/body/div/div/div[3]/div[2]/table/tbody/tr/td[1]/a")
    riq = driver.find_elements(By.XPATH, "/html/body/div/div/div[3]/div[2]/table/tbody/tr/td[2]")
    for j in name:
        a.append(j.text.replace("已发布", ''))
    for j in riq:
        b.append(j.text)
    time.sleep(1)
    next = driver.find_element(By.LINK_TEXT, "下一页")
    next.click()
    time.sleep(1)
with open("天津省科技信息.csv", 'a+', newline='', encoding='UTF-8') as f_c_csv:
    writer = csv.writer(f_c_csv)
    writer.writerow(
        ['项目名称','结项日期'])
    for nl in zip(a, b):
        print(nl)
        writer.writerow(nl)
