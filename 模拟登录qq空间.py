import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

url = 'http://qzone.qq.com'


def main():
    browser = webdriver.Chrome("C:\Program Files\Google\Chrome\Application\chromedriver.exe")
    browser.get(url)

    browser.switch_to.frame('login_frame')  # 找到账号登录框对应的iframe
    # browser.find_element(By.ID,'switcher_plogin').click()
    element = WebDriverWait(browser, 5, 0.5).until(
        EC.presence_of_element_located((By.ID, "switcher_plogin"))
    )  # 直到网页加载出qq登录按钮，才继续下一步
    element.click()
    browser.find_element_by_name('u').clear()  # 清空输入框
    browser.find_element_by_name('u').send_keys('1349453726')  # 找到qq账号输入框
    time.sleep(1)
    browser.find_element_by_name('p').clear()  # 清空输入框
    browser.find_element_by_name('p').send_keys('suhebetter..')  # 找到密码输入框
    time.sleep(1)
    browser.find_element_by_class_name('login_button').click()  # 点击登陆按钮
    time.sleep(1)
    iframe = browser.find_element(By.XPATH, '//*[@id="tcaptcha_iframe"]')  # 找到切换的页面
    browser.switch_to.frame(iframe)
    button = browser.find_element(By.XPATH, '/html/body/div/div[3]/div[2]/div[2]/div[2]/div[1]')  # 找到“蓝色滑块”
    time.sleep(1)
    distance = 195  # 初始位移
    offset = 5  # 位移减少区间
    while 1:
        action = ActionChains(browser)  # 实例化一个action对象
        action.click_and_hold(button).perform()  # perform()用来执行ActionChains中存储的行为
        action.reset_actions()
        print('目前位移为：', distance)
        action.drag_and_drop_by_offset(button, distance, 0).perform()  # 移动滑块
        try:
            alert = browser.find_element(By.XPATH, '/html/body/div/div[3]/div[2]/div[2]/div[2]/div[1]')
        except Exception as e:
            print('get alert error: %s' % e)
            alert = ''
        if alert:
            print(u'滑块位移需要调整:目前为 %s' % distance)
            distance -= offset
            time.sleep(5)
        else:
            print('滑块验证通过')
            browser.switch_to.parent_frame()  # 验证成功后跳回最外层页面
            break


if __name__ == '__main__':
    main()
