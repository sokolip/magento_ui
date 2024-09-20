eco_friendly_title_text = 'Eco Friendly'


def test_verify_title(eco_friendly):
    eco_friendly.open_page()
    eco_friendly.verify_title_on_page(title_text=eco_friendly_title_text)


def test_count_item_on_eco_friendly_page(eco_friendly):
    eco_friendly.open_page()
    eco_friendly.verify_count_on_page()


def test_search_field_on_page(eco_friendly):
    eco_friendly.open_page()
    eco_friendly.verify_search_field_on_page()
