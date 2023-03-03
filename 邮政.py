import time,csv

from selenium import webdriver

from selenium.webdriver.common.by import By

dirver = webdriver.Chrome("E://chromedriver.exe")
dirver.get('http://iframe.chinapost.com.cn/jsp/type/institutionalsite/SiteSearchJT.jsp?community=ChinaPostJT&pos=0')
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
for i in range(0,3):
    sheng=dirver.find_elements(By.XPATH,'/html/body/table/tbody/tr/td[1]')
    del(sheng[0])
    shi=dirver.find_elements(By.XPATH,'/html/body/table/tbody/tr/td[2]')
    del(shi[0])
    xian=dirver.find_elements(By.XPATH,'/html/body/table/tbody/tr/td[3]')
    del(xian[0])
    wangdian=dirver.find_elements(By.XPATH,'/html/body/table/tbody/tr/td[4]')
    del(wangdian[0])
    youbian=dirver.find_elements(By.XPATH,'/html/body/table/tbody/tr/td[5]')
    del(youbian[0])
    add=dirver.find_elements(By.XPATH,'/html/body/table/tbody/tr/td[6]')
    del(add[0])
    yewu=dirver.find_elements(By.XPATH,'/html/body/table/tbody/tr/td[7]')
    del(yewu[0])
    dianhua=dirver.find_elements(By.XPATH,'/html/body/table/tbody/tr/td[8]')
    del(dianhua[0])
    for j in sheng:
        a.append(j.text)
    for j in shi:
        b.append(j.text)
    for j in xian:
        c.append(j.text)
    for j in wangdian:
        d.append(j.text)
    for j in youbian:
        e.append(j.text)
    for j in add:
        f.append(j.text)
    for j in yewu:
        g.append(j.text)
    for j in dianhua:
        h.append(j.text)
    next=dirver.find_element(By.LINK_TEXT,"下一页")
    next.click()
    time.sleep(1)
with open("邮政.csv", 'a+', newline='', encoding='UTF-8') as f_c_csv :
    writer = csv.writer(f_c_csv)
    writer.writerow(['省', '市', '县', '服务网点名称', '邮编','地址','是否办理金融业务','电话'])
    for nl in zip(a,b,c,d,e,f,g,h):
        writer.writerow(nl)
print('写入完成')