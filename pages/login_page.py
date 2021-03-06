from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert "/login/" in self.browser.current_url, "Substring '/login/' is not present in the current url"

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form not found"

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTRATION_FORM), "Register form not found"

    def register_new_user(self, email, password):
        input_email = self.browser.find_element(*LoginPageLocators.EMAIL_ADDRESS)
        input_email.send_keys(email)
        input_password = self.browser.find_element(*LoginPageLocators.PASSWORD)
        input_password.send_keys(password)
        input_confirm_password = self.browser.find_element(*LoginPageLocators.CONFIRM_PASSWORD)
        input_confirm_password.send_keys(password)
        button_register = self.browser.find_element(*LoginPageLocators.BUTTON_REGISTER)
        button_register.click()


