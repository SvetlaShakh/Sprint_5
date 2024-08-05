from locators import BurgersLocators
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from data_for_burgers import DataForBurgers


class Helpers:

    @staticmethod
    def login_in_account(driver):
        WebDriverWait(driver, 5).until(
            expected_conditions.visibility_of_element_located(BurgersLocators.BUTTON_LOGIN_IN_LOGIN_WINDOW))
        driver.find_element(*BurgersLocators.INPUT_EMAIL_LOGIN_WINDOW).send_keys(DataForBurgers.EMAIL_LOGIN)
        driver.find_element(*BurgersLocators.INPUT_PASSWORD_LOGIN_WINDOW).send_keys(DataForBurgers.PASSWORD_LOGIN)
        driver.find_element(*BurgersLocators.BUTTON_LOGIN_IN_LOGIN_WINDOW).click()
