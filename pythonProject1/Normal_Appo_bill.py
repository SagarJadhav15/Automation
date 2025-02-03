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




# create Patient From All Patient
driver.find_element(By.XPATH, "//span[normalize-space()='All Patients']").click()
driver.find_element(By.XPATH, "//span[(text() = 'Search Patients' or . = 'Search Patients')]").click()
driver.find_element(By.XPATH, "//span[@class='MuiFab-label']//*[name()='svg']").click()
#fill patient Data

                           #********** Change Name Of Patient ********************  one C

driver.find_element(By.XPATH, "//input[@placeholder='First Name']").send_keys("Test")
driver.find_element(By.XPATH, "//input[@placeholder='Last Name']").send_keys("Autoseven")
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
time.sleep(10)
driver.implicitly_wait(50)



#   Create Appointment

driver.find_element(By.XPATH,"//span[normalize-space()='Appointments']").click()
driver.find_element(By.XPATH, "//span[normalize-space()='My Appointments']").click()
driver.find_element(By.XPATH, "//span[normalize-space()='Create Appointment']").click()
driver.find_element(By.XPATH,"//input[@id='patientSearch']").send_keys("Test Autoseven")
time.sleep(5)
action = webdriver.ActionChains(driver)
action.send_keys(Keys.ARROW_DOWN).perform()
action.send_keys(Keys.ENTER).perform()
driver.find_element(By.XPATH,"//input[@id='appointmentTimeSlot']").click()
driver.find_element(By.XPATH,"//p[normalize-space()='Instant']").click()
driver.find_element(By.XPATH,"//input[@id='reasonForAdmission']").send_keys("Initial Consultation")
driver.find_element(By.XPATH,"//textarea[@id='comment']").send_keys("Initial Consultation For General Appointment")
driver.implicitly_wait(5)
'''driver.find_element(By.XPATH,"//input[@placeholder='Enter Referred By']").clear()
driver.find_element(By.XPATH,"//input[@placeholder='Enter Referred By']").send_keys("Sagar")
driver.find_element(By.XPATH,"//input[@placeholder='Enter Contact Number']").clear()
driver.find_element(By.XPATH,"//input[@placeholder='Enter Contact Number']").send_keys("8779271395")
driver.find_element(By.XPATH,"//input[@placeholder='Enter Email Address']").clear()
driver.find_element(By.XPATH,"//input[@placeholder='Enter Email Address']").send_keys("Sagarjadhav61679@gmail.com")
driver.find_element(By.XPATH,"//input[@placeholder='Enter Value']").clear()
driver.find_element(By.XPATH,"//input[@placeholder='Enter Value']").send_keys("Navi Mumbai")'''
driver.find_element(By.XPATH,"//span[normalize-space()='Submit']").click()


#Fill EOC

driver.find_element(By.XPATH,"//div[@id='BasicDetails']//div[@id='panel1bh-header']").click()
driver.find_element(By.XPATH,"//input[@placeholder='Height']").send_keys("177")
driver.find_element(By.XPATH,"//input[@id='occupation']").send_keys("Actor")
driver.find_element(By.XPATH,"//input[@id='maritalStatus']").send_keys("Unmarried")
driver.find_element(By.XPATH,"//input[@id='bloodGroup']").send_keys("O+")
driver.find_element(By.XPATH,"//input[@placeholder='Plot No. Apartment']").send_keys("Ishwar Nagar Digha Kalwa")
driver.find_element(By.XPATH,"//input[@name='pincode']").send_keys("400708")
driver.find_element(By.XPATH,"//input[@name='nameOfInsured']").send_keys("Tata")
driver.find_element(By.XPATH,"//input[@id='providerName']").send_keys("Ratan Tata")
driver.find_element(By.XPATH,"//input[@placeholder='0000-0000-0000-0000']").send_keys("8888-9999-0000-1111")

time.sleep(2)
driver.find_element(By.XPATH,"//div[@id='Vitals']//div[@id='panel1bh-header']").click()
time.sleep(2)

