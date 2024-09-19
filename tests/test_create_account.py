import pytest
from pages.create_account import CreateAccount
from faker import Faker


fake = Faker()
first_name = fake.first_name()
last_name = fake.last_name()
email = fake.email()
password = fake.password(9, True, True, True, True)
confirm_text = 'Thank you for registering with Main Website Store.'
incorrect_email = '12345qwermail.com'

existing_email = fake.email()
# 'kykyreky@ya.ru'


def test_create_account_with_correct_data(create_account):
    create_account.open_page()
    create_account.create_account(
        first_name=first_name, last_name=last_name, email=email, password=password
    )
    create_account.check_that_confirm_text_is_presented(text=confirm_text)
    create_account.check_email_in_my_account(email=email)


def test_create_account_with_incorrect_email(create_account):
    create_account.open_page()
    create_account.create_new_account(
        first_name=first_name, last_name=last_name, email=incorrect_email, password=password
    )
    create_account.check_email_validation()


def test_create_account_with_existing_user_email(create_account):
    create_account.open_page()
    create_account.create_new_account(
        first_name=first_name, last_name=last_name, email=existing_email, password=password
    )
    create_account.sign_out()
    create_account.create_new_account(
        first_name=first_name, last_name=last_name, email=existing_email, password=password
    )
    create_account.check_validation_existing_email()


