import pytest
from .pages.product_page import ProductPage

@pytest.mark.parametrize('link', [
    "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
    "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1",
    "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2",
    # "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3",
    # "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4",
    # "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5",
    # "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6",
    # pytest.param("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7", marks=pytest.mark.xfail),
    # "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8",
    # "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9"
])
def test_guest_can_add_product_to_basket(browser, link):
    page = ProductPage(browser, link)
    page.open()  # Открываем страницу товара
    page.add_to_basket()  # Добавляем товар в корзину

    # Получаем название и цену товара из страницы
    product_name = page.get_product_name()
    product_price = page.get_product_price()

    # Проверяем, что появилось сообщение об успешном добавлении
    page.should_be_success_message(product_name)

    # Проверяем, что итоговая сумма в корзине соответствует цене товара
    page.should_be_basket_total(product_price)

    # Если тест не прошел, выводим информацию о ссылке
    print(f"Тест завершился для ссылки: {link}")

def test_should_not_be_success_message(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0"
    page = ProductPage(browser, link)
    page.open()  # Открываем страницу товара
    page.should_not_be_success_message()
