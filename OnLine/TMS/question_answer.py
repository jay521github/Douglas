from selenium import webdriver
import smtplib  #加载smtplib模块
from email.mime.text import MIMEText
from email.utils import parseaddr, formataddr
my_sender='jay521mm@126.com' #发件人邮箱账号，为了后面易于维护，所以写成了变量
my_user='sundong@beiwaiguoji.com','zhangxi@beiwaiguoji.com' #收件人邮箱账号，为了后面易于维护，所以写成了变量
server=smtplib.SMTP("smtp.126.com",25)  #发件人邮箱中的SMTP服务器，端口是25
server.login(my_sender,"sd19841108")    #括号中对应的是发件人邮箱账号、邮箱密码
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
        msg = MIMEText('TMS有问题待处理', 'plain', 'utf-8')
        msg['From'] = formataddr(["监控者", my_sender])  # 括号里的对应发件人邮箱昵称、发件人邮箱账号
        msg['To'] = formataddr(["解决人", my_user])  # 括号里的对应收件人邮箱昵称、收件人邮箱账号
        msg['Subject'] = "TMS问题监控"  # 邮件的主题，也可以说是标题
        server.sendmail(my_sender, [my_user, ], msg.as_string())  # 括号中对应的是发件人邮箱账号、收件人邮箱账号、发送邮件
        server.quit()
        print('TMS邮件提醒已经发送')
        # att1 = MIMEText(open(file_path, 'rb').read(), 'base64', 'utf-8')
        # att1["Content-Type"] = 'application/octet-stream'
        # # 这里的filename可以任意写，写什么名字，邮件中显示什么名字
        # att1["Content-Disposition"] = 'attachment; filename="Tms问题反馈.txt"'
        # msg.attach(att1)
driver.quit()






