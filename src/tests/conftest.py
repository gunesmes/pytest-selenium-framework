import pytest
from selenium import webdriver
from utils.driver_factory import DriverFactory
from utils import config

def pytest_addoption(parser):
    parser.addoption(
        "--mobile_emulation",
        action="store",
        default=None,
        help="Specify mobile emulation to use (iphone_12, iphone_15, samsung_galaxy_s20_ultra, pixel_7, or None)",
    )


@pytest.fixture(scope="session")
def driver(request):
    mobile_emulation_option = request.config.getoption("--mobile_emulation")

    mobile_emulation = None

    if mobile_emulation_option == "iphone_12":
        mobile_emulation = config.iphone_12_emulation
    elif mobile_emulation_option == "iphone_15":
        mobile_emulation = config.iphone_15_emulation
    elif mobile_emulation_option == "samsung_galaxy_s20_ultra":
        mobile_emulation = config.samsung_galaxy_s20_ultra_emulation
    elif mobile_emulation_option == "pixel_7":
        mobile_emulation = config.pixel_7_emulation
    elif mobile_emulation_option is not None and mobile_emulation_option.lower() != "none":
        print(f"Warning: Invalid mobile_emulation option: {mobile_emulation_option}.  Using default (None).")


    driver_factory = DriverFactory(mobile_emulation=mobile_emulation)
    driver = driver_factory.create_driver()
    yield driver
    driver_factory.close_driver(driver)