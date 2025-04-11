from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException

from src.config import (
    CONTEST_DATE_XPATH,
    BALL_LIST_XPATH,
    NEXT_BUTTON_XPATH,
    WAIT_TIMEOUT
)


def wait_for_element(driver, by, value, timeout=WAIT_TIMEOUT):
    try:
        element = WebDriverWait(driver, timeout).until(
            EC.visibility_of_element_located((by, value))
        )
        return element
    except TimeoutException:
        print(
            f"Error: Element {value} not found or visible within {timeout} seconds.")
        return None


def wait_for_clickable_element(driver, by, value, timeout=WAIT_TIMEOUT):
    try:
        element = WebDriverWait(driver, timeout).until(
            EC.element_to_be_clickable((by, value))
        )
        return element
    except TimeoutException:
        print(
            f"Error: Element {value} not clickable within {timeout} seconds.")
        return None


def get_contest_and_date(driver):
    element = wait_for_element(driver, By.XPATH, CONTEST_DATE_XPATH)
    if not element:
        return None, None

    full_text = element.text
    try:
        parts = full_text.split('(')
        contest_part = parts[0].split()[-1]
        date_part = parts[1].replace(')', '').strip()
        return contest_part, date_part
    except (IndexError, ValueError) as e:
        print(f"Error parsing contest/date string '{full_text}': {e}")
        return None, None


def get_drawn_balls(driver):
    balls = []
    try:
        ball_elements = WebDriverWait(driver, WAIT_TIMEOUT).until(
            EC.presence_of_all_elements_located((By.XPATH, BALL_LIST_XPATH))
        )
        if len(ball_elements) >= 6:
            # Get first 6 balls text
            balls = [el.text for el in ball_elements[:6]]
        else:
            print(f"Warning: Found only {len(ball_elements)} ball elements.")
            # Get text from available balls
            balls = [el.text for el in ball_elements]

    except TimeoutException:
        print(f"Error: Ball elements not found within {WAIT_TIMEOUT} seconds.")
    except Exception as e:
        print(f"An unexpected error occurred while getting balls: {e}")

    return balls


def click_next_contest_button(driver):
    button = wait_for_clickable_element(driver, By.XPATH, NEXT_BUTTON_XPATH)
    if button:
        try:
            # Get current contest number to check for change later
            current_contest_element = wait_for_element(
                driver, By.XPATH, CONTEST_DATE_XPATH)
            current_contest_text = current_contest_element.text if current_contest_element else ""

            button.click()

            # Wait until the contest number actually changes
            WebDriverWait(driver, WAIT_TIMEOUT).until(
                lambda d: wait_for_element(d, By.XPATH, CONTEST_DATE_XPATH) is not None and
                wait_for_element(
                    d, By.XPATH, CONTEST_DATE_XPATH).text != current_contest_text
            )
            return True
        except TimeoutException:
            print("Error: Contest number did not update after clicking 'next'.")
            return False
        except Exception as e:
            print(f"Error clicking next button or waiting for update: {e}")
            return False
    return False
