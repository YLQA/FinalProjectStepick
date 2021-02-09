# import pytest
# from selenium import webdriver
#
#
# @pytest.fixture(scope="function")
# def browser():
#     print("\nstart browser for test..")
#     browser = webdriver.Chrome(executable_path='C:\\chromedriver\\chromedriver.exe')
#     browser.implicitly_wait(2)
#     yield browser
#     print("\nquit browser..")
#     browser.quit()

import pytest
from selenium import webdriver

def pytest_addoption(parser):
        parser.addoption('--browser_name', action='store', default=None,
                         help="Choose browser: chrome or firefox")


@pytest.mark.parametrize('language',["en-gb"])
@pytest.fixture(scope="function")
def browser(request, language):
    browser_name = request.config.getoption("browser_name")
    browser = None
    if browser_name == "chrome":
        print("\nstart chrome browser for test..")
        browser = webdriver.Chrome(executable_path='C:\\chromedriver\\chromedriver.exe')
    elif browser_name == "firefox":
        print("\nstart firefox browser for test..")
        browser = webdriver.Firefox(executable_path='C:\\geckodriver\\geckodriver.exe')
    else:
        raise pytest.UsageError("--browser_name should be chrome or firefox")
    yield browser
    print("\nquit browser..")
    browser.quit()
