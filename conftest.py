import pytest
from selenium import webdriver


@pytest.fixture
def browser():
    browser= webdriver.Chrome()
    browser.maximize_window()
    browser.implicitly_wait(5)
    yield browser