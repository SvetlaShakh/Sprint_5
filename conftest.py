import pytest
import random

from selenium import webdriver
from data_for_burgers import DataForBurgers


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.get(DataForBurgers.URL_MAIN_PAGE)

    yield driver

    driver.quit()


@pytest.fixture
def add_data_for_registration():
    name = 'Лилу'
    email = f'Leeloo{random.randint(0000, 9999)}@gmail.com'
    password = f'Lee{random.randint(000, 999999)}'
    return name, email, password
