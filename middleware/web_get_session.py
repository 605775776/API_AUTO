from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.chrome.options import Options


options = Options()
options.add_argument('--headless')

driver = webdriver.Chrome(options=options)
# driver = webdriver.Chrome()
driver.get("https://sso.test.klxuexi.net/login")
input_username = (By.XPATH, "//input[@id='username']")
input_password = (By.XPATH, "//input[@id='password']")
input_validateCode = (By.XPATH, "//input[@id='validateCode']")
submit_login = (By.XPATH, "//div[text()='登录']")
WebDriverWait(driver, 10).until(EC.visibility_of_element_located(submit_login))
driver.find_element(*input_username).send_keys('dswen')
driver.find_element(*input_password).send_keys('987858dsw')
driver.find_element(*input_validateCode).send_keys('1278')
driver.find_element(*submit_login).click()

print((str(driver))[-35: -3])
