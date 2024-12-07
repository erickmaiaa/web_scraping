from selenium.webdriver.common.by import By
from time import sleep

def get_day(driver):
    xpath_day = '//*[@id="wp_resultados"]/div[1]/div/h2/span'
    day_element = driver.find_element(By.XPATH, xpath_day)

    # Obter o texto completo: "Concurso 2804 (05/12/2024)"
    full_text = day_element.text

    # Extrair o número do concurso (parte antes do parêntese)
    concurso = full_text.split(' ')[1]

    # Extrair a data (parte dentro do parêntese)
    day = full_text.split('(')[1].replace(')', '').strip()

    return concurso, day


def get_balls(driver):
    balls = []
    for i in range(1, 7):
        xpath_ball = f'//*[@id="ulDezenas"]/li[{i}]'
        ball_element = driver.find_element(By.XPATH, xpath_ball)
        balls.append(ball_element.text)
    return balls

def click_next_button(driver):
    button_xpath = '//*[@id="wp_resultados"]/div[1]/div/div[2]/ul/li[2]/a'
    button = driver.find_element(By.XPATH, button_xpath)
    button.click()
    sleep(2)