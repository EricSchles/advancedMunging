#helpful guide - http://thiagomarzagao.com/2013/11/12/webscraping-with-selenium-part-1/
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException

driver = webdriver.Firefox()
driver.get("http://www.missingkids.com/search?action=continueSearch&searchSubject=child")
WebDriverWait(driver,100).until(EC.element_to_be_clickable((By.XPATH, '//input[@name="fromDate"]')))
start_date = driver.find_element_by_xpath('//input[@name="fromDate"]')
end_date = driver.find_element_by_xpath('//input[@name="toDate"]')
submit_button = driver.find_element_by_xpath('//form[@id="missingKidsSearchForm"]/input[@value="Submit"]')
start_date.send_keys("8/1/2014")
end_date.send_keys("8/3/2014")
submit_button.click()

#print dir(submit_button)
WebDriverWait(driver,100).until(EC.element_to_be_clickable((By.XPATH, '//div[@class="mk-personThumbnail personThumbnail child-1 clearfix mk-clearfix"]')))
table = driver.find_element_by_xpath('//div[@class="mk-personThumbnail personThumbnail child-1 clearfix mk-clearfix"]')
print table.text
