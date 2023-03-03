import time, csv

from selenium import webdriver
from selenium.webdriver.chrome.service import Service

from selenium.webdriver.common.by import By

path = r"E:/chromedriver.exe"
a, b ,c,d= [], [],[],[]
s = Service(executable_path=path)
driver = webdriver.Chrome(service=s)
driver.get('https://ys.endata.cn/BoxOffice/Ranking')
time.sleep(1)
#内地票房
name=driver.find_elements(By.XPATH,"/html/body/section/section/main/div/div[1]/div/section/section/section/section/div[1]/div[3]/table/tbody/tr/td[2]/div/label/data")
date=driver.find_elements(By.XPATH,"/html/body/section/section/main/div/div[1]/div/section/section/section/section/div[1]/div[3]/table/tbody/tr/td[3]/div/label")
piaofang=driver.find_elements(By.XPATH,"/html/body/section/section/main/div/div[1]/div/section/section/section/section/div[1]/div[3]/table/tbody/tr/td[4]/div/label")
piaojia=driver.find_elements(By.XPATH,"/html/body/section/section/main/div/div[1]/div/section/section/section/section/div[1]/div[3]/table/tbody/tr/td[5]/div/label")
for i in name:
    a.append(i.text)
for i in date:
    b.append(i.text)
for i in piaofang:
    c.append(i.text)
for i in piaojia:
    d.append(i.text)
with open("内地票房.csv", 'a+', newline='', encoding='UTF-8') as f_c_csv:
    writer = csv.writer(f_c_csv)
    writer.writerow(
        ['电影名称','上映日期','累计票房','平均票价'])
    for nl in zip(a, b,c,d):
        print(nl)
        writer.writerow(nl)
#单日票房
a, b ,c,d= [], [],[],[]
driver.find_element(By.XPATH,'/html/body/section/section/main/div/div[1]/div/section/section/div/div[1]/div/div/div/div[2]/span').click()
time.sleep(1)
name=driver.find_elements(By.XPATH,"/html/body/section/section/main/div/div[1]/div/section/section/section/section/div[1]/div[3]/table/tbody/tr/td[2]/div/label/data")
date=driver.find_elements(By.XPATH,"/html/body/section/section/main/div/div[1]/div/section/section/section/section/div[1]/div[3]/table/tbody/tr/td[3]/div/label")
piaofang=driver.find_elements(By.XPATH,"/html/body/section/section/main/div/div[1]/div/section/section/section/section/div[1]/div[3]/table/tbody/tr/td[4]/div/label")
for i in name:
    a.append(i.text)
for i in date:
    b.append(i.text)
for i in piaofang:
    c.append(i.text)
with open("单日票房.csv", 'a+', newline='', encoding='UTF-8') as f_c_csv:
    writer = csv.writer(f_c_csv)
    writer.writerow(
        ['电影名称','上映日期','单日票房'])
    for nl in zip(a, b,c):
        print(nl)
        writer.writerow(nl)
#单月票房
a, b ,c,d= [], [],[],[]
driver.find_element(By.XPATH,'/html/body/section/section/main/div/div[1]/div/section/section/div/div[1]/div/div/div/div[3]/span').click()
time.sleep(1)
name=driver.find_elements(By.XPATH,"/html/body/section/section/main/div/div[1]/div/section/section/section/section/div[1]/div[3]/table/tbody/tr/td[2]/div/label/data")
date=driver.find_elements(By.XPATH,"/html/body/section/section/main/div/div[1]/div/section/section/section/section/div[1]/div[3]/table/tbody/tr/td[3]/div/label")
piaofang=driver.find_elements(By.XPATH,"/html/body/section/section/main/div/div[1]/div/section/section/section/section/div[1]/div[3]/table/tbody/tr/td[4]/div/label")
yuefen=driver.find_elements(By.XPATH,"/html/body/section/section/main/div/div[1]/div/section/section/section/section/div[1]/div[3]/table/tbody/tr/td[5]/div/label")
for i in name:
    a.append(i.text)
for i in date:
    b.append(i.text)
for i in piaofang:
    c.append(i.text)
for i in yuefen:
    d.append(i.text)
with open("单月票房.csv", 'a+', newline='', encoding='UTF-8') as f_c_csv:
    writer = csv.writer(f_c_csv)
    writer.writerow(
        ['电影名称','上映日期','单月票房','月份'])
    for nl in zip(a, b,c,d):
        print(nl)
        writer.writerow(nl)