#Vital
driver.find_element(By.XPATH,"//body[1]/div[2]/div[3]/div[1]/form[1]/div[1]/div[3]/div[1]/div[2]/div[1]/div[2]/div[2]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/table[1]/tbody[1]/tr[1]/td[2]/div[1]/div[1]/input[1]").send_keys("68")
driver.find_element(By.XPATH,"//body[1]/div[2]/div[3]/div[1]/form[1]/div[1]/div[3]/div[1]/div[2]/div[1]/div[2]/div[2]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/table[1]/tbody[1]/tr[1]/td[3]/div[1]/div[1]/input[1]").send_keys("120/68")
driver.find_element(By.XPATH,"//body[1]/div[2]/div[3]/div[1]/form[1]/div[1]/div[3]/div[1]/div[2]/div[1]/div[2]/div[2]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/table[1]/tbody[1]/tr[1]/td[4]/div[1]/div[1]/input[1]").send_keys("70")
driver.find_element(By.XPATH,"//body[1]/div[2]/div[3]/div[1]/form[1]/div[1]/div[3]/div[1]/div[2]/div[1]/div[2]/div[2]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/table[1]/tbody[1]/tr[1]/td[5]/div[1]/div[1]/input[1]").send_keys("95")
driver.find_element(By.XPATH,"//body[1]/div[2]/div[3]/div[1]/form[1]/div[1]/div[3]/div[1]/div[2]/div[1]/div[2]/div[2]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/table[1]/tbody[1]/tr[1]/td[6]/div[1]/div[1]/input[1]").send_keys("100")
driver.find_element(By.XPATH,"//body[1]/div[2]/div[3]/div[1]/form[1]/div[1]/div[3]/div[1]/div[2]/div[1]/div[2]/div[2]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/table[1]/tbody[1]/tr[1]/td[7]/div[1]/div[1]/input[1]").send_keys("25")
driver.find_element(By.XPATH,"//body[1]/div[2]/div[3]/div[1]/form[1]/div[1]/div[3]/div[1]/div[2]/div[1]/div[2]/div[2]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/table[1]/tbody[1]/tr[1]/td[8]/div[1]/div[1]/input[1]").send_keys("68")
driver.find_element(By.XPATH,"//textarea[@name='vitalNote']").send_keys("Normal vitals Report")



driver.implicitly_wait(20)
#Medical History
#Comorbidity


driver.find_element(By.XPATH,"//div[@name='comorbid-1']//div[@class='MuiInputBase-root MuiOutlinedInput-root MuiAutocomplete-inputRoot MuiInputBase-fullWidth MuiInputBase-formControl MuiInputBase-adornedEnd MuiOutlinedInput-adornedEnd MuiInputBase-marginDense MuiOutlinedInput-marginDense']").click()

time.sleep(5)
driver.find_element(By.XPATH,"//p[normalize-space()='COPD']").click()
driver.implicitly_wait(20)
pyautogui.write("COPD Normal", interval=0.05)  # Adjust interval for typing speed

#Allergy
driver.find_element(By.XPATH,"//input[@id='allergy-1']").click()
action = webdriver.ActionChains(driver)
action.send_keys(Keys.ARROW_UP).perform()
driver.implicitly_wait(10)
action.send_keys(Keys.ENTER).perform()
pyautogui.write("(Sulfa Drugs) Allergy", interval=0.05)  # Adjust interval for typing speed


#Chief Complaint
driver.find_element(By.XPATH,"//p[normalize-space()='Abdominal Distension']").click()
driver.implicitly_wait(10)
driver.find_element(By.XPATH,"//li[@id='severity0']//input[@type='radio']").click()
driver.find_element(By.XPATH,"//li[normalize-space()='Once A Day']//input[@type='radio']").click()
driver.find_element(By.XPATH,"//p[normalize-space()='2']").click()
driver.find_element(By.XPATH,"//p[normalize-space()='Days']").click()
driver.find_element(By.XPATH,"//span[normalize-space()='Done']").click()


