from .base_page import BasePage
from .locators import LoginPageLocators  # Импортируем локаторы
from selenium.webdriver.common.by import By

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
        assert self.is_element_present(By.CSS_SELECTOR, LoginPageLocators.LOGIN_FORM), "Форма логина не найдена"

    def should_be_register_form(self):
        # Проверка, что есть форма регистрации на странице
        assert self.is_element_present(By.CSS_SELECTOR, LoginPageLocators.REGISTER_FORM), "Форма регистрации не найдена"

    def is_element_present(self, how, what):
        """Проверяет, присутствует ли элемент на странице"""
        try:
            self.browser.find_element(how, what)
        except:
            return False
        return True
