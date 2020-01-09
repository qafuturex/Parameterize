import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_button_add_to_basket_is_displayed(browser):

    #time.sleep(30)
    try:
        browser.find_element(By.CSS_SELECTOR, '.btn-add-to-basket')
        result = True
    except:
        result = False

    assert result == True, 'It is no Add to basket button on page'

    time.sleep(5)

