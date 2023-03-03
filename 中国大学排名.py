import csv
import time

from selenium import webdriver
from selenium.webdriver.common.by import By

dirver = webdriver.Chrome("C:\Program Files\Google\Chrome\Application\chromedriver.exe")
dirver.get('https://www.shanghairanking.cn/')
windows = dirver.window_handles
dirver.switch_to.window(windows[-1])
a = []
b = []
c = []
d = []
e = []
f = []
num_1 = dirver.find_element(By.XPATH, "/html/body/div/div/div/div[2]/div[2]/div/div[2]/div[2]/a/div[1]/span").click()
windows = dirver.window_handles
dirver.switch_to.window(windows[-1])
time.sleep(1)
for i in range(1, 21):
    paiming = dirver.find_elements(By.XPATH,
                                   "/html/body/div/div/div/div[2]/div/div[3]/div[2]/div[1]/div/div[2]/table/tbody/tr/td[1]/div")
    name = dirver.find_elements(By.XPATH,
                                "/html/body/div/div/div/div[2]/div/div[3]/div[2]/div[1]/div/div[2]/table/tbody/tr/td[2]/div/div[2]/div[1]/div/div/a")
    add = dirver.find_elements(By.XPATH,
                               "/html/body/div/div/div/div[2]/div/div[3]/div[2]/div[1]/div/div[2]/table/tbody/tr/td[3]")
    leixing = dirver.find_elements(By.XPATH,
                                   "/html/body/div/div/div/div[2]/div/div[3]/div[2]/div[1]/div/div[2]/table/tbody/tr/td[4]")
    zongfen = dirver.find_elements(By.XPATH,
                                   "/html/body/div/div/div/div[2]/div/div[3]/div[2]/div[1]/div/div[2]/table/tbody/tr/td[5]")
    chengci = dirver.find_elements(By.XPATH,
                                   "/html/body/div/div/div/div[2]/div/div[3]/div[2]/div[1]/div/div[2]/table/tbody/tr/td[6]")
    for j in paiming:
        a.append(j.text)
    for j in name:
        b.append(j.text)
    for j in add:
        c.append(j.text)
    for j in leixing:
        d.append(j.text)
    for j in zongfen:
        e.append(j.text)
    for j in chengci:
        f.append(j.text)
    ##content-box > ul > li.ant-pagination-next > a
    ##content-box > ul > li.ant-pagination-next > a
    next = dirver.find_element(By.CSS_SELECTOR, "#content-box > ul > li.ant-pagination-next > a").click()
    windows = dirver.window_handles
    dirver.switch_to.window(windows[-1])
    time.sleep(1)
with open("大学排名.csv", 'a+', newline='', encoding='UTF-8') as f_c_csv:
    writer = csv.writer(f_c_csv)
    writer.writerow(
        ['排名', '名称', '省市', '类型', "总分", "办学层次"])
    for nl in zip(a, b, c, d, e, f):
        print(nl)
        writer.writerow(nl)
