import pytest
from pages.browse_page import BrowsePage
import pdb, time

class TestBrowsePage:
    @pytest.fixture(scope="function")
    def setup(self, driver):
        self.page = BrowsePage(driver)
        yield
        driver.quit()

    def test_streamering_starcraft_ii(self, setup):
        self.page.navigate_to(url='/directory')
        assert self.page.get_title() == "All Categories - Twitch"
        self.page.search("Starcraft II")
        self.page.scroll_down(0, 100)
        self.page.scroll_down(0, 100)
        self.page.select_one_streamer()
        self.page.wait_until_streamering_loaded()
        self.page.take_screenshot("test_streamer_starcraft_ii.png")
        
