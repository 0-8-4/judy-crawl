from selenium import webdriver

driver = webdriver.PhantomJS()

driver.get('https://www.baidu.com/')

driver.save_screenshot('baidu1.png')

driver.find_element_by_id('kw').send_keys('美女')

driver.save_screenshot('baidu2.png')
#driver.find_element_by_class_name('bg s_btn').click()

#driver.find_element_by_id('su').click()

import time
time.sleep(3)

driver.save_screenshot('baidu3.png')