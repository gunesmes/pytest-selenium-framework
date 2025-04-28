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
  pytest --mobile_emulation=iphone_12 src/tests/test_home_page.py
  ```

- **Running tests with mobile emulation:**
  Modify the `driver_factory.py` to set the desired mobile device settings. Valid options are `iphone_12`, `iphone_15`, `samsung_galaxy_s20_ultra`, `pixel_7`, or `None` to disable mobile emulation.

## Contributing
Contributions are welcome! Please submit a pull request or open an issue for any enhancements or bug fixes.

## License
This project is licensed under the MIT License. See the LICENSE file for details.