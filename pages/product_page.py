from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoAlertPresentException
import math
from .base_page import BasePage
from .locators import ProductPageLocators
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

class ProductPage(BasePage):
    def add_to_basket_promotion(self):
        add_button = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET)
        add_button.click()
        self.solve_quiz_and_get_code()
    # Решение квиза(капчи)
    def solve_quiz_and_get_code(self):
        alert = self.browser.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()
        try:
            alert = self.browser.switch_to.alert
            alert_text = alert.text
            print(f"Your code: {alert_text}")
            alert.accept()
        except NoAlertPresentException:
            print("No second alert presented")
    

    # Метод для добавления товара в корзину без квиза
    def add_to_basket(self):
        add_button = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET)
        add_button.click()

    
    def get_product_name(self):
        return self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text

    def get_product_price(self):
        return self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text

    def get_success_message(self):
        return self.browser.find_element(*ProductPageLocators.SUCCESS_MESSAGE).text

    def get_basket_total(self):
        return self.browser.find_element(*ProductPageLocators.BASKET_TOTAL).text

    def should_be_success_message(self, product_name):
        WebDriverWait(self.browser, 10).until(
          EC.presence_of_element_located(ProductPageLocators.SUCCESS_MESSAGE)
        )
        assert self.is_element_present(*ProductPageLocators.SUCCESS_MESSAGE), "Success message is not present"
        assert product_name in self.get_success_message(), "Success message does not match"

    def should_be_basket_total(self, product_price):
        assert self.is_element_present(*ProductPageLocators.BASKET_TOTAL), "Basket total is not present"
        assert product_price in self.get_basket_total(), "Basket total does not match product price"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
        "Success message is presented, but should not be"