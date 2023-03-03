import time, csv

from selenium import webdriver

from selenium.webdriver.common.by import By

dirver = webdriver.Chrome("E:/chromedriver.exe")
dirver.get('http://quote.eastmoney.com/center/gridlist.html#hs_a_board')
windows = dirver.window_handles
dirver.switch_to.window(windows[-1])
a = []
b = []
c = []
d = []
e = []
f = []
g = []
h = []
n = []
m = []
y = []
for i in range(0, 5):
    daima = dirver.find_elements(By.XPATH, "/html/body/div[1]/div[2]/div[2]/div[5]/div/table/tbody/tr/td[2]/a")
    nc = dirver.find_elements(By.XPATH, "/html/body/div[1]/div[2]/div[2]/div[5]/div/table/tbody/tr/td[3]/a")
    newjiage = dirver.find_elements(By.XPATH, "/html/body/div[1]/div[2]/div[2]/div[5]/div/table/tbody/tr/td[5]")
    zdf = dirver.find_elements(By.XPATH, "/html/body/div[1]/div[2]/div[2]/div[5]/div/table/tbody/tr/td[6]")
    zde = dirver.find_elements(By.XPATH, "/html/body/div[1]/div[2]/div[2]/div[5]/div/table/tbody/tr/td[7]")
    cjl = dirver.find_elements(By.XPATH, "/html/body/div[1]/div[2]/div[2]/div[5]/div/table/tbody/tr/td[8]")
    cle = dirver.find_elements(By.XPATH, "/html/body/div[1]/div[2]/div[2]/div[5]/div/table/tbody/tr/td[9]")
    zf = dirver.find_elements(By.XPATH, "/html/body/div[1]/div[2]/div[2]/div[5]/div/table/tbody/tr/td[10]")
    zg = dirver.find_elements(By.XPATH, "/html/body/div[1]/div[2]/div[2]/div[5]/div/table/tbody/tr/td[11]")
    zd = dirver.find_elements(By.XPATH, '/html/body/div[1]/div[2]/div[2]/div[5]/div/table/tbody/tr/td[12]')
    jk = dirver.find_elements(By.XPATH, '/html/body/div[1]/div[2]/div[2]/div[5]/div/table/tbody/tr/td[13]')
    for j in daima:
        a.append(j.text)
    for j in nc:
        b.append(j.text)
    for j in newjiage:
        c.append(j.get_attribute('href'))
    for j in zdf:
        d.append(j.text)
    for j in zde:
        e.append(j.text)
    for j in cjl:
        f.append(j.text)
    for j in cle:
        g.append(j.text)
    for j in zf:
        h.append(j.text)
    for j in zg:
        n.append(j.text)
    for j in zd:
        m.append(j.text)
    for j in jk:
        y.append(j.text)
    next = dirver.find_element(By.LINK_TEXT, "下一页")
    next.click()
    time.sleep(1)
with open("沪深京A股.csv", 'a+', newline='', encoding='UTF-8') as f_c_csv:
    writer = csv.writer(f_c_csv)
    writer.writerow(
        ['代码', '名称', '最新价', '涨跌幅', '涨跌额', '成交量（手）', '成交额', '振幅', '最高', '最低','今开'])
    for nl in zip(a, b, c, d, e, f, g, h, n, m,y ):
        print(nl)
        writer.writerow(nl)
