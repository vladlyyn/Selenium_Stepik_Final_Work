from .pages.main_page import MainPage
from .pages.login_page import LoginPage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# def test_guest_can_go_to_login_page(browser):
#    link = "http://selenium1py.pythonanywhere.com/"
#    page = MainPage(browser, link)
#    page.open()
#    page.go_to_login_page()#

# def test_guest_should_see_login_link(browser):
#    link = "http://selenium1py.pythonanywhere.com/"
#    page = MainPage(browser, link)
#    page.open()
#    page.should_be_login_link()#

# def test_guest_should_see_login_form(browser):
#    link = "http://selenium1py.pythonanywhere.com/en-gb/accounts/login/"
#    page = LoginPage(browser, link)
#    page.open()
#    page.should_be_login_form()#

# def test_guest_should_see_register_form(browser):
#    link = "http://selenium1py.pythonanywhere.com/en-gb/accounts/login/"
#    page = LoginPage(browser, link)
#    page.open()
#    page.should_be_register_form()

def test_should_be_login_in_url(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/accounts/login/"
    page = LoginPage(browser, link)
    page.open()
    page.should_be_login_url()



