from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from .locators import BasePageLocators
from .locators import LoginPageLocators


class BasePage():
    def __init__(self, browser, url, timeout=10): 
    # Инициализация базовой страницы с браузером, URL и таймаутом 
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)

    def open(self): 
        self.browser.get(self.url)


    def is_element_present(self, how, what):
        # Проверка наличия элемента на странице
        try:
            self.browser.find_element(how, what)
        except NoSuchElementException:
            print(f"Element with selector '{what}' was not found.")
            return False
        return True

    def is_not_element_present(self, how, what, timeout=4):
        try:
            WebDriverWait(self.browser, timeout).until(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return True

        return False

    def is_disappeared(self, how, what, timeout=4):
        # Проверка, что элемент исчез с страницы в течение указанного времени
        try:
            WebDriverWait(self.browser, timeout).until(EC.staleness_of(self.browser.find_element(how, what)))
        except TimeoutException:
            return False
        return True




    def go_to_login_page(self):
        link = self.browser.find_element(*BasePageLocators.LOGIN_LINK)
        link.click()
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Failed to navigate to login page"

    def should_be_login_link(self):
        assert self.is_element_present(*BasePageLocators.LOGIN_LINK), "Login link is not presented"





    def go_to_basket(self):
        basket_link = self.browser.find_element(*BasePageLocators.BASKET_LINK)  
        basket_link.click()


    def should_be_authorized_user(self):
        # Проверка, что пользователь авторизован
        assert self.is_element_present(*BasePageLocators.USER_ICON), "User  icon is not presented," \
                                                                     " probably unauthorised user"