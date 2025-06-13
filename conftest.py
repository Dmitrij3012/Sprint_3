import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


from curl import login_page
from locators import Locators
from data import Credentials


@pytest.fixture(scope='function')
def driver():
    options = Options()
    options.add_argument('--window-size=1280,720')
    browser = webdriver.Chrome(options=options)
    browser.get(login_page)
    yield browser
    browser.quit()


@pytest.fixture(scope='function')
def login(driver):

    driver.find_element(*Locators.FIELD_EMAIL).send_keys(Credentials.email)
    driver.find_element(*Locators.FIELD_PASSWORD).send_keys(Credentials.password)
    driver.find_element(*Locators.LOGIN_BUTTON).click()

    return driver
