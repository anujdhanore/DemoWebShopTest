from selenium.webdriver.common.by import By

from actions.Action import Action


class CheckoutPage(Action):
    country = (By.XPATH, "//select[@name='BillingNewAddress.CountryId']")
    city = (By.ID, "BillingNewAddress_City")
    add_1 = (By.XPATH, "//input[@name='BillingNewAddress.Address1']")
    add_2 = (By.XPATH, "//input[@name='BillingNewAddress.Address2']")
    zip_code = (By.XPATH, "//input[@name='BillingNewAddress.ZipPostalCode']")
    phone = (By.XPATH, "//input[@name='BillingNewAddress.PhoneNumber']")
    billing_address = (By.XPATH, "//div[@id='billing-buttons-container']/input")
    shipping_address = (By.XPATH, "//div[@id='shipping-buttons-container']/input")
    shipping_method = (By.XPATH, "//div[@id='shipping-method-buttons-container']/input")
    payment_method = (By.XPATH, "//div[@id='payment-method-buttons-container']/input")
    payment_info = (By.XPATH, "//div[@id='payment-info-buttons-container']/input")
    confirm_order = (By.XPATH, "//div[@id='confirm-order-buttons-container']/input")


    def check_out(self, countryname,cityname, address1, address2,zip, phoneno):
        self.select_by_visible_text(self.country, countryname)
        self.type_text(self.city, cityname)

        self.type_text(self.add_1, address1)
        self.type_text(self.add_2,address2)
        self.type_text(self.zip_code,zip)
        self.type_text(self.phone,phoneno)
        self.explicit_wait(self.billing_address, 20)
        self.click_ele(self.billing_address)
        self.explicit_wait(self.shipping_address, 20)
        self.click_ele(self.shipping_address)
        self.explicit_wait(self.shipping_method, 20)
        self.click_ele(self.shipping_method)
        self.explicit_wait(self.payment_method, 20)
        self.click_ele(self.payment_method)
        self.explicit_wait(self.payment_info, 20)
        self.click_ele(self.payment_info)
        self.explicit_wait(self.confirm_order, 20)
        self.click_ele(self.confirm_order)
        self.screenshot_take()

