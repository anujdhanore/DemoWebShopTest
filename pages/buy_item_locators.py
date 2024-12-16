from selenium.webdriver.common.by import By

from actions.Action import Action


class BuyItemPage(Action):
    computers_link = (By.XPATH, "//ul[@class='list']//a[@href='/computers']")
    desktop_link = (By.XPATH, "//ul[@class='list']//a[@href='/desktops']")
    items_list = (By.XPATH, "//div[@class='product-grid']//h2/a")
    add_to_cart = (By.XPATH, "//input[@value ='Add to cart']")
    add_to_cart2 = (By.XPATH, "//div[@class='add-to-cart']//input[2]")
    shopping_cart_link = (By.PARTIAL_LINK_TEXT, "Shopping cart")
    term_Condition = (By.ID, "termsofservice")
    checkout = (By.ID, "checkout")

    def add_item_to_cart(self, c_name):
            self.click_ele(self.computers_link)
            self.click_ele(self.desktop_link)

            c_list = self.find_eles(self.items_list)
            for item in c_list:
                item_name = item.text
                if item_name == c_name:
                    self.click_ele(self.add_to_cart)
                    break

            self.click_ele(self.add_to_cart2)
            self.click_ele(self.shopping_cart_link)
            self.click_ele(self.term_Condition)
            self.click_ele(self.checkout)
