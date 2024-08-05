from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from locators import BurgersLocators
from helpers import Helpers


class TestGoToPersonalAccount:

    def test_link_personal_account_account_window(self, driver):
        driver.find_element(*BurgersLocators.BUTTON_LOGIN_ACCOUNT).click()
        Helpers.login_in_account(driver)
        WebDriverWait(driver, 5).until(
            expected_conditions.visibility_of_element_located(BurgersLocators.H1_IN_MAIN_WINDOW))
        driver.find_element(*BurgersLocators.BUTTON_PERSONAL_ACCOUNT).click()
        assert 'account' in driver.current_url
