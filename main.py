from selenium import webdriver
from time import sleep

from selenium.webdriver import ActionChains
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
driver.find_element(By.XPATH, "//input[@id='basic_loginName']").send_keys('xjx_1')
driver.find_element(By.XPATH, "//input[@id='basic_password']").send_keys('123456')
driver.find_element(By.XPATH, "//button[@class='ant-btn ant-btn-primary ant-btn-lg login-button']").click()
driver.find_element(By.XPATH, "//*[@id='ptp']/section/header/div[1]/div/ul/li[2]/span/span").click()
driver.find_element(By.XPATH, "//*[@id='ptp']/section/main/div/div/div[1]/div[2]/div/div/div/div/div/div/div[1]/div["
                              "2]/button/span").click()
driver.find_element(By.XPATH, "//input[@id='form_item_name']").send_keys('c语言')
iframe = driver.find_element(By.XPATH, '//div[2]/div[1]/iframe')
driver.switch_to.frame(iframe)
driver.find_element(By.XPATH, "//*[@id='tinymce']/p").send_keys('c语言是一个very good的语言')
driver.switch_to.default_content()
driver.find_element(By.XPATH, "//button[@class='ant-btn']").click()
driver.find_element(By.XPATH, "//input[@type='file']").send_keys('C:/Users/dell/Desktop/c.png')
driver.find_element(By.XPATH, "//a[@class='vicp-operate-btn']").click()
driver.find_element(By.XPATH, "//input[@step='1']").send_keys('100')
driver.find_element(By.XPATH, "//input[@step='0.1']").send_keys('100')
# driver.find_element(By.XPATH, "//div[@aria-posinset='3']").click()
driver.find_element(By.XPATH, "/html/body/div[3]/div/div[2]/div/div[2]/div[2]/div/div/div[1]/div[2]/div/div/div/div/form/div[6]/div[2]/div/div/ul/li[3]").click()
# driver.find_element(By.XPATH, "//div[@class='ant-select-selection-overflow']").click()
driver.find_element(By.XPATH, "/html/body/div[3]/div/div[2]/div/div[2]/div[2]/div/div/div[1]/div["
                              "2]/div/div/div/div/form/div[7]/div[2]/div[1]/div/div/div/div/div").click()
sleep(1)
driver.find_element(By.XPATH, "/html/body/div[5]/div/div/div/div[2]/div[1]/div/div/div[1]/div").click()
driver.find_element(By.XPATH, "/html/body/div[5]/div/div/div/div[2]/div[1]/div/div/div[2]/div").click()
driver.find_element(By.XPATH, "/html/body/div[5]/div/div/div/div[2]/div[1]/div/div/div[3]/div").click()
driver.find_element(By.XPATH, "/html/body/div[3]/div/div[2]/div/div[2]/div[2]/div/div/div[1]/div["
                              "2]/div/div/div/div/form/div[7]/div[2]/div[1]/div/div/div/div/div").click()

sleep(1)

# 定位需要进行悬停操作的元素
element_to_hover_over = driver.find_element(By.XPATH, '/html/body/div[7]/div/div[2]/div/div[2]/div[2]/div/div/div[3]/div')

# 创建一个ActionChains对象，并在其中添加悬停事件
hover = ActionChains(driver).move_to_element(element_to_hover_over)

# 执行悬停事件
hover.perform()

sleep(2)

element = driver.find_element(By.XPATH, '/html/body/div[7]/div/div[2]/div/div[2]/div[2]/div/div/div[3]/div')

# 首先模拟鼠标按下事件
action_chains = ActionChains(driver)
action_chains.click_and_hold(element).perform()

# 然后模拟鼠标移动并释放事件，这个过程会导致滚动条位置发生变化
action_chains.move_by_offset(0, 10000).release().perform()

# is_email_visible = driver.find_element(By.XPATH, "/html/body/div[3]/div/div[2]/div/div[2]/div[2]/div/div["
#                                                 "@data-simplebar='init']").is_displayed()
# js = 'document.getElementsByClassName("simplebar-dragging")[0].scrollTop=100000'
# driver.execute_script("window.scrollTo(0,100000)")
# driver.execute_script(js)
sleep(3)
driver.find_element(By.XPATH, "/html/body/div[3]/div/div[2]/div/div[2]/div[2]/div/div/div[1]/div[2]/div/div/div/div/form/div[9]/div[2]/div/div/div/div[1]/div/div/button/span[1]").click()

sleep(2)

# js1 = "document.getElementsByClassName('ant-select-tree-title').style = 'display:block'"
# driver.execute_script(js1)

# is_email_visible = driver.find_element(By.XPATH, "//span[3]/span").is_displayed()
# driver.find_element(By.XPATH, "//div[@class='ant-select-dropdown ant-tree-select-dropdown "
#                            "ant-select-dropdown-placement-bottomLeft']")
# driver.find_element(By.XPATH, "//span[3][@class='ant-select-tree-node-content-wrapper "
#                              "ant-select-tree-node-content-wrapper-normal']").click()

# driver.find_element(By.XPATH, "//*[@id='form_item_organization_id']").click()
driver.find_element(By.XPATH, "//span[3]/span").click()
# driver.find_element(By.XPATH, "//div[@class='ant-select ant-tree-select ant-select-single']").click()

# driver.find_element(By.XPATH, "//div[@class='ant-select-tree-treenode ant-select-tree-treenode-switcher-close "
#                              "ant-select-tree-treenode-leaf-last']")
sleep(1)
driver.find_element(By.XPATH, "/html/body/div[3]/div/div[2]/div/div[2]/div[2]/div/div/div[1]/div["
                              "2]/div/div/div/div/form/div[9]/div[2]/div/div/div/div[1]/div/div/button/span["
                              "1]").click()

# WebElement element = driver.findElement(By.xpath("element_xpath"));
# JavascriptExecutor executor = (JavascriptExecutor)driver;
# executor.executeScript("arguments[0].click();", element);


driver.find_element(By.XPATH, "//span[@class='ant-input-affix-wrapper single-user-selector']/input").click()
driver.find_element(By.XPATH, "//tr[@data-row-key='51']/td[1]/label/span/input").click()
driver.find_element(By.XPATH, '/html/body/div[7]/div/div[2]/div/div[2]/div[3]/div/div[2]/button/span').click()

driver.find_element(By.XPATH, "/html/body/div[6]/div/div[2]/div/div[2]/div[2]/form/div[2]/div["
                              "2]/div/div/div/div/div/div").click()

driver.find_element(By.XPATH, "/html/body/div[10]/div/div/div/div[2]/div[1]/div/div/div/div").click()
driver.find_element(By.XPATH, "/html/body/div[6]/div/div[2]/div/div[2]/div[3]/button[2]/span").click()
driver.find_element(By.XPATH, "/html/body/div[4]/div/div[2]/div/div[2]/div[3]/button[2]/span").click()
