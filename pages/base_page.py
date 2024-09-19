from selenium import webdriver


class BasePage:
    base_url = "https://magento.softwaretestingboard.com/"
    page_url = None

    def __init__(self, driver):
        self.driver = driver

    def open_page(self):
        if self.page_url:
            self.driver.get(f'{self.base_url}/{self.page_url}')
        else:
            raise NotImplementedError("Page can not be opened fo this page url")

    def find(self, locator: tuple):
        return self.driver.find_element(*locator)

    def find_all(self, locator: tuple):
        return self.driver.find_elements(*locator)




