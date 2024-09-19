from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains



first_name_locator = ("xpath", "//input[@id='firstname']")
last_name_locator = ("xpath", "//input[@id='lastname']")
email_field_locator = ("xpath", "//input[@id='email_address']")
password_field_locator = ("xpath", "//input[@id='password']")
password_confirm_field_locator = ("xpath", "//input[@id='password-confirmation']")
create_account_button = ("xpath", "//button[@title='Create an Account']")
title_locator = ("xpath", "//span[text()='My Account']")


class CreateAccount(BasePage):
    page_url = "customer/account/create/"

    def create_new_account(self, first_name, last_name, email, password):
        first_name_field = self.find(first_name_locator)
        last_name_field = self.find(last_name_locator)
        email_field = self.find(email_field_locator)
        password_field = self.find(password_field_locator)
        confirm_password_field = self.find(password_confirm_field_locator)
        confirm_button = self.find(create_account_button)
        first_name_field.send_keys(first_name)
        last_name_field.send_keys(last_name)
        email_field.send_keys(email)
        password_field.send_keys(password)
        confirm_password_field.send_keys(password)
        scroll = ActionChains(self.driver)
        scroll.scroll_to_element(confirm_button)
        # WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(confirm_button))
        confirm_button.click()
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.text_to_be_present_in_element(title_locator, 'My Account'))

    def check_that_confirm_text_is_presented(self, text):
        confirm_text_locator = ("xpath", "//div[@data-bind='html: $parent.prepareMessageForHtml(message.text)']")
        confirm_text = self.find(confirm_text_locator).text
        # print(confirm_text)
        assert confirm_text == text

    def check_email_in_my_account(self, email):
        email_locator = (By.CSS_SELECTOR, '.box-content p')
        account_email_text = self.find(email_locator).text
        account_email = account_email_text.split("\n")[1]
        # print(f'почта {account_email}')
        assert account_email == email

