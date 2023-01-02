import time, os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

chrome_options = Options()

chrome_options.add_argument("--user-agent=Mozilla/5.0 (Linux; Android 13; SM-A205U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.69 Mobile Safari/537.36")
chrome_options.binary_location = "C:\\Program Files\\BraveSoftware\\Brave-Browser\\Application\\brave.exe"
chrome_options.add_argument("--log-level=3")
driver_service = Service(executable_path="C:\\Users\\[your username here]\\.wdm\\drivers\\chromedriver\\win32\\108.0.5359.71\\chromedriver.exe")

wd = webdriver.Chrome(service=driver_service, options=chrome_options, service_log_path="NUL")
timeout = 100

username = input("Username: ")
password = input("Password: ")
new_password = input("New Password: ")

wd.get("https://accounts.spotify.com/en/login?continue=https://www.spotify.com/ph-en/account/change-password/")
WebDriverWait(wd, timeout).until(EC.presence_of_element_located((By.XPATH,'//input[@id="login-username"]')))
wd.find_element(By.XPATH,'//input[@id="login-username"]').send_keys(username)
wd.find_element(By.XPATH,'//input[@id="login-password"]').send_keys(password)
wd.find_element(By.XPATH,'//input[@id="login-password"]').send_keys(Keys.RETURN)
WebDriverWait(wd, timeout).until(EC.presence_of_element_located((By.XPATH,'//input[@id="old_password"]')))
wd.find_element(By.XPATH,'//input[@id="old_password"]').send_keys(password)
WebDriverWait(wd, timeout).until(EC.presence_of_element_located((By.XPATH,'//input[@id="new_password"]')))
wd.find_element(By.XPATH,'//input[@id="new_password"]').send_keys(new_password)
WebDriverWait(wd, timeout).until(EC.presence_of_element_located((By.XPATH,'//input[@id="new_password_confirmation"]')))
wd.find_element(By.XPATH,'//input[@id="new_password_confirmation"]').send_keys(new_password)
wd.find_element(By.XPATH,'//input[@id="new_password_confirmation"]').send_keys(Keys.RETURN)
time.sleep(5)
os.system("cls")
print("Username: ", username)
print("Password: ", new_password)
