from conftest import *
from curl import *
from locators import Locators


class TestClickToMain:

    def test_go_to_constructor(self, login, driver):
        driver.find_element(*Locators.PERSONAL_ACCOUNT_BUTTON).click()
        driver.find_element(*Locators.CONSTRUCTOR).click()
        assert driver.current_url == f'{main_site}/'

    def test_go_by_logo(self, login, driver):
        driver.find_element(*Locators.PERSONAL_ACCOUNT_BUTTON).click()
        driver.find_element(*Locators.LOGO).click()
        assert driver.current_url == f'{main_site}/'
