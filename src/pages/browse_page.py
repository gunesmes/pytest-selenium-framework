from .base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

class BrowsePage(BasePage):
    # This class represents the browse page of the application.
    def get_title(self):
        return self.driver.title

    def search(self, text: str):
        search_input = self.find_element(By.CSS_SELECTOR, "input[type='search']")
        search_input.send_keys(text)
        search_input.send_keys(Keys.RETURN)

    def select_one_streamer(self):
        streamer = self.find_elements(By.XPATH, "//button[contains(@class, 'ScCoreLink-')]")[-1]
        streamer.click()
    
    def check_streamering_loaded(self):
        # Wait for the streamer page to load
        self.wait_for_element(By.XPATH, "//span[text()='Welcome to the chat room!']")
        self.wait_for_element(By.XPATH, "//div[text()='Follow']")
        self.wait_for_element(By.ID, "amazon-video-ads-in-stream-iframe")
        self.wait_for_element(By.ID, "amznidpxl")
        self.wait_for_element(By.ID, "amazon-companion-ad-div")
        self.wait_for_element(By.CSS_SELECTOR, "div[data-a-target='player-overlay-click-handler']")
        # To be sure that steaming is started, we can sniff the network traffic and 
        # check if .m3u8 requests are coming. This can be done using browsermob-proxy or similar tools.
        # For now, we will just wait for the elements that are present in the streamer page.
    
