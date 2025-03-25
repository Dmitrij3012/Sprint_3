from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from conftest import *
from curl import *
from locators import Locators


class TestClickToAccount:

    def test_click_to_go_to_personal_account(self, login, driver):
        driver.find_element(*Locators.PERSONAL_ACCOUNT_BUTTON).click()
        WebDriverWait(driver, 3).until(EC.url_to_be(profile))
        assert driver.current_url == profile
