from .pages.product_page import ProductPage
from .pages.basket_page import BasketPage
from .pages.login_page import LoginPage
import pytest
import random
import time

# @pytest.mark.parametrize('link', ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
#                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1",
#                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2",
#                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3",
#                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4",
#                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5",
#                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6",
#                                    pytest.param("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7", marks=pytest.mark.xfail),
#                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8",
#                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9"])

class TestUserAddToBasketFromProductPage():
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        link = "http://selenium1py.pythonanywhere.com/en-gb/accounts/login/"
        self.login_page = LoginPage(browser, link)
        self.login_page.open()
        count = random.randint(1, 100)
        email = str(time.time()) + "@fakemail.org"
        password = str(time.time() + count)
        self.login_page.register_new_user(email, password)
        self.login_page.should_be_authorized_user()

    def test_user_cant_see_success_message(self, browser):
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
        page = ProductPage(browser, link)
        page.open()
        page.should_not_be_success_message()

    def test_user_can_add_product_to_basket(self, browser):
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
        page = ProductPage(browser,
                           link)  # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
        page.open()  # открываем страницу
        page.add_product_to_basket()  # выполняем метод страницы — добавляем товар в корзину
        # page.solve_quiz_and_get_code()
        page.should_be_success_message()  # получить сообщение о добавлении товара к корзину
        page.should_be_book_name()
        page.should_be_book_price()

# def test_guest_can_add_product_to_basket(browser, link):
#
#     page = ProductPage(browser, link)   # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
#     page.open()                      # открываем страницу
#     page.add_product_to_basket()          # выполняем метод страницы — добавляем товар в корзину
#     page.solve_quiz_and_get_code()
#     page.should_be_success_message()  # получить сообщение о добавлении товара к корзину
#     page.should_be_book_name()
#     page.should_be_book_price()

# def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
#     page = ProductPage(browser, link)
#     page.open()
#     page.add_product_to_basket()
#     page.should_not_be_success_message()
#
# def test_guest_cant_see_success_message(browser):
#     page = ProductPage(browser, link)
#     page.open()
#     page.should_not_be_success_message()
#
# def test_message_disappeared_after_adding_product_to_basket(browser):
#     page = ProductPage(browser, link)
#     page.open()
#     page.add_product_to_basket()
#     page.message_disappeared_after_adding_product_to_basket()
#
# def test_guest_should_see_login_link_on_product_page(browser):
#     page = ProductPage(browser, link)
#     page.open()
#     page.should_be_login_link()
#
# def test_guest_can_go_to_login_page_from_product_page(browser):
#     page = ProductPage(browser, link)
#     page.open()
#     page.go_to_login_page()
#
# def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
#     page = ProductPage(browser, link)
#     page.open()
#     page.go_to_basket_page()
#     basket_page = BasketPage(browser, browser.current_url)
#     basket_page.is_basket_empty()
#     basket_page.should_be_basket_empty_message()