'''#past history
driver.find_element(By.XPATH,"//div[@id='PastHistory']//div[@class='MuiGrid-root MuiGrid-container MuiGrid-align-items-xs-center']").click()
driver.find_element(By.XPATH,"//input[@id='select-1' and @placeholder='Select Treatment Type']").send_keys("surgery")
action.send_keys(Keys.ARROW_DOWN).perform()
action.send_keys(Keys.ENTER).perform()
driver.implicitly_wait(10)

driver.find_element(By.XPATH,"//input[@placeholder='Date']").send_keys("12/12/2024")
driver.find_element(By.XPATH,"//textarea[@placeholder='Enter Brief Note']")
driver.find_element(By.XPATH,"//div[@class='MuiBox-root jss1053']//button[@type='button']").click()

'''


#past history
#Type Of Treatment
driver.find_element(By.XPATH,"//div[@id='PastHistory']//div[@class='MuiGrid-root MuiGrid-container MuiGrid-align-items-xs-center']").click()

driver.find_element(By.XPATH,"//input[@id='select-1' and @placeholder='Select Treatment Type']").send_keys("surgery")

action = webdriver.ActionChains(driver)
action.send_keys(Keys.ARROW_DOWN).perform()
action.send_keys(Keys.ENTER).perform()
driver.find_element(By.XPATH,"//input[@placeholder='Date']").send_keys("12/12/2012")
driver.implicitly_wait(10)
action.send_keys(Keys.TAB).perform()
pyautogui.write("Throte Surgery", interval=0.05)
action.send_keys(Keys.TAB).perform()
pyautogui.write("Positive Surgery", interval=0.05)

action.send_keys(Keys.TAB).perform()
action.send_keys(Keys.TAB).perform()
action.send_keys(Keys.TAB).perform()

#Family History

time.sleep(2)
driver.find_element(By.XPATH,"//input[@id='selectOne-1' and @placeholder='Select Relation']").send_keys("paternal grandmother")
driver.implicitly_wait(10)
action.send_keys(Keys.ARROW_DOWN).perform()
driver.implicitly_wait(10)
action.send_keys(Keys.ENTER).perform()
driver.implicitly_wait(20)
action.send_keys(Keys.ENTER).send_keys("Lung Cancer").perform()
action.send_keys(Keys.ARROW_DOWN).perform()
action.send_keys(Keys.ENTER).perform()
action.send_keys(Keys.TAB).send_keys("53").perform()
driver.implicitly_wait(10)
action.send_keys(Keys.TAB).perform()
driver.implicitly_wait(5)
action.send_keys(Keys.TAB).perform()
driver.implicitly_wait(5)
action.send_keys(Keys.TAB).perform()
driver.implicitly_wait(5)




#Past Hospitalization Pertaining To Present Illness


action.send_keys(Keys.TAB).perform()
pyautogui.write("recurrent kidney stones presenting with severe flank pain", interval=0.05)
action.send_keys(Keys.ENTER).perform()
driver.find_element(By.XPATH,"//input[contains(@placeholder,'Month: Year')]").send_keys("122009")
driver.implicitly_wait(5)
driver.find_element(By.XPATH,"//input[@placeholder='Enter Note']").click()
pyautogui.write("having been hospitalized for a similar episode of kidney stone passage a year prior", interval=0.05)



#Past Hospitalization Other Illness


driver.find_element(By.XPATH,"(//input[@placeholder='Reason For Hospitalization'])[1]").send_keys("Eye irritationRunny noseStuffy nosePuffy, watery eyes")
action.send_keys(Keys.ENTER).perform()
driver.find_element(By.XPATH,"//input[contains(@placeholder,'Month: Year')]").send_keys("112010")
driver.implicitly_wait(5)
driver.find_element(By.XPATH,"//input[@placeholder='Enter Note']").click()
pyautogui.write("these illnesses are upper respiratory infections, meaning they involve your nose, throat, and lungs.", interval=0.05)


#Repoartsssssssssssss 1st

