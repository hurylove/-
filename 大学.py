# coding=gbk
import csv
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
n=0
driver = webdriver.Chrome(r'e:chromedriver.exe')
driver.get('https://daxue.eol.cn/mingdan.shtml')
sleep(1)
windows = driver.window_handles
driver.switch_to.window(windows[-1])
sleep(1)
#/html/body/div[3]/div[2]/div[2]/div[2]/div/div[2]/a
urls = driver.find_elements(By.XPATH,'/html/body/div[3]/div[2]/div[2]/div[2]/div/div/a')
for url in urls:
    url.click()
    windows = driver.window_handles
    driver.switch_to.window(windows[-1])
    sleep(1)
    #/html/body/div[4]/div[2]/div[2]/table/tbody/tr[4]/td[2]
    #/html/body/div[4]/div[1]/span
    #/html/body/div[4]/div[1]/span
    #/html/body/div[4]/div[1]/span
    name = driver.find_elements(By.XPATH,'/html/body/div[4]/div[2]/div[2]/table/tbody/tr/td[2]')
    del name[0]
    xxbs = driver.find_elements(By.XPATH,'/html/body/div[4]/div[2]/div[2]/table/tbody/tr/td[3]')
    del xxbs[0]
    leader = driver.find_elements(By.XPATH,'/html/body/div[4]/div[2]/div[2]/table/tbody/tr/td[4]')
    del leader[0]
    where = driver.find_elements(By.XPATH,'/html/body/div[4]/div[2]/div[2]/table/tbody/tr/td[5]')
    del where[0]
    cengci = driver.find_elements(By.XPATH,'/html/body/div[4]/div[2]/div[2]/table/tbody/tr/td[6]')
    del cengci[0]
    for a, b, c, d, e  in zip(name,xxbs,leader,where,cengci):
        shengfen = driver.find_elements(By.XPATH, '/html/body/div[4]/div[1]/span')
        for i in shengfen:
            print(a.text, b.text, c.text, d.text, e.text,i.text)
            with open(r'大学.csv', 'a+', encoding='gbk',newline='') as f:
                writer=csv.writer(f)
                if n==0:
                    writer.writerow(['学校名称','学校标识码','主管部门','所在地','办学层次','省份'])
                    n=n+1
                content = str(a.text) + ',' + str(b.text) + ',' + str(c.text) + ',' + str(d.text) + ',' + str(e.text)+','+str(i.text) + '\n'
                f.write(content)

    driver.close()
    windows = driver.window_handles
    driver.switch_to.window(windows[-1])
    sleep(1)

driver.quit()

