# pytest-selenium-framework

## Overview
This project is a testing framework built using Python, pytest, and Selenium. It implements the Page Object Model (POM) design pattern to organize test code and improve maintainability. The framework is designed to facilitate automated testing of web applications with support for mobile emulation using ChromeDriver.

## Project Structure
```
pytest-selenium-framework
├── src
│   ├── pages
│   │   ├── base_page.py
│   │   └── home_page.py
│   ├── tests
│   │   ├── conftest.py
│   │   └── test_home_page.py
│   └── utils
│       ├── config.py
│       └── driver_factory.py
├── requirements.txt
├── pytest.ini
└── README.md
```

**Framework Structure Explanation:**

*   **`src/pages`:** This directory contains the Page Objects. Each page in your web application should have a corresponding Page Object class. Page Objects encapsulate the elements and actions that can be performed on a specific page.
    *   [`base_page.py`](base_page.py ): This file defines the `BasePage` class, which serves as the base class for all Page Objects. It provides common methods for interacting with web elements, such as `find_element`, `click`, `send_keys`, and `navigate_to`.
    *   [`home_page.py`](home_page.py ): This file contains the `HomePage` class, which is an example Page Object for the home page of your web application. It inherits from `BasePage` and defines methods specific to the home page, such as `get_title` and `click_login`.
*   **`src/tests`:** This directory contains the test files. Each test file should contain one or more test functions that verify the behavior of your web application.
    *   [`conftest.py`](conftest.py ): This file is used to define pytest configuration settings and fixtures. Fixtures are functions that provide a fixed baseline for your tests, such as a WebDriver instance or a logged-in user.
    *   [`test_home_page.py`](test_home_page.py ): This file contains example test functions for the home page of your web application. It uses the `HomePage` Page Object to interact with the home page and verify its behavior.
*   **`src/utils`:** This directory contains utility files that are used by the framework.
    *   [`config.py`](config.py ): This file defines configuration settings for the framework, such as the base URL of your web application and the timeout values for WebDriver operations.
    *   [`driver_factory.py`](driver_factory.py ): This file defines the `DriverFactory` class, which is responsible for creating and managing WebDriver instances. It supports different browsers and mobile emulation settings.

## Writing New Tests

To write new tests using this framework, follow these steps:

1.  **Identify the page you want to test:** Determine which page in your web application you want to write tests for.
2.  **Create a Page Object (if one doesn't exist):** If a Page Object doesn't already exist for the page you want to test, create a new file in the `src/pages` directory and define a new class that inherits from `BasePage`. Implement methods in the Page Object that represent the actions that can be performed on that page.
3.  **Create a test file:** Create a new file in the `src/tests` directory and define one or more test functions.
4.  **Use the Page Object in your tests:** In your test functions, create an instance of the Page Object for the page you want to test. Use the methods of the Page Object to interact with the page and verify its behavior.
5.  **Run your tests:** Use the `pytest` command to run your tests.

## Setup Instructions

1. **Clone the repository:**

## Setup Instructions

1. **Clone the repository:**
   ```
   git clone https://github.com/yourusername/pytest-selenium-framework.git
   cd pytest-selenium-framework
   ```

2. **Install dependencies:**
   Ensure you have Python installed, then run:
   ```
   pip install -r requirements.txt
   ```

3. **Configure ChromeDriver:**
   Download the appropriate version of ChromeDriver for your system from [ChromeDriver downloads](https://sites.google.com/chromium.org/driver/). Ensure that the ChromeDriver executable is in your system's PATH.

4. **Run Tests:**
   To execute the tests, run:
   ```
   pytest src/tests
   ```

## Usage Examples

- **Running a specific test with Iphone 12:**
  ```
  pytest --mobile_emulation=iphone_12 src/tests/test_browse_page.py
  ```

Test result:
```bash
(.venv) ➜  pytest-selenium-framework git:(main) ✗ pytest -v --mobile_emulation=iphone_12 src/tests/test_browse_page.py
============================================================================================== test session starts ===============================================================================================
platform darwin -- Python 3.10.8, pytest-8.3.5, pluggy-1.5.0 -- /Users/mesutgunes/projects/personal/pytest-selenium-framework/.venv/bin/python3
cachedir: .pytest_cache
metadata: {'Python': '3.10.8', 'Platform': 'macOS-13.4-arm64-arm-64bit', 'Packages': {'pytest': '8.3.5', 'pluggy': '1.5.0'}, 'Plugins': {'html': '4.1.1', 'metadata': '3.1.1', 'cov': '6.1.1'}, 'JAVA_HOME': '/Library/Java/JavaVirtualMachines/adoptopenjdk-8.jdk/Contents/Home'}
rootdir: /Users/mesutgunes/projects/personal/pytest-selenium-framework
configfile: pytest.ini
plugins: html-4.1.1, metadata-3.1.1, cov-6.1.1
collected 1 item                                                                                                                                                                                                 

src/tests/test_browse_page.py::TestBrowsePage::test_streamering_starcraft_ii PASSED                                                                                                                        [100%]

=============================================================================================== 1 passed in 13.15s ===============================================================================================
```

- **Running tests with mobile emulation:**
  Modify the `driver_factory.py` to set the desired mobile device settings. Valid options are `iphone_12`, `iphone_15`, `samsung_galaxy_s20_ultra`, `pixel_7`, or `None` to disable mobile emulation.

## Contributing
Contributions are welcome! Please submit a pull request or open an issue for any enhancements or bug fixes.

## License
This project is licensed under the MIT License. See the LICENSE file for details.