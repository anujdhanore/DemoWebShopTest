from selenium.webdriver.common.by import By

from actions.Action import Action


class RegistrationPage(Action):
    register_link = (By.LINK_TEXT, "Register")
    gender = (By.ID, "gender-male")
    first_name = (By.ID, "FirstName")
    last_name = (By.ID, "LastName")
    email = (By.ID, "Email")
    password = (By.ID, "Password")
    confirm_password = (By.ID, "ConfirmPassword")
    register_button = (By.ID, "register-button")
    continue_button = (By.XPATH, "//div[@class='page registration-result-page']//input")
    logout_btn = (By.LINK_TEXT, "Log out")

    def register_user(self, fname, lname, email, pwd, cnfpwd):
            self.click_ele(self.register_link)
            self.click_ele(self.gender)
            self.type_text(self.first_name, fname)
            self.type_text(self.last_name, lname)
            self.type_text(self.email, email)
            self.type_text(self.password, pwd)
            self.type_text(self.confirm_password, cnfpwd)

            self.click_ele(self.register_button)
            assert self.find_ele(self.continue_button).is_displayed()
            self.click_ele(self.continue_button)
            self.click_ele(self.logout_btn)
