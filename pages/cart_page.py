from .base_page import BasePage
from .locators import CartPageLocators

class CartPage(BasePage):
    def should_not_be_items(self):
        assert self.is_not_element_present(*CartPageLocators.CART_ITEMS), "Cart elements are presented but should not be"

    def should_be_empty_cart_message(self):
        self.is_element_present(*CartPageLocators.MESSAGE), "Empty cart message is not presented"