import random

from locators import BurgersLocators
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions


class DataForBurgers:

    EMAIL_LOGIN = 'svshakhova9213@yandex.ru'
    PASSWORD_LOGIN = 'burger'
    URL_MAIN_PAGE = 'https://stellarburgers.nomoreparties.site/'

    @staticmethod
    def login_in_account(driver):
        WebDriverWait(driver, 5).until(
            expected_conditions.visibility_of_element_located(BurgersLocators.BUTTON_LOGIN_IN_LOGIN_WINDOW))
        driver.find_element(*BurgersLocators.INPUT_EMAIL_LOGIN_WINDOW).send_keys(DataRegistration.EMAIL_LOGIN)
        driver.find_element(*BurgersLocators.INPUT_PASSWORD_LOGIN_WINDOW).send_keys(DataRegistration.PASSWORD_LOGIN)
        driver.find_element(*BurgersLocators.BUTTON_LOGIN_IN_LOGIN_WINDOW).click()
