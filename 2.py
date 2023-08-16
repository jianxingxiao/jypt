import document
from selenium import webdriver
from time import sleep

from selenium.common import NoSuchElementException
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait

# 解决selenium打开chrome浏览器后秒关闭浏览器
options = webdriver.ChromeOptions()
options.add_experimental_option('detach', True)
driver = webdriver.Chrome(options=options)
driver.implicitly_wait(10)
driver.maximize_window()
driver.get("http://www.ustchcs.com/p3-v17/p3-frontend-test/#/login")
driver.find_element(By.XPATH, "//input[@id='basic_loginName']").send_keys('xjx_organization3')
driver.find_element(By.XPATH, "//input[@id='basic_password']").send_keys('123456')
driver.find_element(By.XPATH, "//button[@class='ant-btn ant-btn-primary ant-btn-lg login-button']").click()
driver.find_element(By.XPATH, "//*[@id='ptp']/section/header/div[1]/div/ul/li[2]/span/span").click()
driver.find_element(By.XPATH, "//*[@id='ptp']/section/main/div/div/div[1]/div[2]/div/div/div/div/div/div/div[1]/div["
                              "2]/button/span").click()
driver.find_element(By.XPATH, "//input[@id='form_item_name']").send_keys('c++')
iframe = driver.find_element(By.XPATH, '//div[2]/div[1]/iframe')
driver.switch_to.frame(iframe)
driver.find_element(By.XPATH, "//*[@id='tinymce']/p").send_keys('c++是一个very good的语言')
driver.switch_to.default_content()
driver.find_element(By.XPATH, "//button[@class='ant-btn']").click()
driver.find_element(By.XPATH, "//input[@type='file']").send_keys('C:/Users/dell/Desktop/c.png')
driver.find_element(By.XPATH, "//a[@class='vicp-operate-btn']").click()
driver.find_element(By.XPATH, "//input[@step='1']").send_keys('100')
driver.find_element(By.XPATH, "//input[@step='0.1']").send_keys('100')
# driver.find_element(By.XPATH, "//div[@aria-posinset='3']").click()
sleep(2)
driver.find_element(By.XPATH, "/html/body/div[3]/div/div[2]/div/div[2]/div[2]/div/div/div[1]/div["
                              "2]/div/div/div/div/form/div[6]/div[2]/div/div/ul/li[3]").click()
# driver.find_element(By.XPATH, "//div[@class='ant-select-selection-overflow']").click()
driver.find_element(By.XPATH, "/html/body/div[3]/div/div[2]/div/div[2]/div[2]/div/div/div[1]/div["
                              "2]/div/div/div/div/form/div[7]/div[2]/div[1]/div/div/div/div/div").click()
sleep(1)
driver.find_element(By.XPATH, "/html/body/div[5]/div/div/div/div[2]/div[1]/div/div/div[1]/div").click()
driver.find_element(By.XPATH, "/html/body/div[5]/div/div/div/div[2]/div[1]/div/div/div[2]/div").click()
driver.find_element(By.XPATH, "/html/body/div[5]/div/div/div/div[2]/div[1]/div/div/div[3]/div").click()
driver.find_element(By.XPATH, "/html/body/div[3]/div/div[2]/div/div[2]/div[2]/div/div/div[1]/div["
                              "2]/div/div/div/div/form/div[7]/div[2]/div[1]/div/div/div/div/div").click()

sleep(2)

element = driver.find_element(By.ID, "form_item_organization_id")

# 首先模拟鼠标按下事件
action_chains = ActionChains(driver)
action_chains.click_and_hold(element).perform()

sleep(1)
scrollbar = driver.find_element(By.XPATH,
                                "/html/body/div[3]/div/div[2]/div/div[2]/div[2]/div/div/div[3]/div")  # 获取页面的body元素
action = ActionChains(driver)
action.move_to_element(scrollbar).click_and_hold().perform()  # 鼠标点击并按住滚动条
action.move_by_offset(0, 200).release().perform()  # 拖动滚动条向下滚动100个像素

sleep(1)
driver.find_element(By.XPATH, "/html/body/div[3]/div/div[2]/div/div[2]/div[2]/div/div/div[1]/div["
                              "2]/div/div/div/div/form/div[8]/div[2]/div/div/div/div").click()
driver.find_element(By.XPATH, "//span[@class='ant-select-tree-title']").click()
sleep(1)
driver.find_element(By.XPATH, "/html/body/div[3]/div/div[2]/div/div[2]/div[2]/div/div/div[1]/div["
                              "2]/div/div/div/div/form/div[9]/div[2]/div/div/div/div[1]/div/div/button/span[1]").click()
sleep(2)

driver.find_element(By.XPATH,
                    '/html/body/div[6]/div/div[2]/div/div[2]/div[2]/form/div[1]/div[2]/div/div/div/div/div/div/div/div').click()
sleep(1)
driver.find_element(By.XPATH,
                    '/html/body/div[8]/div/div[2]/div/div[2]/div[2]/div/div/div/div[1]/div['
                    '2]/div/div/div/div/div/div[2]/div/div/div/div/div/div/div[2]/table/tbody/tr[2]/td['
                    '1]/label/span/input').click()
sleep(1)
driver.find_element(By.XPATH, "/html/body/div[8]/div/div[2]/div/div[2]/div[2]/div/div/div/div[1]/div["
                              "2]/div/div/div/div/div/div[2]/div/div/div/div/ul/li[5]/button").click()
sleep(1)
driver.find_element(By.XPATH, "/html/body/div[8]/div/div[2]/div/div[2]/div[2]/div/div/div/div[1]/div["
                              "2]/div/div/div/div/div/div[2]/div/div/div/div/div/div/div[2]/table/tbody/tr[5]/td["
                              "1]/label/span/input").click()
sleep(1)
driver.find_element(By.XPATH, "/html/body/div[8]/div/div[2]/div/div[2]/div[3]/div/div[2]").click()

driver.find_element(By.XPATH, "/html/body/div[6]/div/div[2]/div/div[2]/div[2]/form/div[2]/div["
                              "2]/div/div/div/div/div/div").click()
sleep(2)
driver.find_element(By.XPATH, "/html/body/div[9]/div/div/div/div[2]/div[1]/div/div/div/div").click()
driver.find_element(By.XPATH, "/html/body/div[6]/div/div[2]/div/div[2]/div[2]/form/div[2]/div["
                              "2]/div/div/div/div/div/div").click()
driver.find_element(By.XPATH, "/html/body/div[6]/div/div[2]").click()
sleep(1)
driver.find_element(By.XPATH, "/html/body/div[6]/div/div[2]/div/div[2]/div[3]/button[2]/span").click()
driver.find_element(By.XPATH, "/html/body/div[3]/div/div[2]/div/div[2]/div[3]/button[2]/span").click()
sleep(1)
driver.find_element(By.XPATH, "//*[@id='ptp']/section/main/div/div/div[1]/div[2]/div/div/div/div/div/div/div[2]/div["
                              "1]/div/div/div/div[4]/span/div/span").click()
sleep(1)
driver.find_element(By.XPATH, "/html/body/div[3]/div/div/div/div[2]/div/div[2]/button[2]/span").click()

try:
    driver.find_element(By.XPATH,
                        "//*[@id='ptp']/section/main/div/div/div[1]/div[2]/div/div/div/div/div/div/div[2]/div["
                        "1]/div/div/div/div[2]/span").click()
    print("删除成功")
except NoSuchElementException:
    print("没有删除成功")






