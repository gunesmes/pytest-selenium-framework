import pytest
from selenium import webdriver
from utils.driver_factory import DriverFactory
from utils import config

@pytest.fixture(scope="session")
def driver():
    driver_factory = DriverFactory(mobile_emulation=config.pixel_7_emulation)
    driver = driver_factory.create_driver()
    yield driver
    driver_factory.close_driver(driver)