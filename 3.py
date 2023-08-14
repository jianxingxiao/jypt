import document
from selenium import webdriver
from time import sleep

from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import NoSuchElementException

driver = webdriver.Firefox()
driver.implicitly_wait(10)
driver.maximize_window()
driver.get("http://www.ustchcs.com/p3-v17/p3-frontend-test/#/login")
driver.find_element(By.XPATH, "//input[@id='basic_loginName']").send_keys('xjx_organization3')
driver.find_element(By.XPATH, "//input[@id='basic_password']").send_keys('123456')
driver.find_element(By.XPATH, "//button[@class='ant-btn ant-btn-primary ant-btn-lg login-button']").click()
driver.find_element(By.XPATH, "//*[@id='ptp']/section/header/div[1]/div/ul/li[2]/span/span").click()
driver.find_element(By.XPATH, "//*[@id='ptp']/section/main/div/div/div[1]/div[2]/div/div/div/div/div/div/div[1]/div["
                              "2]/button/span").click()
driver.find_element(By.XPATH, "//input[@id='form_item_name']").send_keys('c语言')
sleep(2)

# iframe = driver.find_element(By.XPATH, '//div[2]/div[1]/iframe')
# driver.switch_to.frame(iframe)
# driver.find_element(By.XPATH, "//*[@id='tinymce']").send_keys('c语言是一个very good的语言')
# driver.switch_to.default_content()


# try:
#     ele = driver.find_element(By.XPATH, "//div[@class = 'mce-editor-container']/textarea")
#     driver.execute_script("arguments[0].style.visibility='visible';", ele)
#     print("ele元素已取消隐藏")
#     driver.execute_script("arguments[0].style.display='block';", ele)
#     print("ele元素已取消display：none")
#     element = driver.find_element(By.XPATH, "//div[@class='tox tox-tinymce']")
#     driver.execute_script("arguments[0].style.visibility='visible';", element)
#     print("element元素已取消隐藏")
#
# except NoSuchElementException:
#     print("元素没有取消隐藏")

try:
    iframe = driver.find_element(By.XPATH, '//div[2]/div[1]/iframe')
    driver.switch_to.frame(iframe)
    print("成功进入iframe")

    # 在iframe内进行操作
    try:
        # 验证元素是否存在于iframe内
        element1 = driver.find_element(By.XPATH, "//*[@class='mce-content-body ']")
        # element1 = driver.find_element(By.XPATH, "/html/body/p")
        # element1 = driver.find_element(By.TAG_NAME, "p")
        print("成功找到元素")

        try:
            element1.click()
            # sleep(2)
            element1.send_keys('c语言是一个very good的语言')
            print("成功输入")

        except NoSuchElementException:
            print("无法输入")

    except NoSuchElementException:
        print("未找到元素")

    # 切换回默认上下文
    driver.switch_to.default_content()
except NoSuchElementException:
    print("未成功进入iframe")
