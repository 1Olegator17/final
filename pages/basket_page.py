from .locators import BasketPageLocators
from .base_page import BasePage

class BasketPage(BasePage):
    def __init__(self, browser, url):
        super().__init__(browser, url)  # Вызов конструктора родительского класса


    def open(self):
        self.browser.get(self.url)

    def should_be_empty_basket_message(self):
        assert self.is_element_present(*BasketPageLocators.EMPTY_BASKET_MESSAGE), "Basket is not empty"
        
    def should_not_be_products_in_basket(self):
        assert self.is_not_element_present(*BasketPageLocators.PRODUCTS_IN_BASKET), "Basket is not empty, products are present"