from selenium.webdriver.common.by import By
from .pages.main_page import MainPage
from .pages.basket_page import BasketPage
from .pages.login_page import LoginPage
import pytest


@pytest.mark.login_guest
class TestLoginFromMainPage(): 
# Тест на возможность перехода на страницу логина         
    def test_guest_can_go_to_login_page(self, browser):
        link = "http://selenium1py.pythonanywhere.com/"
        page = MainPage(browser, link)
        page.open() 
        page.go_to_login_page()  # Переход на страницу логина
        login_page = LoginPage(browser, browser.current_url)
        login_page.should_be_login_page()
    
# Тест на возможность перехода в корзину
    def test_guest_can_go_to_basket(self, browser):
        link = "http://selenium1py.pythonanywhere.com/en-gb/"
        main_page = MainPage(browser, link)
        main_page.open()
        main_page.go_to_basket()
        basket_page = BasketPage(browser, browser.current_url)
        basket_page.should_not_be_products_in_basket()
        basket_page.should_be_empty_basket_message()

                     

    
    
    
    
    
            



