from .base_page import BasePage
from .locators import ProductPageLocators

class ProductPage(BasePage):

    def add_product_to_cart(self):
        button = self.browser.find_element(*ProductPageLocators.ADD_TO_CART_BUTTON)
        button.click()
        self.solve_quiz_and_get_code()
        assert self.is_element_present(*ProductPageLocators.MESSAGE), "Message is not presented"
        cart_price = self.browser.find_element(*ProductPageLocators.CART_PRICE).text
        product_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text
        assert cart_price == product_price, "Cart price {} isn't equal to product price {}".format(cart_price, product_price)