time.sleep(2)
driver.find_element(By.XPATH,"//div[@id='Reports']//div[@class='MuiGrid-root MuiGrid-container MuiGrid-align-items-xs-center']").click()
#driver.find_element(By.XPATH,"(//button[@title='Open'])[13]").send_keys("CT CHEST")
driver.find_element(By.CSS_SELECTOR, "input[placeholder='Select Test']").send_keys("CT CHEST")
driver.implicitly_wait(10)
action.send_keys(Keys.ARROW_DOWN).perform()
action.send_keys(Keys.ENTER).perform()
driver.find_element(By.XPATH,"//input[@placeholder='Date']").send_keys("22/12/2001")
time.sleep(2)
action.send_keys(Keys.TAB).perform()
pyautogui.write("The lungs and airways are normal, The heart is normal in size.", interval=0.05)
action.send_keys(Keys.TAB).perform()
pyautogui.write("Findings: Lungs and airways are normal, heart size is normal, no pleural effusion, no pericardial effusion, and the chest wall is unremarkable.", interval=0.05)

action.send_keys(Keys.TAB).perform()
action.send_keys(Keys.TAB).perform()
action.send_keys(Keys.TAB).perform()

#2nd*************
pyautogui.write("MAMMOGRAPHY BOTH BREASTS", interval=0.05)
action.send_keys(Keys.ARROW_DOWN).perform()
action.send_keys(Keys.ENTER).perform()



driver.implicitly_wait(10)
action.send_keys(Keys.ARROW_DOWN).perform()
action.send_keys(Keys.ENTER).perform()
driver.find_element(By.XPATH,"//input[@placeholder='Date']").send_keys("12/09/2002")

action.send_keys(Keys.TAB).perform()
pyautogui.write("Positive", interval=0.05)
action.send_keys(Keys.TAB).perform()
pyautogui.write("A mass may refer to a tumor", interval=0.05)

action.send_keys(Keys.TAB).perform()
action.send_keys(Keys.TAB).perform()
action.send_keys(Keys.TAB).perform()

#3rd*******************
pyautogui.write("MAMMOGRAPHY SINGLE BREAST", interval=0.05)
action.send_keys(Keys.ARROW_DOWN).perform()
action.send_keys(Keys.ENTER).perform()

driver.implicitly_wait(10)
action.send_keys(Keys.ARROW_DOWN).perform()
action.send_keys(Keys.ENTER).perform()
driver.find_element(By.XPATH,"//input[@placeholder='Date']").send_keys("12/09/2003")

action.send_keys(Keys.TAB).perform()
pyautogui.write("Positive", interval=0.05)
action.send_keys(Keys.TAB).perform()
pyautogui.write("A mass may refer to a tumor", interval=0.05)

action.send_keys(Keys.TAB).perform()
action.send_keys(Keys.TAB).perform()
action.send_keys(Keys.TAB).perform()


#4th **********************
pyautogui.write("ESTROGEN RECEPTOR AG", interval=0.05)
action.send_keys(Keys.ARROW_DOWN).perform()
action.send_keys(Keys.ENTER).perform()

driver.implicitly_wait(10)
action.send_keys(Keys.ARROW_DOWN).perform()
action.send_keys(Keys.ENTER).perform()
driver.find_element(By.XPATH,"//input[@placeholder='Date']").send_keys("12/09/2004")

action.send_keys(Keys.TAB).perform()
pyautogui.write("33", interval=0.05)
action.send_keys(Keys.TAB).perform()
pyautogui.write("α and β, that are encoded by two different genes.", interval=0.05)

action.send_keys(Keys.TAB).perform()
action.send_keys(Keys.TAB).perform()
action.send_keys(Keys.TAB).perform()


#5th **********************
pyautogui.write("SQUAMOUS CELL CARCINOMA AG", interval=0.05)
action.send_keys(Keys.ARROW_DOWN).perform()
action.send_keys(Keys.ENTER).perform()

driver.implicitly_wait(10)
action.send_keys(Keys.ARROW_DOWN).perform()
action.send_keys(Keys.ENTER).perform()
driver.find_element(By.XPATH,"//input[@placeholder='Date']").send_keys("12/09/2005")

action.send_keys(Keys.TAB).perform()
pyautogui.write("67", interval=0.05)
action.send_keys(Keys.TAB).perform()
pyautogui.write("a protein marker detected in blood tests that can indicate the presence of squamous cell.", interval=0.05)

