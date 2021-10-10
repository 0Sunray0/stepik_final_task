from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def should_be_promo_url(self):
        assert "/?promo=" in self.browser.current_url, "Substring '/?promo=' is not present in the " \
                                                              "current url "

    def should_be_a_button_to_add_to_basket(self):
        assert self.is_element_present(*ProductPageLocators.ADD_TO_BASKET), "Button 'Add to basket' not found"

    def add_product_to_basket(self):
        basket = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET)
        basket.click()

    def should_be_message_item_added_to_basket(self):
        message_product_name = self.browser.find_element(*ProductPageLocators.MESSAGE_ITEM_ADDED_TO_BASKET).text
        product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text
        assert message_product_name == product_name, "The product name in the message does not match the added product."

    def should_be_basket_value_message(self):
        message_product_price = self.browser.find_element(*ProductPageLocators.MESSAGE_BASKET_PRICE).text
        product_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text
        assert message_product_price == product_price, "The price of the basket does not match the price of the item."

