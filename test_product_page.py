from .pages.product_page import ProductPage
import pytest

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

promo = ["0", "1", "2", "3", "4", "5", "6", pytest.param("7", marks=pytest.mark.xfail), "8", "9"]

@pytest.mark.parametrize('promolink', promo)
def test_guest_can_add_product_to_basket(browser, promolink):
    link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{promolink}"
    print(f"\n📚 Тестируем промо {promolink}")
    page = ProductPage(browser, link)
    page.open()
    page.click_on_basket_button()
    page.solve_quiz_and_get_code()
    # time.sleep(1)
    page.should_be_product_name_alert()
    page.should_be_price_alert()





