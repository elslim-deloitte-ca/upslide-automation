import json
import os
from datetime import datetime
import time
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

# Steps back one folder from scripts to project root
os.chdir('../')

# Sets variables and configurations for bot
with open(r'config/upslide-credentials.json') as jsonFile:
    content = json.load(jsonFile)
    USERNAME = content['USER']
    PASSWORD = content['PASSWORD']
    DOWNLOAD = os.getcwd() + r"\data\raw\license"

options = Options()
options.add_argument('--headless')
options.add_argument('--lang=en')
options.add_argument('--no-sandbox')
options.add_argument('--disable-gpu')
options.add_argument('--disable-dev-shm-usage')
options.add_argument('--disable-software-rasterizer')
chrome_prefs = {}
chrome_prefs["profile.default_content_settings"] = {"images": 2}
chrome_prefs["profile.managed_default_content_settings"] = {"images": 2}
chrome_prefs["download.default_directory"] = DOWNLOAD
options.experimental_options["prefs"] = chrome_prefs

# Navigate to Upslide login page
driver = webdriver.Chrome(r'chromedriver', options=options)
wait = WebDriverWait(driver, 5)
driver.get("https://portal.upslide.net/")

# Find login form fields
try:
    wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "css-3z6pvx")))
    formELEMS = driver.find_elements(By.CLASS_NAME, "css-3z6pvx")
    userInputELEM = formELEMS[0]
    passwordInputELEM = formELEMS[1]

except TimeoutException:
    print("Timeout - Login Page")

# Enter login details
try:
    userInputELEM.send_keys(USERNAME)
    passwordInputELEM.send_keys(PASSWORD)
    passwordInputELEM.submit()
except TimeoutException:
    print("Timeout - Login Info")

# Click on Users side tab
try:
    wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "css-1npapst")))
    userTabELEM = driver.find_element(By.LINK_TEXT, "Users")
    userTabELEM.click()

except TimeoutException:
    print("Timeout - User Tab")


# Click export
try:
    wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "css-3n3atf")))
    exportELEMS = driver.find_elements(By.CLASS_NAME, "css-3n3atf")
    exportELEM = exportELEMS[0]
    exportELEM.click()

except TimeoutException:
    print("Timeout - Export")

# Click .csv
try:
    wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "css-1uxj2x3")))
    downloadELEMS = driver.find_elements(By.CLASS_NAME, "css-1uxj2x3")
    csvELEM = downloadELEMS[1]
    csvELEM.click()
    time.sleep(3)

except TimeoutException:
    print("Timeout - Download")

# Rename downloaded file
downloadTS = datetime.now().strftime("%Y_%m_%d")
if "users.csv" in os.listdir(DOWNLOAD):
    downloadTS = datetime.now().strftime("%Y_%m_%d")
    if f"{DOWNLOAD}/licenses_{downloadTS}.csv" not in os.listdir(DOWNLOAD):
        os.rename(f"{DOWNLOAD}/users.csv", f"{DOWNLOAD}/licenses_{downloadTS}.csv")

driver.close()
