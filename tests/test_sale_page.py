url_logo = "https://magento.softwaretestingboard.com/pub/static/version1695896754/frontend/Magento/luma/en_US/images/logo.svg"


def test_women_deal_button_is_clickable(sale_page):
    sale_page.open_page()
    sale_page.check_that_women_deals_button_is_clikcable()


def test_check_url_logo_page(sale_page):
    sale_page.open_page()
    sale_page.check_url_logo(url_logo=url_logo)


def test_wish_list_on_sale_page(sale_page):
    sale_page.open_page()
    sale_page.check_wish_list_on_page()