import os

import requests
from selenium import webdriver
from selenium.webdriver.common.by import By

music = []
url = []
name = []
dirver = webdriver.Chrome("E:\chromedriver.exe")
dirver.get('https://music.163.com/artist?id=861777')

windows = dirver.window_handles
dirver.switch_to.window(windows[-1])
dirver.switch_to.frame("contentFrame")
music_id = dirver.find_elements(By.XPATH,
                                '/html/body/div[3]/div[1]/div/div/div[3]/div[2]/div/div/div/div[1]/table/tbody/tr/td[2]/div/div/div/span/a')
music_name = dirver.find_elements(By.XPATH,
                                  "/html/body/div[3]/div[1]/div/div/div[3]/div[2]/div/div/div/div[1]/table/tbody/tr/td[2]/div/div/div/span/a/b")
singer = dirver.find_element(By.XPATH, "/html/body/div[3]/div[1]/div/div/div[1]/div[1]/h2")
for i in music_id:
    music.append(i.get_attribute('href'))
for i in music:
    url.append('http://music.163.com/song/media/outer/url?id=' + i.split('=')[1])
for i in music_name:
    name.append(i.get_attribute('title').replace("\xa0", '').split('-')[0] + '-' + singer.text)
print(url)
print(name)
path = './' + singer.text
if not os.path.exists(path):
    os.makedirs(path)
for i in range(len(url)):
    music_url = requests.get(url[i]).content
    with open(r'./' + singer.text + "/" + name[i] + '.mp3', 'wb') as file:
        file.write(music_url)
    print("正在下载第" + str(i + 1) + "首:  " + name[i])
