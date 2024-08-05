from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from locators import BurgersLocators
from helpers import Helpers


class TestLogin:

    def test_login_on_button_login_account_place_an_order(self, driver):
        driver.find_element(*BurgersLocators.BUTTON_LOGIN_ACCOUNT).click()
        Helpers.login_in_account(driver)
        WebDriverWait(driver, 5).until(
            expected_conditions.visibility_of_element_located(BurgersLocators.H1_IN_MAIN_WINDOW))
        assert driver.find_element(*BurgersLocators.BUTTON_PLACE_AN_ORDER).is_displayed()

    def test_login_on_button_personal_account_place_an_order(self, driver):
        driver.find_element(*BurgersLocators.BUTTON_PERSONAL_ACCOUNT).click()
        Helpers.login_in_account(driver)
        WebDriverWait(driver, 5).until(
            expected_conditions.visibility_of_element_located(BurgersLocators.H1_IN_MAIN_WINDOW))
        assert driver.find_element(*BurgersLocators.BUTTON_PLACE_AN_ORDER).is_displayed()

    def test_login_register_window_place_an_order(self, driver):
        driver.find_element(*BurgersLocators.BUTTON_LOGIN_ACCOUNT).click()
        WebDriverWait(driver, 5).until(
            expected_conditions.visibility_of_element_located(BurgersLocators.BUTTON_LOGIN_IN_LOGIN_WINDOW))
        driver.find_element(*BurgersLocators.LINK_REGISTRATION).click()
        WebDriverWait(driver, 5).until(
            expected_conditions.visibility_of_element_located(BurgersLocators.BUTTON_REGISTRATION_IN_REGISTER_WINDOW))
        driver.find_element(*BurgersLocators.LINK_LOGIN_REGISTER_WINDOW).click()
        Helpers.login_in_account(driver)
        WebDriverWait(driver, 5).until(
            expected_conditions.visibility_of_element_located(BurgersLocators.H1_IN_MAIN_WINDOW))
        assert driver.find_element(*BurgersLocators.BUTTON_PLACE_AN_ORDER).is_displayed()

    def test_login_forgot_password_window_place_an_order(self, driver):
        driver.find_element(*BurgersLocators.BUTTON_LOGIN_ACCOUNT).click()
        WebDriverWait(driver, 5).until(
            expected_conditions.visibility_of_element_located(BurgersLocators.BUTTON_LOGIN_IN_LOGIN_WINDOW))
        driver.find_element(*BurgersLocators.LINK_FOGOT_PASSWORD).click()
        WebDriverWait(driver, 5).until(
            expected_conditions.visibility_of_element_located(BurgersLocators.BUTTON_RESTORE_FORGOT_PASSWORD_WINDOW))
        driver.find_element(*BurgersLocators.LINK_LOGIN_FORGOT_PASSWORD_WINDOW).click()
        Helpers.login_in_account(driver)
        WebDriverWait(driver, 5).until(
            expected_conditions.visibility_of_element_located(BurgersLocators.H1_IN_MAIN_WINDOW))
        assert driver.find_element(*BurgersLocators.BUTTON_PLACE_AN_ORDER).is_displayed()
