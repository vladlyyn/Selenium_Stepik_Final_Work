from .base_page import BasePage
from .locators import ProductPageLocators
from .login_page import LoginPage
from selenium.webdriver.common.by import By

class ProductPage(BasePage):
    def click_on_basket_button(self):
        basket_button = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON)
        basket_button.click()

    def should_be_product_name_alert(self):
        product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text
        product_name_alert = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME_ALERT).text
        assert product_name == product_name_alert, "Should be same value in product name"
        print('Name of product and alert are the same!🎉')

    def should_be_price_alert(self):
        product_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text
        product_price_alert = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE_ALERT).text
        assert product_price == product_price_alert, "Should be same value in product price"
        print('Name of price and alert are the same!🎉')

    def should_not_be_success_message_is_not_present(self):
        assert self.is_not_element_present(*ProductPageLocators.PRODUCT_NAME_ALERT), \
       "Success message is presented, but should not be"

    def should_not_be_success_message_disappeared(self):
        assert self.is_disappeared(*ProductPageLocators.PRODUCT_NAME_ALERT), \
            "Success message is still present, but it should have disappeared"





