import time

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
driver.find_element(By.CSS_SELECTOR, "#standard-phoneno-input").send_keys("8692057470")
driver.find_element(By.CSS_SELECTOR,"button[type='submit'] span[class='MuiButton-label']").click()
# OTP
driver.find_element(By.CSS_SELECTOR, "input[placeholder='-'][aria-label='Please enter verification code. Digit 1']").send_keys("5746")
driver.find_element(By.XPATH,"//span[normalize-space()='Login OTP']").click()

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
driver.find_element(By.XPATH, "//input[@placeholder='Last Name']").send_keys("Auto")
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

time.sleep(5)
              #*******  Create Paient From Create Appointment ****************


driver.find_element(By.XPATH, "//span[normalize-space()='Appointments']").click()
driver.find_element(By.XPATH, "//span[normalize-space()='My Appointments']").click()
driver.find_element(By.XPATH, "//span[normalize-space()='Create Appointment']").click()
driver.find_element(By.XPATH, "//span[normalize-space()='Add New Patient']").click()

driver.find_element(By.XPATH, "//input[@placeholder='First Name']").send_keys("Test")
driver.find_element(By.XPATH, "//input[@placeholder='Last Name']").send_keys("Auto")
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
driver.find_element(By.XPATH, "(//span[normalize-space()='Save'])[1]").click()

time.sleep(5)

# *******  Create Paient From Daycare ****************



driver.find_element(By.XPATH, "//span[normalize-space()='DayCare']").click()
time.sleep(2)
driver.find_element(By.XPATH, "//span[normalize-space()='Create Appointment']").click()
driver.find_element(By.XPATH, "//span[normalize-space()='Add New Patient']").click()

driver.find_element(By.XPATH, "//input[@placeholder='First Name']").send_keys("Test")
driver.find_element(By.XPATH, "//input[@placeholder='Last Name']").send_keys("Auto")
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

#driver.find_element(By.XPATH, "//button[@aria-label='close']//span[@class='MuiIconButton-label']//*[name()='svg']").click()


driver.find_element(By.XPATH, "//span[normalize-space()='Save']").click()
time.sleep(5)

#*******************  create Patient From Instant Appointment ******************************

driver.find_element(By.XPATH, "//button[@title='Instant EOC Form']//span[@class='MuiIconButton-label']//*[name()='svg']").click()
driver.implicitly_wait(10)
driver.find_element(By.XPATH, "//input[@placeholder='Search/Enter Patient Name']").send_keys("Sagar")
driver.find_element(By.XPATH, "//input[@placeholder='Last Name']").send_keys("Auto")
driver.find_element(By.XPATH, "//input[@name='dateOfBirth']").send_keys("28/12/2000")
driver.find_element(By.XPATH, "//input[@value='Male']").click()
driver.find_element(By.XPATH, "//input[@placeholder='Height']").send_keys("188")
driver.find_element(By.XPATH, "//input[@name='alternetNumber']").send_keys("9999988776")
driver.find_element(By.XPATH, "//input[@placeholder='00-0000-0000-0000']").send_keys("78654567896545")
driver.find_element(By.XPATH, "(//input[@placeholder='Enter Number'])[1]").send_keys("ASDFG3456F")
driver.find_element(By.XPATH, "(//input[@placeholder='Enter Number'])[2]").send_keys("656789898978")
driver.find_element(By.XPATH, "//input[@placeholder='Enter Hospital Id']").send_keys("SAGAR@23454")
driver.find_element(By.XPATH, "//input[@placeholder='Enter Email']").send_keys("SAGARJADHAV8754675@GMAIL.COM")
driver.find_element(By.XPATH, "//input[@placeholder='Plot No. Apartment']").send_keys("Shivshkti Appartment Kalwa")
driver.find_element(By.XPATH, "//input[@placeholder='City, State']").send_keys("Navi Mumbai")
driver.find_element(By.XPATH, "//input[@placeholder='Enter Name']").send_keys("400708")

driver.find_element(By.XPATH, "//input[@placeholder='Enter Referred By']").send_keys("Sagar")
driver.find_element(By.XPATH, "//input[@placeholder='Enter Contact Number']").send_keys("8779271395")
driver.find_element(By.XPATH, "//input[@placeholder='Enter Email Address']").send_keys("SAGARJADHAV8754675@GMAIL.COM")
driver.find_element(By.XPATH, "//input[@placeholder='Enter Address']").send_keys("Kalwa,Thane")
driver.implicitly_wait(10)
driver.find_element(By.XPATH, "//span[normalize-space()='Submit']").click()
time.sleep(2)
driver.find_element(By.XPATH, "//button[@aria-label='close']//span[@class='MuiIconButton-label']//*[name()='svg']").click()
driver.find_element(By.XPATH, "//span[@class='MuiButton-label'][normalize-space()='Appointments']").click()

print("Search Patient, Appointment Patient create, Daycare Create patient All Create patient Working Also Instant Patient Create Working")




