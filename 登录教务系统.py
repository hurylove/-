from selenium.webdriver import Chrome
from chaojiying import Chaojiying_Client
from selenium.webdriver.common.by import By
import time

web = Chrome('C:\Program Files\Google\Chrome\Application\chromedriver.exe')
web.get('http://jwxt.cptc.cn/xtgl/login_slogin.html')

# 处理验证码
img = web.find_element(By.XPATH,'/html/body/div[1]/div[2]/div[2]/form/div/div/div[1]/div[3]/div[2]/img').screenshot_as_png
chaojiying = Chaojiying_Client('1469603831', 'tianjunmu2001', '929977')
dic = chaojiying.PostPic(img, 1902)
# print(dic)
# {'err_no': 0, 'err_str': 'OK', 'pic_id': '9150421376883800001', 'pic_str': 'bwcn', 'md5': '6ac8e38e0f7f894dd1dbc37e503a8cf1'}
verfy_code = dic['pic_str']

# 输入信息
web.find_element(By.XPATH,'/html/body/div[1]/div[2]/div[2]/form/div/div/div[1]/div[1]/div/input').send_keys('32002150128')
# time.sleep(2)
web.find_element(By.XPATH,'/html/body/div[1]/div[2]/div[2]/form/div/div/div[1]/div[2]/div/input[2]').send_keys('294714')
# time.sleep(2)
web.find_element(By.XPATH,'/html/body/div[1]/div[2]/div[2]/form/div/div/div[1]/div[3]/div[1]/input').send_keys(verfy_code)
# time.sleep(5)
# 点击登录
web.find_element(By.XPATH,'/html/body/div[1]/div[2]/div[2]/form/div/div/div[1]/div[5]/button').click()
time.sleep(2)
print('登录成功')