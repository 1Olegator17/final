from selenium.webdriver.common.by import By
from .pages.main_page import MainPage
from .pages.login_page import LoginPage  

def test_guest_can_go_to_login_page(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(browser, link)
    page.open() 
    page.go_to_login_page()  # Переход на страницу логина

def test_guest_should_see_login_link(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(browser, link)
    page.open()
    page.should_be_login_link()  # Проверяем наличие ссылки на логин

def test_login_page(browser):
    link = "http://selenium1py.pythonanywhere.com/accounts/login/"  # URL страницы логина
    page = LoginPage(browser, link)  # Создаем экземпляр LoginPage с правильным URL
    page.open()  
    page.should_be_login_url()  # Проверяем, что URL содержит 'login'
    page.should_be_login_form()  # Проверяем наличие формы логина
    page.should_be_register_form()  # Проверяем наличие формы регистрации
