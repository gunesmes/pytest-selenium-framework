from .base_page import BasePage
from selenium.webdriver.common.by import By

class HomePage(BasePage):
    def get_title(self):
        return self.driver.title

    def click_login(self):
        login_button = self.find_element_by_text("Log in")
        login_button.click()