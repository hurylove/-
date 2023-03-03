import time, csv

from selenium import webdriver

from selenium.webdriver.common.by import By


dirver = webdriver.Chrome("E:/chromedriver.exe")
dirver.get('http://kaijiang.zhcw.com/zhcw/html/ssq/list.html')
windows = dirver.window_handles
dirver.switch_to.window(windows[-1])
for i in range(1, 6):
    shijian, qihao, haoma, xiaoshoue, one, two = [], [], [], [], [], []
    a = dirver.find_elements(By.XPATH, "/html/body/table/tbody/tr/td[1]")
    b = dirver.find_elements(By.XPATH, "/html/body/table/tbody/tr/td[2]")
    c = dirver.find_elements(By.XPATH, "/html/body/table/tbody/tr/td[3]")
    d = dirver.find_elements(By.XPATH, "/html/body/table/tbody/tr/td[4]")
    e = dirver.find_elements(By.XPATH, "/html/body/table/tbody/tr/td[5]")
    f = dirver.find_elements(By.XPATH, "/html/body/table/tbody/tr/td[6]")
    for j in a:
        shijian.append(j.text)
    for j in b:
        qihao.append(j.text)
    for j in c:
        haoma.append(j.text.replace("\n", ' '))
    for j in d:
        xiaoshoue.append(j.text)
    for j in e:
        one.append(j.text)
    for j in f:
        two.append(j.text)
    next = dirver.find_element(By.LINK_TEXT, "下一页")
    next.click()
    time.sleep(1)
    with open("双色球第"+str(i)+"页.csv", 'a+', newline='', encoding='UTF-8') as f_c_csv:
        writer = csv.writer(f_c_csv)
        writer.writerow(
            ['开奖日期', '期号', '中奖号码', '销售额', '一等奖', '二等奖'])
        for nl in zip(shijian, qihao, haoma, xiaoshoue, one, two):
            print(nl)
            writer.writerow(nl)
