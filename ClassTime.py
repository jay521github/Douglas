from selenium import webdriver
from time import sleep
from selenium.webdriver.support.ui import Select
driver=webdriver.Firefox()
driver.get('http://192.168.54.235:8081/qingshao/_platform/indexFrameNew1.jsp')
driver.maximize_window()
driver.find_element_by_xpath('html/body/form/div/div[2]/p[1]/input').send_keys('shangchao')
driver.find_element_by_xpath('html/body/form/div/div[2]/p[2]/input').send_keys('123456')
driver.find_element_by_xpath('html/body/form/div/div[2]/p[3]/input').send_keys('0000')
driver.find_element_by_xpath('html/body/form/div/div[2]/p[4]/input').click()
sleep(3)
#教务
driver.find_element_by_xpath('html/body/table/tbody/tr[2]/td[1]/a/img').click()
sleep(5)
driver.switch_to.frame("topFrame")
#班级管理
driver.find_element_by_xpath('html/body/table/tbody/tr[2]/td/div/ul/li[3]/a/span').click()
driver.switch_to.default_content()
driver.switch_to.frame("mainFrame")
driver.switch_to.frame('BoardTitle')
sleep(2)
driver.find_element_by_xpath('//*[@title="班级管理"]').click()
driver.switch_to.parent_frame()
driver.switch_to.frame('right')
sleep(6)
driver.find_element_by_xpath('//*[@name="teacherName"]').send_keys('老师')
sleep(5)
Select(driver.find_element_by_id('classStatus')).select_by_value('2')
driver.find_element_by_xpath('//*[@value="搜索"]').click()
sleep(3)
driver.find_element_by_xpath('html/body/form/div/table/tbody/tr[2]/td[10]/span/a/span').click()
sleep(5)
driver.find_element_by_xpath('html/body/table[3]/tbody/tr[1]/td[6]/img').click()
sleep(5)
#移除js只读的属性
js = "document.getElementById(id='input_td_486389_1').removeAttribute('readonly')"
driver.execute_script(js)
sleep(3)
driver.find_element_by_xpath('//*[@id="input_td_486389_1"]').clear()
driver.find_element_by_xpath('//*[@id="input_td_486389_1"]').send_keys('2018-06-29')
sleep(2)
driver.find_element_by_xpath('html/body/table[2]/tbody/tr[2]/td[2]/input').click()
driver.quit()