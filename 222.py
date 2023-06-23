
from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

'''
变量 -数据的载体
1、字母（Unicode字符）、数字、下划线，不能使用特殊字符，数字不能开头
2、变量名是区分大小写的（大小写敏感，x和X是不同的变量名）
3、不能使用python中的关键字（python代码中有特殊含义的单词）和保留字
4、见名知意（看到变量的名字，就能知道它什么意思）
5、变量的命名使用全小写，多个单词使用下划线进行连接（Snake case）
'''
options = Options()
wd = webdriver.Chrome(options=options)
url = "https://baidu.com"
element_id = 'kw'
wd.get(url)
print(wd.title)
try:
    element = wd.find_element(By.ID, element_id)
    element.send_keys('天猫精灵')
    element.find_element(By.CLASS_NAME, 'btn_wr s_btn_wr bg').click()
except NoSuchElementException:
    print('{element_id}元素不存在'.format(element_id=element_id))
wd.quit()
