import time

import pytest
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from locators import BurgersLocators


class TestTabOfConstructor():

    name_tabs_and_lists = [[BurgersLocators.TAB_SAUCES, BurgersLocators.NAME_OF_LIST_SAUCES,
                            BurgersLocators.TAB_SAUCES_CURRENT],
                           [BurgersLocators.TAB_FILLINGS, BurgersLocators.NAME_OF_LIST_FILLINGS,
                            BurgersLocators.TAB_FILLINGS_CURRENT]]

    @pytest.mark.parametrize('tab_name, name_of_list, tab_current', name_tabs_and_lists)
    def test_click_tab_constructor_current_list(self, driver, tab_name, name_of_list, tab_current):

        driver.find_element(*tab_name).click()
        WebDriverWait(driver, 5).until(expected_conditions.presence_of_element_located(tab_current))

        assert driver.find_element(*name_of_list).is_displayed() and driver.find_element(*tab_current).is_displayed()

    def test_click_tab_bun_constructor_current_list(self, driver):

        driver.find_element(*BurgersLocators.TAB_SAUCES).click()
        WebDriverWait(driver, 5).until(expected_conditions.presence_of_element_located(BurgersLocators.TAB_SAUCES_CURRENT))
        driver.find_element(*BurgersLocators.TAB_BUNS).click()
        WebDriverWait(driver, 5).until(expected_conditions.presence_of_element_located(BurgersLocators.TAB_BUNS_CURRENT))

        assert (driver.find_element(*BurgersLocators.NAME_OF_LIST_BUNS).is_displayed() and
                driver.find_element(*BurgersLocators.TAB_BUNS_CURRENT).is_displayed())
