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
    driver.find_element(By.XPATH, "/html/body/form[2]/input").click()
    driver.find_element(By.NAME, "username").click()
    driver.find_element(By.NAME, "username").send_keys("username5")
    driver.find_element(By.NAME, "password").click()
    driver.find_element(By.NAME, "password").send_keys("password5")
    driver.find_element(By.NAME, "passkey").click()
    driver.find_element(By.NAME, "passkey").send_keys("testing555")
    driver.find_element(By.XPATH, "/html/body/form[1]/input[4]").click()
    print("Login page and register page loaded successfully")
except:
    print("Error in register")


