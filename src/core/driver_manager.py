from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions


def initialize_driver(selenium_grid_url):
    chrome_options = ChromeOptions()
    chrome_options.add_argument("--start-maximized")
    try:
        driver = webdriver.Remote(
            command_executor=selenium_grid_url,
            options=chrome_options
        )
        return driver
    except Exception as e:
        print(f"Error initializing WebDriver: {e}")
        print(f"Ensure the Selenium Grid is running at {selenium_grid_url}")
        raise
