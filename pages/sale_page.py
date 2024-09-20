from pages.base_page import BasePage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class SalePage(BasePage):
    page_url = "sale.html"

    def check_that_women_deals_button_is_clikcable(self):
        shop_women_deal_locator = ("xpath", "//span[@class='more button']")
        wait = WebDriverWait(self.driver, 5)
        wait.until(EC.element_to_be_clickable(shop_women_deal_locator))

    def check_url_logo(self, url_logo):
        logo_url_locator = (By.CSS_SELECTOR, 'a.logo img')
        logo = self.find(logo_url_locator)
        url_logo_page = logo.get_attribute('src')
        assert url_logo == url_logo_page

    def check_wish_list_on_page(self):
        wish_list_locator = ("xpath", "//strong[text()='My Wish List']")
        wait = WebDriverWait(self.driver, 5)
        wait.until(EC.text_to_be_present_in_element(wish_list_locator, 'My Wish List'))
