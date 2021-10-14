from selenium.webdriver.common.by import By


class LoginPageLocators:
    REGISTRATION_FORM = (By.CSS_SELECTOR, "[id ='register_form']")
    LOGIN_FORM = (By.CSS_SELECTOR, "[id ='login_form']")


class ProductPageLocators:
    ADD_TO_BASKET = (By.CSS_SELECTOR, "[class ='btn btn-lg btn-primary btn-add-to-basket']")
    PRODUCT_NAME = (By.CSS_SELECTOR, "ul.breadcrumb li.active")
    PRODUCT_PRICE = (By.CSS_SELECTOR, ".col-sm-6 p.price_color")
    MESSAGE_ITEM_ADDED_TO_BASKET = (By.CSS_SELECTOR, "div.alertinner strong")
    MESSAGE_BASKET_PRICE = (By.CSS_SELECTOR, ".alert.alert-safe.alert p strong")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, "#messages div:nth-child(1)")


class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")


class BasketPageLocators:
    BASKET_LINK = (By.CSS_SELECTOR, "a[class='btn btn-default']")
    PRODUCT_IN_THE_BASKET = (By.CSS_SELECTOR, "#id_form-0-quantity")
    EMPTY_BASKET_MESSAGE = (By.CSS_SELECTOR, "div#content_inner:nth-child(2) p")
