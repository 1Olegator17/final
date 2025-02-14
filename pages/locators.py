from selenium.webdriver.common.by import By

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    BASKET_LINK = (By.CSS_SELECTOR, "a.btn.btn-default[href*='/basket/']")


class LoginPageLocators:
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")  
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")  

class ProductPageLocators:
    ADD_TO_BASKET = (By.CSS_SELECTOR, ".btn-add-to-basket")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, ".alertinner strong")
    BASKET_TOTAL = (By.CSS_SELECTOR, ".alert-info .alertinner p")
    PRODUCT_NAME = (By.CSS_SELECTOR, ".product_main h1")
    PRODUCT_PRICE = (By.CSS_SELECTOR, ".product_main .price_color")


class BasketPageLocators():
    EMPTY_BASKET_MESSAGE = (By.CSS_SELECTOR, "#content_inner > p")
    PRODUCTS_IN_BASKET = (By.CSS_SELECTOR, ".basket-items")  


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
