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