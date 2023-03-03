from selenium.webdriver import Chrome
from chaojiying import Chaojiying_Client
import time

web = Chrome()
web.get('http://www.chaojiying.com/user/login/')

# 处理验证码
img = web.find_element_by_xpath('/html/body/div[3]/div/div[3]/div[1]/form/div/img').screenshot_as_png
chaojiying = Chaojiying_Client('1469603831', 'tianjunmu2001', '929977')
dic = chaojiying.PostPic(img, 1902)
# print(dic)
# {'err_no': 0, 'err_str': 'OK', 'pic_id': '9150421376883800001', 'pic_str': 'bwcn', 'md5': '6ac8e38e0f7f894dd1dbc37e503a8cf1'}
verfy_code = dic['pic_str']

# 输入信息
web.find_element_by_xpath('/html/body/div[3]/div/div[3]/div[1]/form/p[1]/input').send_keys('1469603831')
web.find_element_by_xpath('/html/body/div[3]/div/div[3]/div[1]/form/p[2]/input').send_keys('tianjunmu2001')
web.find_element_by_xpath('/html/body/div[3]/div/div[3]/div[1]/form/p[3]/input').send_keys(verfy_code)
time.sleep(5)
# 点击登录
web.find_element_by_xpath('/html/body/div[3]/div/div[3]/div[1]/form/p[4]/input').click()

print('登录成功')
# 打印当前剩余积分
jifen = web.find_element_by_xpath('/html/body/div[3]/div[2]/div[1]/div[1]/span').text
print(jifen)