action.send_keys(Keys.TAB).perform()
action.send_keys(Keys.TAB).perform()
action.send_keys(Keys.TAB).perform()

#6th **********************
pyautogui.write("CARCINOEMBRYONIC AG", interval=0.05)
action.send_keys(Keys.ARROW_DOWN).perform()
action.send_keys(Keys.ENTER).perform()

driver.implicitly_wait(10)
action.send_keys(Keys.ARROW_DOWN).perform()
action.send_keys(Keys.ENTER).perform()
driver.find_element(By.XPATH,"//input[@placeholder='Date']").send_keys("12/09/2006")

action.send_keys(Keys.TAB).perform()
pyautogui.write("89", interval=0.05)
action.send_keys(Keys.TAB).perform()
pyautogui.write("Carcinoembryonic antigen (CEA) is a protein that can be used to help identify cancer.", interval=0.05)

action.send_keys(Keys.TAB).perform()
action.send_keys(Keys.TAB).perform()
action.send_keys(Keys.TAB).perform()


#personal history ******************
#Immunization
driver.find_element(By.XPATH,"//div[@id='PersonalHistory']//div[@class='MuiGrid-root MuiGrid-container MuiGrid-align-items-xs-center']").click()
driver.find_element(By.XPATH,"//div[@name='immunization-1']//input[@id='select-1']").send_keys("COVISHIELD")
action.send_keys(Keys.ARROW_DOWN).perform()
action.send_keys(Keys.ENTER).perform()
#2nd
driver.find_element(By.XPATH,"//div[@name='immunization-3']//input[@id='select-3']").send_keys("anthrax immune globulin  ")
action.send_keys(Keys.ARROW_DOWN).perform()
action.send_keys(Keys.ENTER).perform()


#Tobacco Consumption

driver.find_element(By.XPATH,"//input[@id='tobacco-1']").send_keys("Cigarette")
action.send_keys(Keys.ARROW_DOWN).perform()
action.send_keys(Keys.ENTER).perform()
time.sleep(2)
pyautogui.write("2", interval=0.05)
driver.find_element(By.XPATH,"//li[normalize-space()='Per day']").click()
action.send_keys(Keys.ENTER).perform()
time.sleep(2)
action.send_keys(Keys.TAB).perform()
pyautogui.write("3", interval=0.05)
driver.find_element(By.XPATH,"//li[normalize-space()='Weeks']").click()
action.send_keys(Keys.ENTER).perform()

#Alcohol Consumption

driver.find_element(By.XPATH,"//body[1]/div[2]/div[3]/div[1]/form[1]/div[1]/div[3]/div[1]/div[2]/div[1]/div[2]/div[8]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[3]/div[1]/div[1]/div[2]/div[1]/div[1]/fieldset[1]/div[1]/label[1]/span[1]/span[1]/input[1]").click()
pyautogui.write("4", interval=0.05)
driver.find_element(By.XPATH,"//li[normalize-space()='Per day']").click()
action.send_keys(Keys.ENTER).perform()
time.sleep(2)
action.send_keys(Keys.TAB).perform()
pyautogui.write("7", interval=0.05)
driver.find_element(By.XPATH,"//li[normalize-space()='Weeks']").click()
action.send_keys(Keys.ENTER).perform()


#Drug Consumption


driver.find_element(By.XPATH,"//input[@value='Yes']").click()
pyautogui.write("2", interval=0.05)
driver.find_element(By.XPATH,"//li[normalize-space()='Per day']").click()
action.send_keys(Keys.ENTER).perform()
time.sleep(2)
action.send_keys(Keys.TAB).perform()
pyautogui.write("3", interval=0.05)
driver.find_element(By.XPATH,"//li[normalize-space()='Weeks']").click()
action.send_keys(Keys.ENTER).perform()

#Diet Type

driver.find_element(By.XPATH,"//input[@id='diet']").send_keys("Non Vegetarian")
action.send_keys(Keys.ARROW_DOWN).perform()
action.send_keys(Keys.ENTER).perform()

