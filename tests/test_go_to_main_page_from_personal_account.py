import pytest
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from locators import BurgersLocators
from data_for_burgers import DataForBurgers
from helpers import Helpers


class TestGoToMainPage:

    @pytest.mark.parametrize('to_main_page_button', [BurgersLocators.BUTTON_CONSTRUCTOR, BurgersLocators.BUTTON_LOGO])
    def test_click_button_to_main_page(self, driver, to_main_page_button):
        driver.find_element(*BurgersLocators.BUTTON_LOGIN_ACCOUNT).click()
        Helpers.login_in_account(driver)
        WebDriverWait(driver, 5).until(
            expected_conditions.visibility_of_element_located(BurgersLocators.H1_IN_MAIN_WINDOW))
        driver.find_element(*BurgersLocators.BUTTON_PERSONAL_ACCOUNT).click()
        WebDriverWait(driver, 5).until(
            expected_conditions.visibility_of_element_located(BurgersLocators.BUTTON_LOGO))
        driver.find_element(*to_main_page_button).click()
        assert DataForBurgers.URL_MAIN_PAGE == driver.current_url
