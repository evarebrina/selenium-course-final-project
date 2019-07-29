from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, '#login_link')


class LoginPageLocators():
    LOGIN_BUTTON = (By.CSS_SELECTOR, 'button[name="login_submit"]')
    REGISTRATION_BUTTON = (By.CSS_SELECTOR, 'button[name="registration_submit"]')
    LOGIN_USERNAME = (By.CSS_SELECTOR, 'input[name="login-username"]')
    LOGIN_PASSWORD = (By.CSS_SELECTOR, 'input[name="login-password"]')
    REGISTRATION_EMAIL = (By.CSS_SELECTOR, 'input[name="registration-email"]')
    REGISTRATION_PASSWORD = (By.CSS_SELECTOR, 'input[name="registration-password1"]')
    REGISTRATION_CONFIRM_PASSWORD = (By.CSS_SELECTOR, 'input[name="registration-password2"]')


class ProductPageLocators():
    ADD_TO_CART_BUTTON = (By.CLASS_NAME, 'btn-add-to-basket')
    MESSAGE = (By.CSS_SELECTOR, '#messages > .alert:nth-child(1) .alertinner strong')
    CART_PRICE = (By.CSS_SELECTOR, '#messages > .alert:nth-child(3) .alertinner strong')
    PRODUCT_PRICE = (By.CSS_SELECTOR, '.product_main > .price_color')