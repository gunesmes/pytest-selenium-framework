class DriverFactory:
    def __init__(self, mobile_emulation=None):
        self.mobile_emulation = mobile_emulation

    def create_driver(self):
        from selenium import webdriver
        from selenium.webdriver.chrome.service import Service
        from webdriver_manager.chrome import ChromeDriverManager

        options = webdriver.ChromeOptions()
        
        if self.mobile_emulation:
            options.add_experimental_option("mobileEmulation", self.mobile_emulation)
        else:
            options.add_argument("--start-maximized")

        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

        # Set the window size for mobile emulation
        # This is a workaround for the issue with mobile emulation not setting the window size correctly        
        if self.mobile_emulation:
            width = self.mobile_emulation['deviceMetrics']['width']
            height = self.mobile_emulation['deviceMetrics']['height']
            driver.set_window_size(width, height)
        return driver

    def close_driver(self, driver):
        driver.quit()