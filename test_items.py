import time
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException


def test_button_add_to_basket_is_displayed(browser):
    browser.get('http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/')
    try:
        browser.find_element(By.CSS_SELECTOR, '.btn-add-to-basket')
        result = True
    except NoSuchElementException:
        result = False

    assert result == True, 'It is no Add to basket button on page'
    # Для моего коллеги ревьювера оставляю закоменченным ожидание)
    #time.sleep(10)
