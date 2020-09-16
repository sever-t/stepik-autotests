import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def pytest_addoption(parser):
    parser.addoption('--browser_name', action='store', default='chrome', help="Choose browser: chrome or firefox")
    parser.addoption('--language', action='store', default='ru', help="Choose language: ru, es, fr,...")

@pytest.fixture(scope="function")
def browser(request):
    browser_name = request.config.getoption("browser_name")
    selected_language = request.config.getoption("language")
    browser = None
    if browser_name == "chrome":
        print("\nstart browser chrome for test...")
        options = Options()
        options.add_experimental_option('prefs', {'intl.accept_languages': selected_language})
        browser = webdriver.Chrome(options=options)
    elif browser_name == "firefox":
        print("\nstart browser firefox for test...")
        fp = webdriver.FirefoxProfile()
        fp.set_preference("intl.accept_languages", selected_language)
        browser = webdriver.Firefox(firefox_profile=fp)
    else:
        raise pytest.UsageError("browser or language parametrs error")
    yield browser
    print("\nquit browser...")
    browser.quit()
