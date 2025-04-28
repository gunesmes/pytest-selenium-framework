from abc import ABC
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from utils import config 
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage(ABC):
    # Base class for all page objects that provides common methods and properties
    # to interact with the web page.
    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.base_url = config.base_url 
   
    def navigate_to(self, url: str = ""): 
        self.driver.get(self.base_url + url)

    def find_element(self, by: By, value: str):
        return self.driver.find_element(by, value)

    def find_elements(self, by: By, value: str):
        return self.driver.find_elements(by, value)
    
    def find_element_by_text(self, text: str):
        # Find an element by its visible text
        return self.driver.find_element(By.XPATH, f"//*[text()='{text}']")
    
    def wait_for_element(self, by: By, value: str, timeout: int = 10, poll_frequency: float = 1.0):
        return WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located((by, value)))
    
    def scroll_down(self, x: int, y: int):
        self.driver.execute_script("window.scrollTo(arguments[0], arguments[1]);", x, y)
        time.sleep(1)  # Optional: wait for the scroll to complete

    def take_screenshot(self, filename: str):
        self.driver.save_screenshot(filename)