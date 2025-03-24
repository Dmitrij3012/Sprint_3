from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from conftest import *
from locators import Locators


class TestTransitionsToSections:

    def test_transition_to_buns(self, login):
        driver = login
        WebDriverWait(driver, 3).until(EC.presence_of_element_located(Locators.BUNS))
        assert 'tab_tab_type_current__2BEPc' in driver.find_element(*Locators.BUNS_PARENT).get_attribute('class')

    def test_transition_to_sauces(self, login):
        driver = login
        WebDriverWait(driver, 3).until(EC.presence_of_element_located(Locators.SAUCES))
        driver.find_element(*Locators.SAUCES).click()
        assert 'tab_tab_type_current__2BEPc' in driver.find_element(*Locators.SAUCES_PARENT).get_attribute('class')

    def test_transition_to_fillings(self, login):
        driver = login
        WebDriverWait(driver, 3).until(EC.presence_of_element_located(Locators.FILLINGS))
        driver.find_element(*Locators.FILLINGS).click()
        assert 'tab_tab_type_current__2BEPc' in driver.find_element(*Locators.FILLINGS_PARENT).get_attribute('class')
