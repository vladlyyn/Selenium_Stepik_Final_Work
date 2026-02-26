from .base_page import BasePage
from .locators import MainPageLocators
from .login_page import LoginPage
from .locators import BasketPageLocators
from selenium.webdriver.common.by import By

class BasketPage(BasePage):
    def should_not_be_goods_in_basket_page(self):
        assert self.is_not_element_present(*BasketPageLocators.GOODS_IN_BASKET), \
       "The product is in the bucket, but should not be" 

    def should_be_empty_basket_text(self):
        assert self.is_element_present(*BasketPageLocators.EMPTY_BASKET_TEXT), \
       "There is no empty basket text" 