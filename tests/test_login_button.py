from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from conftest import *
from curl import *
from data import Credentials
from locators import Locators


class TestLoginButton:

    def test_login_main_page_login_to_account_button(self, driver):
        driver.get(main_site)
        driver.find_element(*Locators.LOGIN_BUTTON_MAIN_PAGE).click()
        WebDriverWait(driver, 3).until(EC.presence_of_element_located(Locators.LOGIN_BUTTON))
        driver.find_element(*Locators.FIELD_EMAIL).send_keys(Credentials.email)
        driver.find_element(*Locators.FIELD_PASSWORD).send_keys(Credentials.password)
        driver.find_element(*Locators.LOGIN_BUTTON).click()
        WebDriverWait(driver, 3).until(EC.presence_of_element_located(Locators.BUTTON_PLACE_AN_ORDER))
        assert driver.current_url == f'{main_site}/'

    def test_login_personal_account_button(self, driver):
        driver.get(main_site)
        driver.find_element(*Locators.PERSONAL_ACCOUNT_BUTTON).click()
        WebDriverWait(driver, 3).until(EC.presence_of_element_located(Locators.LOGIN_BUTTON))
        driver.find_element(*Locators.FIELD_EMAIL).send_keys(Credentials.email)
        driver.find_element(*Locators.FIELD_PASSWORD).send_keys(Credentials.password)
        driver.find_element(*Locators.LOGIN_BUTTON).click()
        WebDriverWait(driver, 3).until(EC.presence_of_element_located(Locators.BUTTON_PLACE_AN_ORDER))
        assert driver.current_url == f'{main_site}/'

    def test_login_form_registration_button(self, driver):
        driver.get(register)
        element = driver.find_element(*Locators.REG_FORM_AND_FGT_PSW_LOG_BTN)
        driver.execute_script('arguments[0].scrollIntoView();', element)
        element.click()
        WebDriverWait(driver, 3).until(EC.presence_of_element_located(Locators.LOGIN_BUTTON))
        driver.find_element(*Locators.FIELD_EMAIL).send_keys(Credentials.email)
        driver.find_element(*Locators.FIELD_PASSWORD).send_keys(Credentials.password)
        driver.find_element(*Locators.LOGIN_BUTTON).click()
        WebDriverWait(driver, 3).until(EC.presence_of_element_located(Locators.BUTTON_PLACE_AN_ORDER))
        assert driver.current_url == f'{main_site}/'

    def test_login_forgot_password_button(self, driver):
        driver.get(forgot_password)
        element = driver.find_element(*Locators.REG_FORM_AND_FGT_PSW_LOG_BTN)
        driver.execute_script('arguments[0].scrollIntoView();', element)
        element.click()
        WebDriverWait(driver, 3).until(EC.presence_of_element_located(Locators.LOGIN_BUTTON))
        driver.find_element(*Locators.FIELD_EMAIL).send_keys(Credentials.email)
        driver.find_element(*Locators.FIELD_PASSWORD).send_keys(Credentials.password)
        driver.find_element(*Locators.LOGIN_BUTTON).click()
        WebDriverWait(driver, 3).until(EC.presence_of_element_located(Locators.BUTTON_PLACE_AN_ORDER))
        assert driver.current_url == f'{main_site}/'
