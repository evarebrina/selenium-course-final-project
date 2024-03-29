from .base_page import BasePage
from .locators import LoginPageLocators
import time


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert 'login' in self.browser.current_url, "Login url doesn't contain 'login' substring"

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_USERNAME), 'Login username input field is not presented'
        assert self.is_element_present(*LoginPageLocators.LOGIN_PASSWORD), 'Login password input field is not presented'
        assert self.is_element_present(*LoginPageLocators.LOGIN_BUTTON), 'Login button is not presented'

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTRATION_EMAIL), 'Registration email input field is not presented'
        assert self.is_element_present(*LoginPageLocators.REGISTRATION_PASSWORD), 'Registration password input field is not presented'
        assert self.is_element_present(*LoginPageLocators.REGISTRATION_CONFIRM_PASSWORD), 'Registration confirm password input field is not presented'
        assert self.is_element_present(*LoginPageLocators.REGISTRATION_BUTTON), 'Registration button is not presented'

    def register_new_user(self, email, password):
        self.browser.find_element(*LoginPageLocators.REGISTRATION_EMAIL).send_keys(email)
        self.browser.find_element(*LoginPageLocators.REGISTRATION_PASSWORD).send_keys(password)
        self.browser.find_element(*LoginPageLocators.REGISTRATION_CONFIRM_PASSWORD).send_keys(password)
        self.browser.find_element(*LoginPageLocators.REGISTRATION_BUTTON).click()