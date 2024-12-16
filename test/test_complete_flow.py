from base.BaseClass import BaseClass
from pages.buy_item_locators import BuyItemPage
from pages.checkout_page import CheckoutPage
from pages.login_page import LoginPage
from pages.registration_page import RegistrationPage
from test.test_data_file import get_test_data


class TestCases(BaseClass):

    def test_registration_test(self):
        data = get_test_data()["user_data"]
        rp = RegistrationPage(self.driver)
        rp.register_user(data["first_name"], data["last_name"], data["email"], data["password"], data["confirm_password"])

    def test_login(self):
        data = get_test_data()["user_data"]
        lp = LoginPage(self.driver)
        lp.login(data["email"], data["password"])

    def test_item_buy(self):
        data = get_test_data()["item"]
        bi = BuyItemPage(self.driver)
        bi.add_item_to_cart(data["item_name"])

    def test_checkout(self):
        data = get_test_data()["user_data"]
        co = CheckoutPage(self.driver)
        co.check_out(data["country"], data["city"], data["address1"], data["address2"], data["zip_code"],data["phone"])
