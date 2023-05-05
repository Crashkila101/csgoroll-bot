from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from selenium.webdriver.common.by import By

from src.debug import slow
from src. logs import debug_log, log


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

    # Wait for the button to be clickable and click
    try:
        login_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[data-test='auth-login-btn']")))
        slow()
        login_button.click()
        slow()
    except TimeoutException:
        debug_log(driver, "Timed out waiting for button to be clickable")
        driver.quit()
        return False

    # Steam Form
    try:
        steam_form = wait.until(EC.presence_of_element_located(
            (By.XPATH, "//form[(@name='steam_form')]")))
        form_checkbox = steam_form.find_element(
            By.XPATH, ".//input[(@class='form-check-input')]")
        slow()
        form_checkbox.click()
        slow()
        steam_form.submit()
        slow()
    except TimeoutException:
        debug_log(driver, "Timed out waiting for/filling in Steam form")
        driver.quit()
        return False
    

    # Wait for steam to load
    try:
        wait.until(EC.presence_of_element_located((By.XPATH, "//body")))
        slow()
    except TimeoutException:
        debug_log(driver, "Timed out waiting for Steam to load")
        driver.quit()
        return False

    # Reload page
    driver.refresh()

    # Steam login
    try:
        # Wait for steam login form to load
        login_form = wait.until(EC.presence_of_element_located(
            (By.XPATH, "//form[(@name='loginForm')]")))
        # Get the logged in user's name
        user_info = login_form.find_element(
            By.XPATH, ".//div[(@class='OpenID_loggedInAccount')]")
        debug_log(driver, f"Logged in as {user_info.text} ")
        slow()
        login_form.submit()
        slow()
    except TimeoutException:
        debug_log(driver, "Timed out waiting for steam login form to load")
        driver.quit()
        return False
    except NoSuchElementException:
        debug_log(
            driver, "Failed to find logged in user's name, is the cookie correct?")
        driver.quit()

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
    
    return None