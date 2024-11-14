import time
from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
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
driver.implicitly_wait(10)
driver.find_element(By.XPATH,"//span[normalize-space()='OK']").click()

# create Patient From All Patient
driver.find_element(By.XPATH, "//span[normalize-space()='All Patients']").click()
driver.find_element(By.XPATH, "//span[(text() = 'Search Patients' or . = 'Search Patients')]").click()
driver.find_element(By.XPATH, "//span[@class='MuiFab-label']//*[name()='svg']").click()
#fill patient Data

                           #********** Change Name Of Patient ********************  one C

driver.find_element(By.XPATH, "//input[@placeholder='First Name']").send_keys("Test")
driver.find_element(By.XPATH, "//input[@placeholder='Last Name']").send_keys("Three")
driver.find_element(By.XPATH, "//input[@placeholder='Select Date']").send_keys("28/12/2000")
driver.find_element(By.XPATH, "//p[normalize-space()='Male']").click()
driver.find_element(By.XPATH, "//input[@placeholder='Plot No. Apartment']").send_keys("mumbai")
driver.find_element(By.XPATH, "//input[@placeholder='City']").send_keys("Thane")


                           # ********** Change contact Number Of Patent ********************


driver.find_element(By.XPATH, "//input[@name='contactNumber']").send_keys("")
driver.find_element(By.XPATH, "//input[@name='alternetNumber']").send_keys("9999999999")
driver.find_element(By.XPATH, "//input[@placeholder='Enter Email']").send_keys("Sagarjadhav1522@gmail.com")
driver.find_element(By.XPATH, "//input[@placeholder='00-0000-0000-0000']").send_keys("98765654312342")
driver.find_element(By.XPATH, "//input[@name='panNumber']").send_keys("DFGVF3456D")
driver.find_element(By.XPATH, "//input[@name='aadharNumber']").send_keys("676545654321")
driver.find_element(By.XPATH, "//input[@placeholder='Enter Hospital Id']").send_keys("ASD1234")
driver.find_element(By.XPATH, "//input[@name='sendInvite']").click()
driver.find_element(By.XPATH, "//span[normalize-space()='Save']").click()
driver.implicitly_wait(10)
time.sleep(5)


#   Create Appointment

driver.find_element(By.XPATH,"//span[normalize-space()='Appointments']").click()
driver.find_element(By.XPATH, "//span[normalize-space()='My Appointments']").click()
driver.find_element(By.XPATH, "//span[normalize-space()='Create Appointment']").click()
driver.find_element(By.XPATH,"//input[@id='patientSearch']").send_keys("Test Three")
