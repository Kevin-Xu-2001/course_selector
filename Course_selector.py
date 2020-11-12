#/!/usr/bin/env python3

from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time

driver = webdriver.Chrome("/YOURPATH/chromedriver")
#driver = webdriver.PhantomJS("/YOURPATH/phantomjs-2.1.1-macosx/bin/phantomjs")

#Request the page
driver.get('https://horizon.mcgill.ca/pban1/twbkwbis.P_WWWLogin')
driver.save_screenshot("./initial.png")
time.sleep(4)

driver.save_screenshot("./login.png")

driver.find_element_by_id("mcg_un").send_keys("MCGILL_EMAIL")
driver.find_element_by_id("mcg_pw").send_keys("PASSWORD")
driver.find_element_by_id("mcg_un_submit").click()

driver.get('https://horizon.mcgill.ca/pban1/bwskfreg.P_AltPin')

select = Select(driver.find_element_by_id('term_id'))

# select by value 
select.select_by_value('202101')

#submit the selection
driver.find_element_by_xpath("/html/body/div[3]/form/input").click()

time.sleep(1)

driver.find_element_by_id("crn_id1").send_keys("16983")
driver.find_element_by_xpath("/html/body/div[3]/form/input[19]").click()

time.sleep(1)

try:
	select = Select(driver.find_element_by_id("waitaction_id1"))
	select.select_by_value('LW')
	driver.find_element_by_xpath("/html/body/div[3]/form/input[19]").click()
except Exception as e:
	print("We can't find waitlist")
	print(e)


time.sleep(5)

driver.quit()



