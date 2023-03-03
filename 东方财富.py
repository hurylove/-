import time,csv

from selenium import webdriver

from selenium.webdriver.common.by import By

dirver = webdriver.Chrome("E:\chromedriver.exe")
dirver.get('https://data.eastmoney.com/bbsj/202203/yjbb.html')
windows=dirver.window_handles
dirver.switch_to.window(windows[-1])
a=[]
b=[]
c=[]
d=[]
e=[]
f=[]
g=[]
h=[]
n=[]
m=[]
for i in range(0,20):
    print('第',i+1,'页开始爬取')
    daima=dirver.find_elements(By.XPATH,"/html/body/div[1]/div[8]/div[2]/div[8]/div[2]/div[2]/table/tbody/tr/td[2]")
    name=dirver.find_elements(By.XPATH,"/html/body/div[1]/div[8]/div[2]/div[8]/div[2]/div[2]/table/tbody/tr/td[3]")
    xiangguan=dirver.find_elements(By.XPATH,"/html/body/div[1]/div[8]/div[2]/div[8]/div[2]/div[2]/table/tbody/tr/td[4]/a")
    shouyi=dirver.find_elements(By.XPATH,"/html/body/div[1]/div[8]/div[2]/div[8]/div[2]/div[2]/table/tbody/tr/td[5]")
    yyzsr=dirver.find_elements(By.XPATH,"/html/body/div[1]/div[8]/div[2]/div[8]/div[2]/div[2]/table/tbody/tr/td[6]")
    tbzz_y=dirver.find_elements(By.XPATH,"/html/body/div[1]/div[8]/div[2]/div[8]/div[2]/div[2]/table/tbody/tr/td[7]")
    jdhbzz_y=dirver.find_elements(By.XPATH,"/html/body/div[1]/div[8]/div[2]/div[8]/div[2]/div[2]/table/tbody/tr/td[8]")
    jlr=dirver.find_elements(By.XPATH,"/html/body/div[1]/div[8]/div[2]/div[8]/div[2]/div[2]/table/tbody/tr/td[9]")
    tbzz_j=dirver.find_elements(By.XPATH,"/html/body/div[1]/div[8]/div[2]/div[8]/div[2]/div[2]/table/tbody/tr/td[10]")
    jdhbzz_j=dirver.find_elements(By.XPATH,"/html/body/div[1]/div[8]/div[2]/div[8]/div[2]/div[2]/table/tbody/tr/td[11]")
    print('第',i+1,'页爬取成功')
    print('第',i+1,'页开始存入')
    for j in daima:
        a.append(j.text)
    for j in name:
        b.append(j.text)
    for j in xiangguan:
        c.append(j.get_attribute('href'))
    for j in shouyi:
        d.append(j.text)
    for j in yyzsr:
        e.append(j.text)
    for j in tbzz_y:
        f.append(j.text)
    for j in jdhbzz_y:
        g.append(j.text)
    for j in jlr:
        h.append(j.text)
    for j in tbzz_j:
        n.append(j.text)
    for j in jdhbzz_j:
        m.append(j.text)
    print('第',i+1,'页存入成功')
    next=dirver.find_element(By.LINK_TEXT,"下一页")
    next.click()
    time.sleep(1)
with open("东方财富.csv", 'a+', newline='', encoding='UTF-8') as f_c_csv :
    writer = csv.writer(f_c_csv)
    writer.writerow(['股票代码', '股票简称', '相关', '每股收益（元）', '营业总收入（元）', '同比增长（%）', '季度环比增长（%）', '净利润（元）', '同比增长（%）','季度环比增长（%）'])
    for nl in zip(a,b,c,d,e,f,g,h,n,m,):
        writer.writerow(nl)
