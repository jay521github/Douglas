from selenium import webdriver
from time import sleep
driver=webdriver.Firefox()
driver.get('http://192.168.54.212:58088/login/login')
driver.maximize_window()
driver.find_element_by_xpath("//input[@name='loginname']").send_keys('admin')
driver.find_element_by_xpath("//input[@name='password']").send_keys('123456')
driver.find_element_by_xpath("//a[@class='landbtn']").click()
sleep(3)
driver.find_element_by_xpath("//a[contains(.,'在线预览')]").click()
sleep(2)
driver.find_element_by_xpath('html/body/div[2]/div[2]/div/div[2]/div[2]/table/tbody/tr[3]/td[3]/button').click()
for handle in driver.window_handles:#始终获得当前最后的窗口
    driver.switch_to.window(handle)
sleep(3)
driver.find_element_by_xpath("//img[@onclick='nextPage()']").click()#下一页
sleep(3)
driver.find_element_by_xpath("//img[@onclick='nextPage()']").click()
sleep(3)
driver.find_element_by_xpath("//img[@onclick='nextPage()']").click()
sleep(3)
driver.switch_to.frame('childPage')
driver.find_element_by_xpath("//img[@class='singimg']").click()
sleep(3)
driver.find_element_by_xpath("//img[@class='danceimg']").click()
sleep(3)
driver.switch_to.default_content()
driver.find_element_by_xpath("//img[@onclick='nextPage()']").click()
driver.switch_to.frame('childPage')
sleep(2)
driver.find_element_by_xpath("//video[@src='Hocky Pocky.mp4']").click()#看视频
sleep(10)
driver.switch_to.default_content()
driver.find_element_by_xpath("//img[@onclick='nextPage()']").click()
driver.switch_to.frame('childPage')
sleep(3)
driver.find_element_by_xpath("//img[@src='images/cake.png']").click()#吃饭糕
sleep(1)
driver.find_element_by_xpath("//img[@src='images/1.png']").click()
sleep(1)
driver.find_element_by_xpath("//img[@src='images/2.png']").click()
sleep(1)
driver.find_element_by_xpath("//img[@src='images/4.png']").click()
sleep(1)
driver.find_element_by_xpath("//img[@src='images/5.png']").click()
sleep(1)
driver.find_element_by_xpath("//img[@src='images/6.png']").click()
sleep(1)
driver.find_element_by_xpath("//img[@src='images/7.png']").click()
sleep(1)
driver.find_element_by_xpath("//img[@src='images/8.png']").click()
sleep(1)
driver.find_element_by_xpath("//img[@src='images/9.png']").click()
sleep(1)
driver.find_element_by_xpath("//img[@src='images/10.png']").click()
sleep(2)
driver.switch_to.default_content()
driver.find_element_by_xpath("//img[@onclick='nextPage()']").click()
sleep(2)
driver.find_element_by_xpath("//img[@onclick='nextPage()']").click()
driver.switch_to.frame('childPage')
sleep(2)
driver.find_element_by_xpath("//img[@src='images/box_bg.png']").click()#玩具箱
sleep(2)
driver.find_element_by_xpath("//img[@src='images/box_ball.gif']").click()
sleep(2)
driver.find_element_by_xpath("//img[@src='images/box_car.gif']").click()
sleep(2)
driver.find_element_by_xpath("//img[@src='images/box_doll.gif']").click()
sleep(2)
driver.find_element_by_xpath("//img[@src='images/box_helicopter.gif']").click()
sleep(2)
driver.find_element_by_xpath("//img[@src='images/box_train.gif']").click()
sleep(2)
driver.switch_to.default_content()
driver.find_element_by_xpath("//img[@onclick='nextPage()']").click()
driver.switch_to.frame('childPage')
sleep(2)
driver.find_element_by_xpath("//img[@src='images/game1_start.png']").click()#点击气球
sleep(2)
driver.find_element_by_xpath("//img[@src='images/qiq1.gif']").click()
sleep(2)
driver.find_element_by_xpath("//img[@src='images/qiq2.gif']").click()
sleep(2)
driver.find_element_by_xpath("//img[@src='images/qiq3.gif']").click()
sleep(2)
driver.find_element_by_xpath("//img[@src='images/qiq4.gif']").click()
sleep(2)
driver.find_element_by_xpath("//img[@src='images/qiq5.gif']").click()
sleep(2)
driver.switch_to.default_content()
driver.find_element_by_xpath("//img[@onclick='nextPage()']").click()
driver.switch_to.frame('childPage')
sleep(2)
driver.find_element_by_xpath("//img[@class='start']").click()#转盘
sleep(6)
driver.find_element_by_xpath("//img[@src='images/circle1.png']").click()
driver.switch_to.default_content()
driver.find_element_by_xpath("//img[@onclick='nextPage()']").click()
driver.switch_to.frame('childPage')
sleep(2)
driver.find_element_by_xpath("//span[contains(.,'car')]").click()#钓鱼
sleep(2)
driver.find_element_by_xpath("//img[@src='images/s_car.png']").click()
sleep(2)
driver.find_element_by_xpath("//span[contains(.,'ball')]").click()
driver.find_element_by_xpath("//img[@src='images/s_ball.png']").click()
sleep(2)
driver.find_element_by_xpath("//span[contains(.,'helicopter')]").click()
driver.find_element_by_xpath("//img[@src='images/s_helicopter.png']").click()
sleep(2)
driver.find_element_by_xpath("//span[contains(.,'doll')]").click()
sleep(1)
driver.find_element_by_xpath("//img[@src='images/s_doll.png']").click()
sleep(2)
driver.find_element_by_xpath("//span[contains(.,'train')]").click()
sleep(1)
driver.find_element_by_xpath("//img[@src='images/s_train.png']").click()
driver.switch_to.default_content()
driver.find_element_by_xpath("//img[@onclick='nextPage()']").click()
sleep(2)
driver.find_element_by_xpath("//img[@onclick='nextPage()']").click()
driver.find_element_by_xpath("//img[@onclick='nextPage()']").click()
driver.find_element_by_xpath("//img[@onclick='nextPage()']").click()
driver.quit()


