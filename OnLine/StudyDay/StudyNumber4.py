# from selenium import webdriver
# from selenium.common.exceptions import NoSuchElementException
# import unittest
# import os
# from time import  *
# class Baidu(unittest.TestCase):
#     def setUp(self):
#         self.driver=webdriver.Firefox()
#         self.driver.get('https://www.baidu.com/')
#         self.driver.maximize_window()
#         self.driver.implicitly_wait(10)
#     def tearDown(self):
#         pass
#     def test01(self):
#         input=self.driver.find_element_by_id("kw")
#         try: