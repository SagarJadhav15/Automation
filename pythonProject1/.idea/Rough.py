import time
from time import sleep

import action
import pyautogui
from pyautogui import keyDown
from selenium import webdriver
from selenium.webdriver import Keys, ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from urllib3.poolmanager import key_fn_by_scheme

options = Options()
options.add_experimental_option("detach", True)
# Set up Selenium WebDriver
driver = webdriver.Chrome(options=options)
# Open the website
driver.get("https://demo.nuqare.com/")

driver.maximize_window()
driver.implicitly_wait(10)
driver.find_element(By.CSS_SELECTOR, "#standard-phoneno-input").send_keys("0000011112")
driver.find_element(By.XPATH,"(//p[@class='MuiTypography-root jss39 MuiTypography-body1'])[1]").click()


#driver.find_element(By.CSS_SELECTOR,"button[type='submit'] span[class='MuiButton-label']").click()
# OTP
#driver.find_element(By.CSS_SELECTOR, "input[placeholder='-'][aria-label='Please enter verification code. Digit 1']").send_keys("5746")
driver.find_element(By.XPATH,"//span[normalize-space()='Proceed']").click()
driver.find_element(By.CSS_SELECTOR, "input[placeholder='-'][aria-label='Please enter verification code. Digit 1']").send_keys("1111")
#driver.find_element(By.XPATH,"//span[normalize-space()='Login OTP']").click()
driver.find_element(By.XPATH,"//span[normalize-space()='Login']").click()



#select location
driver.find_element(By.XPATH,"//p[normalize-space()='Wag Cancer Clinic']").click()

driver.implicitly_wait(50)
driver.find_element(By.XPATH,"//span[normalize-space()='OK']").click()

driver.find_element(By.XPATH," //button[@title='Instant EOC Form']//span[@class='MuiIconButton-label']//*[name()='svg']").click()


action = webdriver.ActionChains(driver)



#RX************

driver.find_element(By.XPATH,"//input[@placeholder='Drug Name']").send_keys("Genericart S-Amlodipine 5mg Tablet")
action.send_keys(Keys.ARROW_DOWN).perform()
action.send_keys(Keys.ENTER).perform()

driver.find_element(By.XPATH,"//input[@placeholder='Type']").send_keys("20")
action.send_keys(Keys.TAB).perform()
action.send_keys(Keys.TAB).perform()
driver.implicitly_wait(5)
pyautogui.write("1-1-1", interval=0.05)

action.send_keys(Keys.TAB).perform()
driver.implicitly_wait(5)
pyautogui.write("Before Food", interval=0.05)
action.send_keys(Keys.ENTER).perform()


driver.find_element(By.XPATH,"//p[normalize-space()='0 days']").click()
driver.find_element(By.XPATH,"//input[@placeholder='Number']").clear()
driver.find_element(By.XPATH,"//input[@placeholder='Number']").send_keys("30")
driver.find_element(By.XPATH,"//li[normalize-space()='Days']").click()
action.send_keys(Keys.TAB).perform()
action.send_keys(Keys.TAB).perform()
action.send_keys(Keys.TAB).perform()
action.send_keys(Keys.TAB).perform()
action.send_keys(Keys.ENTER).perform()










