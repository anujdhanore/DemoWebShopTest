from datetime import datetime
import os.path

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait


class Action:

    def __init__(self, driver):
        self.driver = driver

    def find_ele(self, ele):
        return self.driver.find_element(*ele)

    def find_eles(self, ele):
        return self.driver.find_elements(*ele)

    def scroll_by_visibility_of_element(self, ele):
        self.driver.execute_script("arguments[0].scrollIntoView();", ele)

    def click_ele(self, locator_name):
        # To perform click without moving to the element
        # self.driver.find_element(*locator_name).click()
        self.find_ele(locator_name).click()

    def type_text(self, locator, text):
        """
        This method types the given text into a field identified by `locator`.
        Returns True if the text was successfully entered, False otherwise.
        """
        flag = False
        try:
            # Check if the element is displayed
            flag = self.find_ele(locator).is_displayed()
            if flag:
                # Clear any existing text and send the new text
                self.find_ele(locator).clear()
                self.find_ele(locator).send_keys(text)
                flag = True
        except Exception as e:
            print(f"Location Not found: {locator}")
            flag = False
        finally:
            if flag:
                print(f"Successfully entered value at: \"{locator}\"")
            else:
                print(f"Unable to enter value at: \"{locator}\"")
        return flag

    def implicitly_wait(self, sec):
        self.driver.implicitly_wait(sec)

    def page_load_timeout(self, sec):
        self.driver.set_page_load_timeout(sec)

    def explicit_wait(self, element, sec):
        wait = WebDriverWait(self.driver, sec)
        wait.until(EC.element_to_be_clickable(self.find_ele(element)))

    def explicit_wait_visible(self, element):
        wait = WebDriverWait(self.driver, 30)
        wait.until(EC.visibility_of(self.find_ele(element)))

    def explicit_wait_invisible(self, element, sec):
        wait = WebDriverWait(self.driver, sec)
        wait.until(EC.invisibility_of_element(self.find_ele(element)))

    def select_by_index(self, locator, index):
        flag = False
        try:
            select = Select(self.find_ele(locator))
            select.select_by_index(index)
            flag = True
            return True
        except Exception as e:
            return False
        finally:
            if flag:
                print(f"Option selected by Index {index}")
            else:
                print(f"Option not selected by Index {index}")

    def select_by_value(self, locator, value):
        flag = False
        try:
            select = Select(self.find_ele(locator))
            select.select_by_value(value)
            flag = True
            return True
        except Exception as e:
            return False
        finally:
            if flag:
                print(f"Option selected by Value {value}")
            else:
                print(f"Option not selected by Value {value}")

    def select_by_visible_text(self, locator, text):
        flag = False
        try:
            select = Select(self.find_ele(locator))  # Assuming 'driver' is defined globally
            select.select_by_visible_text(text)
            flag = True
            return True
        except Exception as e:
            return False
        finally:
            if flag:
                print(f"Option selected by VisibleText {text}")
            else:
                print(f"Option not selected by VisibleText {text}")

    def screenshot_take(self):
        screenshot_dir = os.path.join(os.getcwd(),"Screenshots")

        if not os.path.exists(screenshot_dir):
            os.makedirs(screenshot_dir)

        date_name = datetime.now().strftime("%d_%m_%Y_%H_%M_%S")
        screenshot_path = os.path.join(screenshot_dir,f"screenshot_{date_name}.png")
        try:
            self.driver.save_screenshot(screenshot_path)
            print(f"Screenshot saved at {screenshot_path}")
        except Exception as e:
            print(f"Error while taking screenshot: {e}")



