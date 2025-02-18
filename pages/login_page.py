from .base_page import BasePage
from .locators import LoginPageLocators  # Импортируем локаторы
from selenium.webdriver.common.by import By
import time

class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        # Проверка на корректный URL адрес
        current_url = self.browser.current_url
        assert "login" in current_url, f"URL не содержит 'login': {current_url}"

    def should_be_login_form(self):
        # Проверка, что есть форма логина
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Форма логина не найдена"

    def should_be_register_form(self):
        # Проверка, что есть форма регистрации на странице
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "Форма регистрации не найдена"



    def register_new_user(self, email, password):
        self.browser.find_element(*LoginPageLocators.EMAIL_INPUT).send_keys(email)
        self.browser.find_element(*LoginPageLocators.PASSWORD_INPUT).send_keys(password)
        self.browser.find_element(*LoginPageLocators.CONFIRM_PASSWORD_INPUT).send_keys(password)
        self.browser.find_element(*LoginPageLocators.REGISTER_BUTTON).click()
        time.sleep(1)  
