from time import sleep
from src.driver_manager import initialize_driver
from src.scraper import get_day, get_balls, click_next_button
from src.file_handler import write_to_csv

def main():
    driver = initialize_driver()
    driver.get('https://loterias.caixa.gov.br/Paginas/Mega-Sena.aspx')
    sleep(20)

    data = []
    for _ in range(10):
        concurso, day = get_day(driver)  # Agora retorna dia e concurso
        balls = get_balls(driver)
        
        # Organiza os dados separando Concurso e Dia
        data.append([concurso, day] + balls)
        click_next_button(driver)

    write_to_csv(data)

    driver.quit()

if __name__ == "__main__":
    main()