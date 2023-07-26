from components.components import WebElement


class BasePage:
    def __init__(self, driver, base_url):
        self.driver = driver
        self.base_url = base_url

        self.metaView = WebElement(driver, 'head > meta')

    def visit(self):
        return self.driver.get(self.base_url)
