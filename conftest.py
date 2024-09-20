import pytest
from selenium import webdriver
from pages.create_account import CreateAccount
from pages.eco_friendly_page import EcoFriendly

@pytest.fixture()
def driver():
    driver = webdriver.Chrome()
    return driver


@pytest.fixture()
def create_account(driver):
    return CreateAccount(driver)

@pytest.fixture()
def eco_friendly(driver):
    return EcoFriendly(driver)