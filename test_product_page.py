import pytest
from .pages.product_page import ProductPage
from .pages.basket_page import BasketPage
from .pages.login_page import LoginPage
import time
from .pages.locators import ProductPageLocators

# Параметризованный тест для добавления товара в корзину с различными промо-ссылками
@pytest.mark.parametrize('link', [
    "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
    "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1",
    "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2",
    pytest.param("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7", marks=pytest.mark.xfail)# Ожидается сбой
])
def test_guest_can_add_product_to_basket(browser, link):
    page = ProductPage(browser, link)
    page.open()  
    page.add_to_basket_promotion() 


    product_name = page.get_product_name()
    product_price = page.get_product_price()


    page.should_be_success_message(product_name)

    # Проверяем, что итоговая сумма в корзине соответствует цене товара
    page.should_be_basket_total(product_price)

    print(f"Тест завершился для ссылки: {link}")

@pytest.mark.parametrize('link', [
    "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
])
# сообщение об успехе не отображается при переходе на страницу товара
def test_should_not_be_success_message(browser, link):
    page = ProductPage(browser, link)
    page.open()  
    page.should_not_be_success_message()



@pytest.mark.parametrize('link', [
    pytest.param("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0", marks=pytest.mark.xfail)
])
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser, link):
    page = ProductPage(browser, link)
    page.open()  
    page.add_to_basket_promotion()  # Добавляем товар в корзину
    # Проверяем, что сообщение об успехе не отображается
    page.should_not_be_success_message()





@pytest.mark.parametrize('link', [
    pytest.param("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0", marks=pytest.mark.xfail)
])
def test_message_disappeared_after_adding_product_to_basket(browser, link):
    # Тест, чтобы проверить, исчезло ли сообщение об успехе после добавления товара
    page = ProductPage(browser, link)
    page.open()  # Открываем страницу товара
    page.add_to_basket_promotion()  # Добавляем товар в корзину
    # Проверяем, что сообщение об успехе исчезло
    assert page.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), "Success message did not disappear after adding product to basket"


def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()


def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()
    
    


def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    product_page = ProductPage(browser, link)
    product_page.open()
    product_page.go_to_basket()
    
    basket_page = BasketPage(browser, browser.current_url)
    basket_page.should_not_be_products_in_basket()
    basket_page.should_be_empty_basket_message()


class TestUserAddToBasketFromProductPage:
    @pytest.fixture(scope="function")
    def setup(self, browser):
        # Открываем страницу регистрации
        link = "http://selenium1py.pythonanywhere.com/en-gb/accounts/login/"
        login_page = LoginPage(browser, link)
        login_page.open()

        # Регистрация нового пользователя
        email = str(time.time()) + "@fakemail.org"
        password = "TestPassword123"
        login_page.register_new_user(email, password)

        # Проверка, что пользователь залогинен
        login_page.should_be_authorized_user()

    @pytest.mark.usefixtures("setup")
    def test_user_cant_see_success_message(self, browser):
        link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
        page = ProductPage(browser, link)
        page.open()
        page.should_not_be_success_message()

    @pytest.mark.usefixtures("setup")
    def test_user_can_add_product_to_basket(self, browser):
        link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
        page = ProductPage(browser, link)
        page.open()
        page.add_to_basket()
        product_name = page.get_product_name()
        page.should_be_success_message(product_name)