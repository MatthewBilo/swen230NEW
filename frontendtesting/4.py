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
    driver.find_element(By.NAME, "password").send_keys("password5v2")
    driver.find_element(By.XPATH, "/html/body/form[1]/input[3]").click()
    driver.find_element(By.XPATH, "/html/body/ul/li[3]/a").click()
    driver.find_element(By.XPATH, "/html/body/div/form/input[1]").click()
    driver.find_element(By.XPATH, "/html/body/div/form/input[1]").send_keys("ITQlaW1nayEqc2shOmtnT2pqZSFtTEdFR0ZNWmw0")
    driver.find_element(By.XPATH, "/html/body/div/form/input[2]").click()
    
    value = driver.find_element(By.XPATH, "/html/body/div/form/input[3]").get_attribute('value')
    if value == "encrypted_text":
        print("Test 4 passed")
    else:
        print("Test 4 failed") 
except:
    print("Test 4 failed")

