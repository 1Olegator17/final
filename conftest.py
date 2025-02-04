import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def pytest_addoption(parser):
    parser.addoption(
        "--language", action="store", default="en", help="language for the test"
    )

@pytest.fixture
def user_language(request):
    return request.config.getoption("--language")

@pytest.fixture(scope="function")
def browser(user_language):
    print("\nstart browser for test..")
    options = Options()
    options.add_experimental_option('prefs', {'intl.accept_languages': user_language})
    browser = webdriver.Chrome(options=options)
    yield browser
    print("\nquit browser..")
    browser.quit()
