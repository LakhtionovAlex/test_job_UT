from pages.base_page import BasePage
from components.components import WebElement


class DemoUpTr(BasePage):
    def __init__(self, driver):
        self.base_url = 'https://demo.uptr.dev/auth/login'
        super().__init__(driver, self.base_url)

        self.language = WebElement(driver, ".css-1hwfws3 > div")
        self.sign_in = WebElement(driver, "#login-page-nav-to-login-page-active")
        self.register = WebElement(driver, "#login-page-nav-to-registration-page")
