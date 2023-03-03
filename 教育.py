import time, csv

from selenium import webdriver

from selenium.webdriver.common.by import By



with open("教育.csv", 'a+', newline='', encoding='UTF-8') as f_c_csv:
    writer = csv.writer(f_c_csv)
    writer.writerow(["学校名称", "学校标识码", "主管部门", "所在地", "办学层次", '所在省'])

dirver = webdriver.Chrome("E:\chromedriver.exe")
dirver.get('https://daxue.eol.cn/mingdan.shtml')
windows = dirver.window_handles
dirver.switch_to.window(windows[-1])
school = dirver.find_elements(By.XPATH, "/html/body/div[3]/div[2]/div[2]/div[2]/div/div/a")
for i in range(len(school)):
    a = []
    b = []
    c = []
    d = []
    e = []
    f = []
    school[i].click()
    shengfeng=school[i].text
    windows = dirver.window_handles
    dirver.switch_to.window(windows[-1])
    name = dirver.find_elements(By.XPATH, "/html/body/div[4]/div[2]/div[2]/table/tbody/tr/td[2]")
    del (name[0])
    xxbs = dirver.find_elements(By.XPATH, "/html/body/div[4]/div[2]/div[2]/table/tbody/tr/td[3]")
    del (xxbs[0])
    zgbm = dirver.find_elements(By.XPATH, "/html/body/div[4]/div[2]/div[2]/table/tbody/tr/td[4]")
    del (zgbm[0])
    szd = dirver.find_elements(By.XPATH, "/html/body/div[4]/div[2]/div[2]/table/tbody/tr/td[5]")
    del (szd[0])
    bxcc = dirver.find_elements(By.XPATH, "/html/body/div[4]/div[2]/div[2]/table/tbody/tr/td[6]")
    del (bxcc[0])
    for j in name:
        a.append(j.text)
    for j in xxbs:
        b.append(j.text)
    for j in zgbm:
        c.append(j.text)
    for j in szd:
        d.append(j.text)
    for j in bxcc:
        e.append(j.text)
    for j in range(len(name)):
        f.append(shengfeng)
    dirver.close()
    windows = dirver.window_handles
    dirver.switch_to.window(windows[-1])
    with open("教育.csv", 'a+', newline='', encoding='UTF-8') as f_c_csv:
        writer = csv.writer(f_c_csv)
        for nl in zip(a, b, c, d, e,f):
            writer.writerow(nl)
