import random

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from locators import BurgersLocators
from data_for_registration import DataRegistration


class TestRegistration():

    def test_registration_text_on_button_place_an_order(self, driver):

        driver.find_element(*BurgersLocators.BUTTON_LOGIN_ACCOUNT).click()

        WebDriverWait(driver, 5).until(
            expected_conditions.visibility_of_element_located(BurgersLocators.BUTTON_LOGIN_IN_LOGIN_WINDOW))
        driver.find_element(*BurgersLocators.LINK_REGISTRATION).click()

        WebDriverWait(driver, 5).until(
            expected_conditions.visibility_of_element_located(BurgersLocators.BUTTON_REGISTRATION_IN_REGISTER_WINDOW))
        email = DataRegistration.EMAIL
        password = DataRegistration.PASSWORD
        driver.find_element(*BurgersLocators.INPUT_NAME_REGISTER_WINDOW).send_keys('Лилу')
        driver.find_element(*BurgersLocators.INPUT_EMAIL_REGISTER_WINDOW).send_keys(email)
        driver.find_element(*BurgersLocators.INPUT_PASSWORD_REGISTER_WINDOW).send_keys(password)
        driver.find_element(*BurgersLocators.BUTTON_REGISTRATION_IN_REGISTER_WINDOW).click()

        WebDriverWait(driver, 5).until(
            expected_conditions.visibility_of_element_located(BurgersLocators.BUTTON_LOGIN_IN_LOGIN_WINDOW))
        driver.find_element(*BurgersLocators.INPUT_EMAIL_LOGIN_WINDOW).send_keys(email)
        driver.find_element(*BurgersLocators.INPUT_PASSWORD_LOGIN_WINDOW).send_keys(password)
        driver.find_element(*BurgersLocators.BUTTON_LOGIN_IN_LOGIN_WINDOW).click()

        WebDriverWait(driver, 5).until(
            expected_conditions.visibility_of_element_located(BurgersLocators.H1_IN_MAIN_WINDOW))

        assert driver.find_element(*BurgersLocators.BUTTON_PLACE_AN_ORDER).is_displayed()

    def test_registration_text_password_len_less_then_6_password_text_error(self, driver):

        driver.find_element(*BurgersLocators.BUTTON_LOGIN_ACCOUNT).click()

        WebDriverWait(driver, 5).until(
            expected_conditions.visibility_of_element_located(BurgersLocators.BUTTON_LOGIN_IN_LOGIN_WINDOW))
        driver.find_element(*BurgersLocators.LINK_REGISTRATION).click()

        WebDriverWait(driver, 5).until(
            expected_conditions.visibility_of_element_located(BurgersLocators.BUTTON_REGISTRATION_IN_REGISTER_WINDOW))
        email = DataRegistration.EMAIL
        password = random.randint(0, 99999)
        driver.find_element(*BurgersLocators.INPUT_NAME_REGISTER_WINDOW).send_keys('Лилу')
        driver.find_element(*BurgersLocators.INPUT_EMAIL_REGISTER_WINDOW).send_keys(email)
        driver.find_element(*BurgersLocators.INPUT_PASSWORD_REGISTER_WINDOW).send_keys(password)
        driver.find_element(*BurgersLocators.BUTTON_REGISTRATION_IN_REGISTER_WINDOW).click()

        assert driver.find_element(*BurgersLocators.PASSWORD_TEXT_ERROR).is_displayed()
