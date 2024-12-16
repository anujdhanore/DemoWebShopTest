from selenium.webdriver.common.by import By
#from page_objects import BaseClass  # Assuming you have a BaseClass in your project
from actions.Action import Action
from base.BaseClass import BaseClass

class LoginPage(Action):

    login_link = (By.LINK_TEXT, "Log in")
    emailId = (By.ID,"Email")
    passWord = (By.ID, "Password")
    submit_btn = (By.XPATH, "//input[@value='Log in']")
    forgotPwd = (By.XPATH, "//tr[@class='weblogin']//div[@class='m-t20']/span/a")
    registerNew = (By.XPATH, "//tr[@class='weblogin']//div[@class='m-t20']/a")

    def login(self, email, pswd):
        self.click_ele(self.login_link)
        self.type_text(self.emailId, email)
        self.type_text(self.passWord, pswd)

        # Click the login button
        self.click_ele(self.submit_btn)