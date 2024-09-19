import pytest
from selenium import webdriver
from pages.create_account import CreateAccount


@pytest.fixture()
def driver():
    driver = webdriver.Chrome()
    return driver


@pytest.fixture()
def create_account(driver):
    return CreateAccount(driver)