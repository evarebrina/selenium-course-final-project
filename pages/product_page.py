from .base_page import BasePage
from .locators import ProductPageLocators

class ProductPage(BasePage):

    def add_product_to_cart(self):
        button = self.browser.find_element(*ProductPageLocators.ADD_TO_CART_BUTTON)
        button.click()
        self.solve_quiz_and_get_code()
        product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text
        product_name_in_message = self.browser.find_element(*ProductPageLocators.MESSAGE).text
        assert product_name == product_name_in_message, "Product name {} isn't equal to product added to cart {}".format(product_name, product_name_in_message)
        cart_price = self.browser.find_element(*ProductPageLocators.CART_PRICE).text
        product_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text
        assert cart_price == product_price, "Cart price {} isn't equal to product price {}".format(cart_price, product_price)