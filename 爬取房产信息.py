import time,csv

from selenium import webdriver

from selenium.webdriver.common.by import By

with open("房产.csv", 'a+', newline='', encoding='UTF-8') as f_c_csv :
    writer = csv.writer(f_c_csv)
    writer.writerow(['标题','小区名', '面积', '总价','单价'])
#chromedriver.exe
url='https://sjz.ke.com/ershoufang/yuhua1/pg1/'
dirver = webdriver.Chrome("C:\Program Files\Google\Chrome\Application\chromedriver.exe")
dirver.get(url)
windows=dirver.window_handles
dirver.switch_to.window(windows[-1])
a=[]
b=[]
c=[]
d=[]
e=[]
for i in range(0,17):
    home=dirver.find_elements(By.XPATH,'/html/body/div[1]/div[4]/div[1]/div[4]/ul/li/div/div[1]/a')
    for j in home:
        j.click()
        windows = dirver.window_handles
        dirver.switch_to.window(windows[-1])
        name=dirver.find_element(By.XPATH,'/html/body/div[1]/div[4]/div[1]/div[2]/div[4]/div[1]/a[1]')
        mj=dirver.find_element(By.XPATH,'/html/body/div[1]/div[4]/div[1]/div[2]/div[3]/div[3]/div[1]')
        zj=dirver.find_element(By.XPATH,'/html/body/div[1]/div[4]/div[1]/div[2]/div[2]/div/span[1]')
        dj=dirver.find_element(By.XPATH,'/html/body/div[1]/div[4]/div[1]/div[2]/div[2]/div/div[1]/div[1]/span')
        bt=dirver.find_element(By.XPATH,'/html/body/div[1]/div[2]/div[2]/div/div/div[1]/h1')
        e.append(bt.text)
        a.append(name.text)
        b.append(mj.text)
        c.append(zj.text+'万')
        d.append(dj.text+'元/平米')
        dirver.close()
        windows = dirver.window_handles
        dirver.switch_to.window(windows[-1])
        time.sleep(1)
    next=dirver.find_element(By.LINK_TEXT,"下一页")
    next.click()
print(e,a,b,c,d)
for m in range(len(e)):
    with open("房产.csv", 'a+', newline='', encoding='UTF-8') as f_c_csv :
        content=str(e[m])+str(a[m])+str(b[m])+str(c[m])+str(d[m])+'\n'
        f_c_csv.write(content)
print("写入完成！")

#链家
dirver.get('https://sjz.lianjia.com/ershoufang/yuhua1/pg1/')
windows=dirver.window_handles
dirver.switch_to.window(windows[-1])
a=[]
b=[]
c=[]
d=[]
e=[]
for i in range(0,17):
    home=dirver.find_elements(By.XPATH,'/html/body/div[4]/div[1]/ul/li/div[1]/div[1]/a')
    #/html/body/div[4]/div[1]/ul/li[1]/div[1]/div[1]/a
    #/html/body/div[4]/div[1]/ul/li/div[1]/div[1]/a
    for j in home:
        j.click()
        windows = dirver.window_handles
        dirver.switch_to.window(windows[-1])
        name=dirver.find_element(By.XPATH,'/html/body/div[5]/div[2]/div[5]/div[1]/a[1]')
        mj=dirver.find_element(By.XPATH,'/html/body/div[5]/div[2]/div[4]/div[3]/div[1]')
        zj=dirver.find_element(By.XPATH,'/html/body/div[5]/div[2]/div[3]/div/span[1]')
        dj=dirver.find_element(By.XPATH,'/html/body/div[5]/div[2]/div[3]/div/div[1]/div[1]/span')
        bt=dirver.find_element(By.XPATH,'/html/body/div[3]/div/div/div[1]/h1')
        e.append(bt.text)
        a.append(name.text)
        b.append(mj.text)
        c.append(zj.text+'万')
        d.append(dj.text)
        dirver.close()
        windows = dirver.window_handles
        dirver.switch_to.window(windows[-1])
        time.sleep(1)
    next=dirver.find_element(By.LINK_TEXT,"下一页")
    next.click()
print(e,a,b,c,d)
for m in range(len(e)):
    with open("房产.csv", 'a+', newline='', encoding='UTF-8') as f_c_csv :
        content=str(e[m])+str(a[m])+str(b[m])+str(c[m])+str(d[m])+'\n'
        f_c_csv.write(content)
print("写入完成！")