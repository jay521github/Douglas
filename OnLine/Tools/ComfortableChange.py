from appium import webdriver
from Tools.singleton import singleton
@singleton
class initialize(object):
    def __init__(self):
        desired_caps={}
        desired_caps['platformName']='Android'
        desired_caps['platformVersion']='4.4.2'
        desired_caps['deviceName']=':MI_6_'
        desired_caps['appPackage']='com.ihimee.bwqs'
        desired_caps['appActivity']='com.himee.LogoActivity'
        self.driver=webdriver.Remote('http://127.0.0.1:4723/wd/hub',desired_caps)
