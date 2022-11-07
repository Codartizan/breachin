
import base64

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

driver = None
username = "timshi2013@gmail.com"
# username = "tim.shi@telephant.co.nz"
password = "SinCosTan1987"


for i in range(50):
    try:
        driver = webdriver.Safari()
        wait = WebDriverWait(driver, 20)
        driver.get("https://github.com/settings/tokens")
        driver.find_element(By.ID, 'login_field').send_keys(username)
        driver.find_element(By.ID, "password").send_keys(password)
        driver.find_element(By.CSS_SELECTOR, "[type='submit']").click()

        wait.until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, "#js-pjax-container > "
                                                                                       "div.pt-4.container-xl.p"
                                                                                       "-responsive > div > "
                                                                                       "div.Layout-main > div > div > "
                                                                                       "div.settings-next > "
                                                                                       "div.Subhead > div > a")))

        driver.find_element(By.CSS_SELECTOR, "#js-pjax-container > div.pt-4.container-xl.p-responsive > div > "
                                             "div.Layout-main > div > div > div.settings-next > div.Subhead > div > "
                                             "a").click()

        wait.until(expected_conditions.visibility_of_element_located((By.ID, 'oauth_access_description')))

        driver.find_element(By.ID, 'oauth_access_description').send_keys('Autogen{}'.format(i))

        driver.find_element(By.CSS_SELECTOR, "#new_oauth_access > p > button").click()

        wait.until(expected_conditions.visibility_of_element_located((By.ID, 'new-oauth-token')))

        token = driver.find_element(By.ID, "new-oauth-token").text

        print(str(base64.b64encode(token.encode())).removeprefix('b') + ',')

    finally:
        if driver is not None:
            driver.quit()
