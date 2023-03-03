import time, csv, os

from selenium import webdriver

from selenium.webdriver.common.by import By

dirver = webdriver.Chrome("E:\chromedriver.exe")
dirver.get('https://www.shanghairanking.cn/')
windows = dirver.window_handles
dirver.switch_to.window(windows[-1])
a = []
b = []
c = []
d = []
num_1 = dirver.find_element(By.XPATH, "/html/body/div/div/div/div[2]/div[2]/div/div[3]/div[2]/a/div[1]/span").click()
windows = dirver.window_handles
dirver.switch_to.window(windows[-1])
time.sleep(1)
zhuanye = dirver.find_element(By.XPATH, "/html/body/div/div/div/div[2]/div[2]/div[1]/div[8]/div[2]/div[12]/a").click()
windows = dirver.window_handles
dirver.switch_to.window(windows[-1])
time.sleep(1)
for i in range(0, 5):
    paiming_2021 = dirver.find_elements(By.XPATH,
                                        '/html/body/div/div/div/div[2]/div/div[2]/div[2]/div[1]/div/div[2]/table/tbody/tr/td[1]/div')
    paiming_2020 = dirver.find_elements(By.XPATH,
                                        '/html/body/div/div/div/div[2]/div/div[2]/div[2]/div[1]/div/div[2]/table/tbody/tr/td[2]/span')
    name = dirver.find_elements(By.XPATH,
                                '/html/body/div/div/div/div[2]/div/div[2]/div[2]/div[1]/div/div[2]/table/tbody/tr/td[4]/div')
    num = dirver.find_elements(By.XPATH,
                               '/html/body/div/div/div/div[2]/div/div[2]/div[2]/div[1]/div/div[2]/table/tbody/tr/td[5]')
    for j in paiming_2021:
        a.append(j.text)
    for j in paiming_2020:
        b.append(j.text)
    for j in name:
        c.append(j.text)
    for j in num:
        d.append(j.text)
    next = dirver.find_element(By.XPATH, "/html/body/div/div/div/div[2]/div/div[2]/div[2]/div[1]/div/ul/li[7]/a")
    next.click()
    windows = dirver.window_handles
    dirver.switch_to.window(windows[-1])
    time.sleep(1)
with open("大学学科排名.csv", 'a+', newline='', encoding='UTF-8') as f_c_csv:
    writer = csv.writer(f_c_csv)
    writer.writerow(
        ['2021年排名','2020年排名','学校名称','总分'])
    for nl in zip(a, b, c, d):
        print(nl)
        writer.writerow(nl)
