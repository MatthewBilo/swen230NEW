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
import warnings
from urllib3.exceptions import InsecureRequestWarning

warnings.simplefilter('ignore', category=InsecureRequestWarning)


driver = webdriver.Chrome()
driver.get("http://localhost:9090")
try:
    driver.find_element(By.XPATH, "/html/body/form[2]/input").click()
    driver.find_element(By.XPATH, "/html/body/form[1]/input[1]").click()
    driver.find_element(By.XPATH, "/html/body/form[1]/input[1]").send_keys("username5")
    driver.find_element(By.XPATH, "/html/body/form[1]/input[2]").click()
    driver.find_element(By.XPATH, "/html/body/form[1]/input[2]").send_keys("password5")
    driver.find_element(By.XPATH, "/html/body/form[1]/input[3]").click()
    driver.find_element(By.XPATH, "/html/body/form[1]/input[3]").send_keys("testing555")
    driver.find_element(By.XPATH, "/html/body/form[1]/input[4]").click()
    print("Login page and register page loaded successfully")
except:
    print("Error in register")


