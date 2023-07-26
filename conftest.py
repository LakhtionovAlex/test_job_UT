import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def pytest_addoption(parser):
    parser.addoption(
        '--language',
        action='store',
        default='en',
        help='Choose language'
        )


@pytest.fixture(scope="module")
def browser(request):
    user_language = request.config.getoption("language")
    options = Options()
    options.add_experimental_option('prefs', {'intl.accept_languages': user_language})
    driver = webdriver.Chrome(options=options)
    driver.set_window_size(width=1000, height=1000)
    yield driver
    driver.quit()







# import pytest
# from selenium import webdriver
# from selenium.webdriver.chrome.options import Options
#
#
# def pytest_addoption(parser):
#     parser.addoption(
#         '--browser_name',
#         action='store',
#         default="chrome",
#         help="Choose browser: chrome or firefox"
#         )
#     parser.addoption(
#         '--language',
#         action='store',
#         default='ru',
#         help='Choose language'
#         )
#
#
# @pytest.fixture(scope="function")
# def browser(request):
#     language = request.config.getoption("language")
#     options = Options()
#     options.add_experimental_option('prefs', {'intl.accept_languages': language})
#     print("\nstarting browser for test..")
#     browser = webdriver.Chrome(options=options)
#     yield browser
#     print("\nquit browser..")
#     browser.quit()
#


# @pytest.fixture(scope="function")
# def browser(request):
#     choosen_language = request.config.getoption("language")
#     opts = Options()
#     opts.add_experimental_option('prefs', {'intl.accept_languages': choosen_language})
#     print('\nstart Chrome browser...')
#     browser = webdriver.Chrome(options=opts)
#     yield browser
#     browser.quit()
