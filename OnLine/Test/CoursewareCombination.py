from selenium import webdriver
from time import sleep
driver=webdriver.Firefox()
driver.get('http://192.168.54.212:58088/login/login')
driver.maximize_window()
driver.find_element_by_xpath("//input[@name='loginname']").send_keys('shenfenghua')
driver.find_element_by_xpath("//input[@name='password']").send_keys('123456')
driver.find_element_by_xpath("//a[@class='landbtn']").click()
cookies=driver.get_cookies()
for cookie in cookies:
    print('value=%s'% cookie['value'])
sleep(2)
driver.find_element_by_xpath("//a[contains(.,'课程管理')]").click()
sleep(5)
driver.find_element_by_xpath("html/body/div[2]/div[2]/div/div[2]/div[2]/table/tbody/tr[1]/td[3]/button[1]").click()
sleep(2)
# classname=driver.find_element_by_xpath("//td[contains(.,'英标一级A方案')]").text
# delete=driver.find_element_by_xpath('html/body/div[2]/div[2]/div/div[2]/div/table/tbody/tr[2]/td[10]/button[4]')
# true=driver.find_element_by_xpath("//button[contains(.,'确定')]")
# if classname=='英标一级A方案':
#     delete.click()
# else:
driver.find_element_by_xpath("//button[contains(.,'添加一个组合方案')]").click()
sleep(3)
driver.find_element_by_xpath('html/body/div[2]/div[2]/div/div[2]/div[2]/table/tbody/tr[1]/td[7]/button[1]').click()
sleep(2)
print(driver.current_window_handle)
handles=driver.window_handles
print(handles)

for handle in handles:#始终获得当前最后的窗口
    driver.switch_to.window(handle)

sleep(5)
driver.find_element_by_xpath("//img[contains(@onclick,'next();')]").click()
sleep(2)
next=driver.find_element_by_xpath("//img[contains(@onclick,'next();')]")
next.click()
next.click()
next.click()
driver.find_element_by_xpath("//img[contains(@onclick,'cancel();')]").click()
driver.find_element_by_xpath("//img[contains(@onclick,'savePro();')]").click()
driver.find_element_by_xpath("//input[@placeholder='请修改方案名称']").send_keys('英标一级A方案')
driver.find_element_by_xpath("//a[@onclick='submit()']").click()
driver.find_element_by_xpath("//a[@id='ye']").click()
sleep(2)
driver.find_element_by_xpath("//input[@value='610']").click()
driver.find_element_by_xpath("//button[contains(.,'确定')]").click()
driver.close()
sleep(5)
driver.switch_to.window('13')
driver.find_element_by_xpath("//button[contains(.,'返回')]").click()
sleep(3)
update=driver.find_element_by_xpath("//button[contains(.,'修改名称')]")
update.click()
sleep(2)
input=driver.find_element_by_xpath("//input[contains(@check-type,'required')]")
input.clear()
input.send_keys('测试')
driver.find_element_by_xpath("//button[contains(.,'确定')]").click()
sleep(2)
driver.find_element_by_xpath("//a[contains(.,'班级列表')]").click()
sleep(2)
driver.find_element_by_xpath(".//*[@id='bslist']/table/tbody/tr[10]/td[8]/button[2]").click()
sleep(2)
driver.find_element_by_xpath("//button[contains(.,'确定')]").click()
sleep(2)
driver.find_element_by_xpath("//a[contains(.,'课程管理')]").click()
sleep(5)
driver.find_element_by_xpath("html/body/div[2]/div[2]/div/div[2]/div[2]/table/tbody/tr[1]/td[3]/button[1]").click()
sleep(3)
driver.find_element_by_xpath("//button[contains(.,'删除')]").click()
sleep(2)
driver.find_element_by_xpath("//button[contains(.,'确定')]").click()
sleep(3)
messige=driver.find_element_by_xpath("//p[contains(.,'成功删除1条')]").text
print(messige)
b='成功删除1条'
if b==messige:
    print('没毛病、老铁')
else:
    print('碧油鸡')
driver.quit()