import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities


driver = webdriver.Chrome()
driver.get("http://localhost:9090")
try:
    driver.find_element(By.XPATH, "/html/body/form[1]/input[1]").click()
    driver.find_element(By.NAME, "username").click()
    driver.find_element(By.NAME, "username").send_keys("username5")
    driver.find_element(By.NAME, "password").click()
    driver.find_element(By.NAME, "password").send_keys("WRONGPASSWORD")
    driver.find_element(By.XPATH, "/html/body/form[1]/input[3]").click()
    element = driver.find_element(By.XPATH, "/html/body/p")
    if(element.text == "Wrong password"):
        print("Test 7a passed")
    else:
        print("Test 7a failed")
    driver.find_element(By.NAME, "username").click()
    driver.find_element(By.NAME, "username").send_keys("WRONGUSERNAME")
    driver.find_element(By.NAME, "password").click()
    driver.find_element(By.NAME, "password").send_keys("password5v2")
    driver.find_element(By.XPATH, "/html/body/form[1]/input[3]").click()
    element = driver.find_element(By.XPATH, "/html/body/p")
    if(element.text == "Wrong username"):
        print("Test 7b passed")
    else:
        print("Test 7b failed")
except:
    print("Test 7 failed")   