This project will only work correctly if you have Python and Java installed on your machine.

# Web Data Scraping Project using Python

This is a learning project focused on practicing Web Scraping, a technique used to extract information from websites in an automated manner. The project has been entirely developed in Python, a widely-used programming language in data analysis and task automation.

## Objective

The main goal of this project is to demonstrate how to collect data from the web.

## Features

- **Data Extraction:** The project allows for the automated extraction of data from web pages, including text, images, links, and more.
- **Data Manipulation:** After extraction, the data can be manipulated and processed according to the user's needs.
- **Storage:** The data can be stored in various formats, such as CSV, JSON, or even in a database for further analysis.

## Technologies Used

- **Python:** Programming language used for project development.
- **Selenium:** Automation tool for controlling web browsers, commonly used for web scraping dynamic content and simulating user interactions.

## How to Use

1. Install project dependencies using the `requirements.txt` file.

   ```
   pip install -r requirements.txt
   ```

2. Select the webdriver of your preference and download it. For example, I used the Chrome driver.

3. Download the webdriver for your preferred browser version and place it in your project directory. You can find the Chrome driver at [ChromeDriver Downloads](https://googlechromelabs.github.io/chrome-for-testing/).

4. Execute the chromedriver in your terminal.

   ```
   ./chromedriver.exe
   ```

5. Execute the Selenium server in your terminal.

   ```
   java -jar selenium-server-4.7.2.jar standalone
   ```

6. Execute the Python scripts available in the project folder to perform the desired data collection.

7. The data will be saved in the format specified in the scripts or according to user preferences.

**Enjoy scraping the web!**

**Note:** This project uses Selenium and other web scraping techniques to extract data from websites. While Selenium is effective for web scraping dynamic content, it can be slower compared to other methods like BeautifulSoup or Scrapy, especially for static sites. This approach has been chosen for educational purposes to demonstrate automation, but for faster data extraction, consider using APIs or libraries like BeautifulSoup (for static HTML) or Scrapy.
