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
driver.implicitly_wait(30)
driver.find_element(By.XPATH,"//span[normalize-space()='OK']").click()
