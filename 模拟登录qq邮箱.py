from selenium import webdriver
browser = webdriver.Chrome(
    r"C:\Users\Administrator\AppData\Local\Google\Chrome\Application\chromedriver.exe")
browser.get('https://mail.qq.com/cgi-bin/loginpage')
browser.switch_to.frame('login_frame') #找到邮箱账号登录框对应的iframe
browser.find_element_by_name('u').send_keys('1349453726') #找到邮箱账号输入框
browser.find_element_by_name('p').send_keys('suhebetter..') #找到密码输入框
browser.find_element_by_class_name('login_button').click() #点击登陆按钮