#Generate HOPI using our
driver.find_element(By.XPATH,"//div[@id='HistoryOfPresentIllness']//div[@class='MuiGrid-root MuiGrid-container MuiGrid-align-items-xs-center']").click()
driver.find_element(By.XPATH,"//span[normalize-space()='Intelligent HOPI Generator?']").click()
driver.implicitly_wait(30)

driver.find_element(By.XPATH,"/html/body/div[5]/div[3]/div/div/div[2]/div/div[1]/div/div[2]/div/div[3]/button/span[1]").click()

#General Examination

driver.find_element(By.XPATH,"//div[@id='GeneralExamination']//div[@class='MuiGrid-root MuiGrid-container MuiGrid-align-items-xs-center']").click()

driver.find_element(By.XPATH,"//input[@aria-label='Icterus']").click()
pyautogui.write("Positive", interval=0.05)

driver.find_element(By.XPATH,"//input[@aria-label='Pallor']").click()
pyautogui.write("Positive", interval=0.05)

driver.find_element(By.XPATH,"//input[@aria-label='Clubbing']").click()
pyautogui.write("Positive", interval=0.05)

driver.find_element(By.XPATH,"//input[@aria-label='Cyanosis']").click()
pyautogui.write("Positive", interval=0.05)

driver.find_element(By.XPATH,"//input[@aria-label='Oedema']").click()
pyautogui.write("Positive", interval=0.05)

driver.find_element(By.XPATH,"//input[@aria-label='Lymphadenopathy']").click()
pyautogui.write("Positive", interval=0.05)

driver.implicitly_wait(5)
#Systemic Examination

driver.find_element(By.XPATH,"//input[@name='cns']").send_keys("Positive")
driver.find_element(By.XPATH,"//input[@name='cvs']").send_keys("Positive")
driver.find_element(By.XPATH,"//input[@name='respiratory']").send_keys("Positive")
driver.find_element(By.XPATH,"//input[@name='perAbdomen']").send_keys("Positive")

driver.implicitly_wait(5)
#Local Examination
driver.find_element(By.XPATH,"//input[@name='inspection']").send_keys("Positive")
driver.find_element(By.XPATH,"//input[@name='palpation']").send_keys("Positive")
driver.implicitly_wait(5)

#Clinical Findings
driver.find_element(By.XPATH,"//textarea[@name='clinicalFinding']").send_keys(" Asthma (disorder) Headache (Finding)")

driver.implicitly_wait(5)

#Diagnosis/Impression For Visit

driver.find_element(By.XPATH,"//div[@id='ImpressionForVisit-Diagnosis']//div[@class='MuiGrid-root MuiGrid-container MuiGrid-align-items-xs-center']").click()
driver.find_element(By.XPATH,"//p[normalize-space()='Upper Respiratory Tract Infection']").click()


#Advice

driver.find_element(By.XPATH,"//div[@id='Advice-Tests']//div[@class='MuiGrid-root MuiGrid-container MuiGrid-align-items-xs-center']").click()


driver.find_element(By.XPATH,"(//input[@id='select-1'])[5]").send_keys("CT CHEST")
time.sleep(2)
action.send_keys(Keys.ARROW_DOWN).perform()
action.send_keys(Keys.ENTER).perform()

driver.find_element(By.XPATH,"(//input[@id='select-1'])[5]").send_keys("SEX HORMONE BINDING GLOBULIN")
action.send_keys(Keys.ARROW_DOWN).perform()
action.send_keys(Keys.ENTER).perform()
driver.find_element(By.XPATH,"(//input[@id='adviceReportedBy-0'])[1]").send_keys("Positive")


#Treatment Plan

driver.find_element(By.XPATH,"//div[@id='TreatmentPlan']//div[@class='MuiGrid-root MuiGrid-container MuiGrid-align-items-xs-center']").send_keys("Radiation therapy")

driver.find_element(By.XPATH,"//input[@id='select-1' and @placeholder='Select Treatment']").send_keys("Radiation therapy")
driver.find_element(By.XPATH,"//textarea[@name='treatmentProcedure']").send_keys("Uses energy beams to treat cancer")








