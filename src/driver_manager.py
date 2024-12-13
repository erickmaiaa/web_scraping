from selenium import webdriver

def initialize_driver():
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--start-maximized")

    driver = webdriver.Remote(
        command_executor='http://localhost:4444', options=chrome_options)
    return driver