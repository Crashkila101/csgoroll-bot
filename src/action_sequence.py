from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from selenium.webdriver.common.by import By

from src.debug import slow
from src. logs import debug_log, log
import time


def action_sequence(driver, url):

    # Timeout
    wait = WebDriverWait(driver, 10)

    # Load page
    try:
        driver.get(url)
    except:
        debug_log(
            driver, "Failed to load page!\nCheck if the URL is correct: {url}")
        driver.quit()
        return False

    # Wait for document to load
    try:
        wait.until(EC.presence_of_element_located((By.XPATH, "//body")))
        slow()
    except TimeoutException:
        debug_log(driver, "Timed out waiting for page to load")
        driver.quit()
        return False

    # Wait for the login button to be clickable and click
    try:
        login_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[data-test='auth-login-btn']")))
        slow()
        login_button.click()
        slow()
    except TimeoutException:
        debug_log(driver, "Timed out waiting for button to be clickable")
        driver.quit()
        return False

    # Steam login
    try:
        wait.until(EC.presence_of_element_located((By.XPATH, "//body")))
        slow()
    except TimeoutException:
        debug_log(driver, "Timed out waiting for Steam to load")
        driver.quit()
        return False
    
    # Steam Form
    try:
        steam_signin_button = wait.until(EC.element_to_be_clickable(
            (By.ID, "imageLogin")))
        slow()
        steam_signin_button.click()
        slow()
    except TimeoutException:
        debug_log(driver, "Timed out; Steam sign in button not found")
        driver.quit()
        return False


    # Wait for rewards link to be clickable and click
    try:
        rewards_link = wait.until(EC.element_to_be_clickable(
            (By.XPATH, "//a[.//span[text()='REWARDS']]")))
        slow()
        rewards_link.click()
        slow()
    except TimeoutException:
        debug_log(driver, "Timed out waiting for button to be clickable")
        driver.quit()
        return False
    
    while wait.until(EC.visibility_of_element_located((By.XPATH, "//button[contains(span/span/text(), 'OPEN CASE')]"))):
    # Link to open case modal box
        try:
            open_case_modal = wait.until(EC.element_to_be_clickable(
                    (By.XPATH, "//button[contains(span/span/text(), 'OPEN CASE')]")))
            slow()
            open_case_modal.click()
            slow()
        except TimeoutException:
            debug_log(driver, "Timed out waiting for button to be clickable")
            driver.quit()
            return False

        # Open case and close modal
        try:
            open_case = wait.until(EC.element_to_be_clickable(
                    (By.XPATH, "//button[contains(span/span/span/text(), 'Open 1 time')]")))
            slow()
            open_case.click()
            slow()
            time.sleep(0.1)
            close_modal = wait.until(
                EC.element_to_be_clickable((By.CLASS_NAME, "mat-focus-indicator.close.mat-icon-button.mat-button-base")))
            slow()
            close_modal.click()
        except TimeoutException:
            debug_log(driver, "Timed out waiting for button to be clickable")
            driver.quit()
            return False    
    return None