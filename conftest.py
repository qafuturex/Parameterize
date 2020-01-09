import pytest
from selenium import webdriver

def pytest_addoption(parser):
    parser.addoption('--language', action='store', default=None,
                     help="Choose language: es, fr")

@pytest.fixture(scope="function")
def browser(request):
    language_name = request.config.getoption("language")
    language = None
    if language_name == "es":
        link = 'http://selenium1py.pythonanywhere.com/es/catalogue/coders-at-work_207/'
        print("\nstart chrome browser for test, language = es")
        browser = webdriver.Chrome()
        browser.get(link)
    elif language_name == "fr":
        link = 'http://selenium1py.pythonanywhere.com/fr/catalogue/coders-at-work_207/'
        print("\nstart chrome browser for test, language = es")
        browser = webdriver.Chrome()
        browser.get(link)
    else:
        raise pytest.UsageError("--You are not set up any browser")

