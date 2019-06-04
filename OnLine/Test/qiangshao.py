from time import sleep
from appium import webdriver
desired_caps={}
desired_caps['platformName']='Android'
desired_caps['platformVersion']='4.4.2'
desired_caps['deviceName']='MI_6'
desired_caps['appPackage']='com.ihimee.bwqs'
desired_caps['appActivity']='com.himee.LogoActivity'
driver=webdriver.Remote('http://127.0.0.1:4723/wd/hub',desired_caps)
#滑屏
sleep(5)
size=driver.get_window_size()
width=size.get('width')
height=size.get('height')
driver.swipe(size['width']*0.7,size['height']*0.3,size['width']*0.1,size['height']*0.3,1000)
driver.swipe(size['width']*0.7,size['height']*0.3,size['width']*0.1,size['height']*0.3,1000)
#driver.swipe(size['width']*0.7,size['height']*0.3,size['width']*0.1,size['height']*0.3,1000)
# driver.swipe(size['width']*0.7,size['height']*0.3,size['width']*0.1,size['height']*0.3,1000)
# driver.swipe(size['width']*0.7,size['height']*0.3,size['width']*0.1,size['height']*0.3,1000)
# sleep(2)
# driver.swipe(size['width']*0.8,size['height']*0.3,size['width']*0.1,size['height']*0.3,1000)
# driver.swipe(700,500,100,500,1000)
# driver.swipe(700,500,100,500,1000)
# driver.swipe(700,500,100,500,1000)
# driver.swipe(700,500,100,500,1000)
# driver.swipe(700,500,100,500,1000)
sleep(2)
# driver.swipe(700,500,100,500,1000)
driver.find_element_by_class_name('android.widget.Button').click()
sleep(2)
# driver.find_element_by_id('com.ihimee.bwqs:id/main_tab_settings').click()
sleep(2)
#登陆
driver.find_element_by_id('com.ihimee.bwqs:id/username_edit').send_keys('zhangkairui1 ')
driver.find_element_by_id('com.ihimee.bwqs:id/password_edit').send_keys('123456')
driver.find_element_by_id('com.ihimee.bwqs:id/login_btn').click()
sleep(5)
#学习模块
driver.find_element_by_('com.ihimee.bwqs:id/bottom_nav_icon').click()
sleep(3)
#确认按钮
driver.find_element_by_id('com.ihimee.bwqs:id/sure_btn').click()
sleep(2)
driver.find_elements_by_class_name('android.widget.RelativeLayout')[0].click()
sleep(5)
driver.find_elements_by_class_name('android.widget.RelativeLayout')[9].click()
sleep(2)
# driver.swipe(500,1000,500,100,1000)
# driver.swipe(500,1000,500,100,1000)
driver.swipe(size['width']*0.3,size['height']*0.8,size['width']*0.3,size['height']*0.3,1000)
sleep(2)
driver.tap([(114,1633)])
sleep(10)
driver.tap([(114,1633)])
sleep(2)
driver.find_element_by_id('com.ihimee.bwqs:id/topbar_left_view_btn').click()
sleep(2)
driver.find_element_by_id('com.ihimee.bwqs:id/topbar_left_view_btn').click()
driver.find_element_by_id('com.ihimee.bwqs:id/main_tab_settings').click()
a=driver.find_element_by_id('com.ihimee.bwqs:id/user_name').text
b='张凯瑞zhangkairui'
if a==b:
    print('pass')
else:
    print('fail')
driver.quit()