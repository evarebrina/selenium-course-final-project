import pytest
from pages.product_page import ProductPage


def test_guest_can_add_product_to_cart(browser):
    link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019'
    page = ProductPage(browser, link)
    page.open()
    page.should_not_be_successful_message()
    page.add_product_to_cart()
    page.should_be_successful_message_with_product_name()
    page.should_be_cart_price_equal_to_product_price()

def test_guest_cant_see_success_message(browser):
    link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019'
    page = ProductPage(browser, link)
    page.open()
    page.should_not_be_successful_message()
