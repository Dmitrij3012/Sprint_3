from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from conftest import *
from curl import *
from locators import Locators
import helper


class TestRegistration:

    def test_registration_with_correct_login_and_password(self, driver):
        name, email, password = helper.generate_registration_data()

        driver.get(register)
        driver.find_element(*Locators.NAME).send_keys(name)
        driver.find_element(*Locators.EMAIL).send_keys(email)
        driver.find_element(*Locators.PASSWORD).send_keys(password)
        driver.find_element(*Locators.REGISTRATION_BUTTON).click()
        WebDriverWait(driver, 3).until(EC.visibility_of_element_located(Locators.LOGIN_BUTTON))
        assert driver.current_url == login_page

    def test_registration_with_incorrect_password(self, driver):
        name, email, incorrect_password = helper.generate_registration_data_incorrect_password()

        driver.get(register)
        driver.find_element(*Locators.NAME).send_keys(name)
        driver.find_element(*Locators.EMAIL).send_keys(email)
        driver.find_element(*Locators.PASSWORD).send_keys(incorrect_password)
        driver.find_element(*Locators.REGISTRATION_BUTTON).click()
        error_message = (WebDriverWait(driver, 3).until(
            EC.visibility_of_element_located(Locators.PASSWORD_ERROR_MESSAGE)).text)
        assert error_message == 'Некорректный пароль'
