from selenium import webdriver
class WebInitalize(object):
    def __init__(self):
        driver=webdriver.Firefox()
        driver.get('http://192.168.54.212:58088/login/login')
        driver.maximize_window()
