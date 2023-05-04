# Selenium
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.firefox.options import Options
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

# Other
from src.args import args
from src.logs import log


def get_driver(options=None):

    # Set options and start driver
    # if options is not None then
    if not options:
        options = Options()
        if args.headless:
            options.add_argument("--headless")
        options.add_argument("--disable-gpu")
        options.add_argument("--disable-infobars")
        options.add_argument("--disable-notifications")
        options.add_argument("--disable-extensions")
        options.add_argument("--disable-dev-shm-usage")
        options.add_argument(f"--window-size={args.width},{args.height}")
        if args.incognito:
            options.add_argument("--incognito")
        options.add_argument("--disable-cloud-management")
        if args.debug:
            options.add_argument("--log-level=0")
        else:
            options.add_argument("--log-level=3")
            options.add_argument("--silent")

        
    # Set up Firefox WebDriver using webdriver-manager  
    driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()), options=options)

    # Test driver
    try:
        driver.get("https://www.google.com/")
        wait = WebDriverWait(driver, 10)
        wait.until(EC.title_is("Google"))
        log("Driver test successful")
    except:
        print("Failed to test the driver!\nCheck if the browser and driver paths are correct")
        driver.quit()
        exit()

    # Return driver
    return driver