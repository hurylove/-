import time, csv, os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

from selenium.webdriver.common.by import By

path = r"E:/chromedriver.exe"
a, b,c,d,e = [], [],[],[],[]
s = Service(executable_path=path)
driver = webdriver.Chrome(service=s)
driver.get('https://www.guahao.com/expert/all/%E5%85%A8%E5%9B%BD/all/%E4%B8%8D%E9%99%90')
for i in range(1,6):
    name=driver.find_elements(By.XPATH,"/html/body/div[1]/div[2]/div[2]/div[1]/div[2]/ul/li/div[2]/a")
    zhicheng=driver.find_elements(By.XPATH,"/html/body/div[1]/div[2]/div[2]/div[1]/div[2]/ul/li/div[1]/dl/dt")
    danwei=driver.find_elements(By.XPATH,"/html/body/div[1]/div[2]/div[2]/div[1]/div[2]/ul/li/div[1]/dl/dd/p[2]/span")
    wenz=driver.find_elements(By.XPATH,"/html/body/div[1]/div[2]/div[2]/div[1]/div[2]/ul/li/div[1]/dl/dd/p[3]/span[2]/i")
    shanchang=driver.find_elements(By.XPATH,"/html/body/div[1]/div[2]/div[2]/div[1]/div[2]/ul/li/div[2]/div[1]/p")
    for j in name:
        a.append(j.text)
    for j in range(len(zhicheng)):
        b.append(zhicheng[j].text.replace(name[j].text," ").replace("    ",""))
    for j in danwei:
        c.append(j.text)
    for j in wenz:
        d.append(j.text)
    for j in shanchang:
        e.append(j.text)
    next = driver.find_element(By.LINK_TEXT, ">")
    next.click()
    time.sleep(1)

    #/html/body/div[1]/div[2]/div[2]/div[1]/div[3]/div/form/div[1]/a[6]
with open("微医网.csv", 'a+', newline='', encoding='UTF-8') as f_c_csv:
    writer = csv.writer(f_c_csv)
    writer.writerow(
        ['名字', '职称', '单位', '问诊量', "擅长"])
    for nl in zip(a, b, c, d, e, ):
        print(nl)
        writer.writerow(nl)