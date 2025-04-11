import argparse
from src.core.driver_manager import initialize_driver
from src.scraper.mega_sena_scraper import (
    get_contest_and_date,
    get_drawn_balls,
    click_next_contest_button,
    wait_for_element
)
from src.utils.file_handler import write_to_csv
from src.config import SELENIUM_GRID_URL, TARGET_URL, BUSCA_CONCURSO_INPUT_XPATH, WAIT_TIMEOUT
from selenium.webdriver.common.by import By


def main(num_results):
    driver = None
    try:
        driver = initialize_driver(SELENIUM_GRID_URL)
        driver.get(TARGET_URL)

        print(f"Waiting up to {WAIT_TIMEOUT} seconds for page to load...")
        if not wait_for_element(driver, By.XPATH, BUSCA_CONCURSO_INPUT_XPATH):
            print("Initial page load failed or element not found. Exiting.")
            return

        print("Page loaded. Starting scraping...")
        results_data = []
        scraped_count = 0

        for i in range(num_results):
            print(f"Scraping result {i + 1}...")
            contest, date = get_contest_and_date(driver)
            balls = get_drawn_balls(driver)

            if contest and date and len(balls) == 6:
                results_data.append([contest, date] + balls)
                scraped_count += 1
                print(
                    f"  > Scraped: Contest {contest}, Date {date}, Balls {balls}")
            else:
                print(
                    f"  > Failed to scrape data for result {i + 1}. Skipping.")
                # Optional: Add a small delay or retry mechanism here if needed

            if i < num_results - 1:
                print("  > Clicking next button...")
                if not click_next_contest_button(driver):
                    print("Failed to navigate to the next result. Stopping scrape.")
                    break
            else:
                print("Reached desired number of results.")

        if results_data:
            write_to_csv(results_data)
        else:
            print("No data was successfully scraped.")

    except Exception as e:
        print(f"An unexpected error occurred in main execution: {e}")
    finally:
        if driver:
            print("Closing WebDriver.")
            driver.quit()


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Scrape Mega-Sena results from Caixa website.")
    parser.add_argument(
        "-n", "--num_results",
        type=int,
        default=10,
        help="Number of past results to scrape (default: 10)"
    )
    args = parser.parse_args()

    if args.num_results <= 0:
        print("Error: Number of results must be positive.")
    else:
        main(args.num_results)
