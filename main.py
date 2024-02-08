import csv
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--start-maximized")

driver = webdriver.Remote(
    command_executor='http://localhost:4444', options=chrome_options)
driver.get('https://loterias.caixa.gov.br/Paginas/Mega-Sena.aspx')
sleep(10)

with open('Data.csv', 'w', newline='') as csvfile:
    csvwriter = csv.writer(csvfile)

    for _ in range(10):
        xpathBalls = []
        day = '//*[@id="wp_resultados"]/div[1]/div/h2/span'
        buttonXpath = '//*[@id="wp_resultados"]/div[1]/div/div[2]/ul/li[2]/a'
        day_element = driver.find_element(By.XPATH, day)
        day_value = day_element.text

        for i in range(0, 5):
            xpathBalls.append(f'//*[@id="ulDezenas"]/li[{i+1}]')

        balls = []
        for xpath in xpathBalls:
            ball_element = driver.find_element(By.XPATH, xpath)
            ball_value = ball_element.text
            balls.append(ball_value)

        csvwriter.writerow([day_value] + balls)

        button = driver.find_element(By.XPATH, buttonXpath)
        button.click()
        sleep(2)

driver.quit()
