import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
options = Options()
options.add_experimental_option("detach", True)
# Set up Selenium WebDriver
driver = webdriver.Chrome(options=options)
# Open the website
driver.get("https://msc-project-git-demo-sagars-projects-1577e7b0.vercel.app?_vercel_share=xR9n0TNxXBNm9fwTUOTm9wdTWVi0JwCO ")
driver.maximize_window()
driver.implicitly_wait(10)
time.sleep(3)
driver.find_element(By.XPATH,"/html/body/header/nav/a[2]").click()
time.sleep(3)
driver.find_element(By.XPATH,"/html/body/section[2]/div/div[1]/a[2]/img").click()
time.sleep(3)
driver.find_element(By.XPATH,"/html/body/section[1]/div/div/a[1]").click()
time.sleep(3)
driver.find_element(By.XPATH,"/html/body/header/div/a[2]").click()
driver.find_element(By.XPATH,"/html/body/div[1]/button[1]").click()
driver.find_element(By.XPATH,"/html/body/section/form/div[1]/div[1]/input").send_keys("Sagar Sanjay Jadhav")
driver.find_element(By.XPATH,"/html/body/section/form/div[1]/div[2]/input").send_keys("8779271395")
driver.find_element(By.XPATH,"/html/body/section/form/div[2]/div[1]/input").send_keys("2")
driver.find_element(By.XPATH,"/html/body/section/form/div[2]/div[2]/input").send_keys("22/08/2024")
driver.find_element(By.XPATH,"/html/body/section/form/div[3]/div[1]/textarea").send_keys("Ishwar Nagar Digha Navi Mumbai Thane 400708.")
driver.find_element(By.XPATH,"/html/body/section/form/div[4]/div/div/input").click()
driver.find_element(By.XPATH,"/html/body/section/form/div[5]/a").click()

time.sleep(3)
driver.find_element(By.XPATH,"/html/body/header/nav/a[2]").click()
time.sleep(3)
driver.find_element(By.XPATH,"/html/body/header/nav/a[3]").click()
time.sleep(3)
driver.find_element(By.XPATH,"/html/body/header/nav/a[4]").click()
time.sleep(3)
driver.find_element(By.XPATH,"/html/body/header/nav/a[5]").click()
time.sleep(3)
driver.find_element(By.XPATH,"/html/body/header/a/img").click()


print("Happy Flow Working Fine")
quit()




