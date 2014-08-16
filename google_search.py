#http://selenium-python.readthedocs.org/
#http://irwinkwan.com/2013/04/05/automating-the-web-with-selenium-complete-tasks-automatically-and-write-test-cases/
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
driver = webdriver.Firefox()
driver.get("https://www.google.com")
elem = driver.find_element_by_name("q")
elem.send_keys("human trafficking")
elem.submit()
WebDriverWait(driver,10).until(EC.title_contains("human trafficking"))
print driver.title
