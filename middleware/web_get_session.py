from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.chrome.options import Options


class Web_Get_Session:
    input_username = (By.XPATH, "//input[@id='username']")
    input_password = (By.XPATH, "//input[@id='password']")
    input_validateCode = (By.XPATH, "//input[@id='validateCode']")
    submit_login = (By.XPATH, "//div[text()='登录']")
    options = Options()
    options.add_argument('--headless')

    def web_get_session(self):
        driver = webdriver.Chrome(options=self.options)
        driver.get("url")
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(self.submit_login))
        driver.find_element(*self.input_username).send_keys('username')
        driver.find_element(*self.input_password).send_keys('password')
        driver.find_element(*self.input_validateCode).send_keys('validateCode')
        driver.find_element(*self.submit_login).click()
        return driver


if __name__ == '__main__':
    driver = webdriver
    a = Web_Get_Session().web_get_session()
    print(a)