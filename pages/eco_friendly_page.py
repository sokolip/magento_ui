from pages.base_page import BasePage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class EcoFriendly(BasePage):
    page_url = 'collections/eco-friendly.html'

    def verify_title_on_page(self, title_text):
        title_locator = ("xpath", "//span[@data-ui-id='page-title-wrapper']")
        title = self.find(title_locator).text
        assert title_text == title

    def verify_count_on_page(self):
        limiter_locator = ("xpath", "(//option[@selected='selected'])[3]")
        limiter = self.find(limiter_locator).text
        limiter = int(limiter)
        item_count_locator = ("xpath", "//li[@class='item product product-item']")
        item_count = len(self.find_all(item_count_locator))
        assert item_count == limiter

    def verify_search_field_on_page(self):
        search_field_locator = ("xpath", "//input[@id='search']")
        search_form_locator = ("xpath", "//form[@id='search_mini_form']")
        search_field = self.find(search_field_locator)
        search_field.click()
        wait = WebDriverWait(self.driver, 5)
        wait.until(EC.text_to_be_present_in_element_attribute(search_form_locator, 'class', 'form minisearch active'))
