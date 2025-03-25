from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from conftest import *
from curl import *
from locators import Locators


class TestLogOut:

    def test_log_out_from_account(self, login, driver):
        driver.find_element(*Locators.PERSONAL_ACCOUNT_BUTTON).click()
        WebDriverWait(driver, 3).until(EC.visibility_of_element_located(Locators.LOG_OUT_BUTTON))
        driver.find_element(*Locators.LOG_OUT_BUTTON).click()
        WebDriverWait(driver, 3).until(EC.visibility_of_element_located(Locators.FIELD_EMAIL))
        assert driver.current_url == login_page
