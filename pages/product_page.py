from .base_page import BasePage
from .locators import ProductPageLocators

class ProductPage(BasePage):

    def should_not_be_successful_message(self):
        assert self.is_not_element_present(*ProductPageLocators.MESSAGE), "Message is presented, but should not be"

    def add_product_to_cart(self):
        button = self.browser.find_element(*ProductPageLocators.ADD_TO_CART_BUTTON)
        button.click()
        self.solve_quiz_and_get_code()        

    def should_be_successful_message_with_product_name(self):
        product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text
        product_name_in_message = self.browser.find_element(*ProductPageLocators.MESSAGE).text
        assert product_name == product_name_in_message, "Product name {} isn't equal to product added to cart {}".format(product_name, product_name_in_message)

    def should_be_cart_price_equal_to_product_price(self):
        cart_price = self.browser.find_element(*ProductPageLocators.CART_PRICE).text
        product_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text
        assert cart_price == product_price, "Cart price {} isn't equal to product price {}".format(cart_price, product_price)

    def should_message_disappear(self):
        assert self.is_disappeared(*ProductPageLocators.MESSAGE), "Message did not disappear, but should did"