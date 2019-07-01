from selenium import webdriver
if __name__ == '__main__':




    driver = webdriver.Chrome()
    driver.get('http://tms.beiwaiguoji.com/login/login')
    driver.maximize_window()
    driver.find_element_by_xpath("//input[@name='loginname']").send_keys('admin')
    driver.find_element_by_xpath("//input[@name='password']").send_keys('bwgj')
    driver.find_element_by_name('validNumber').send_keys(6666)
    driver.find_element_by_xpath("//a[@class='landbtn']").click()
    driver.implicitly_wait(30)



    js = "var q=document.body.scrollTop=500"
    driver.execute_script(js)
    driver.find_element_by_xpath('//*[@id="sub_0"]/li[22]/a/span').click()
    js = "var q=document.body.scrollTop=0"
    driver.execute_script(js)
    driver.find_element_by_xpath('//*[@id="queryForm"]/div[2]/div/div[2]/button').click()
    driver.find_element_by_xpath('//*[@id="queryForm"]/div[2]/div/div[2]/ul/li[3]/a/label').click()
    driver.find_element_by_xpath('//*[@id="queryForm"]/button').click()
    Page_text=driver.find_element_by_xpath('//*[@id="bslist"]').text
    Page_data='没有数据！'
    file_path = r'C:\Users\Administrator\Desktop\Tms.txt'
    if Page_data in Page_text:
        print('没有待处理的问题')
    else:
        with open(file_path,'w')as fp:
            fp.write(Page_text)
    driver.quit()








