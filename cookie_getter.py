# Selenium
from selenium.webdriver.firefox.options import Options
from src.driver_setup import get_driver

# Other
import pickle
import os



def main():
    options = Options()
    options.add_argument("--disable-gpu")
    options.add_argument("--disable-infobars")
    options.add_argument("--disable-notifications")
    options.add_argument("--window-size=960,960")
    options.add_argument("--incognito")
    options.add_argument("--disable-cloud-management")

    driver = get_driver(options)

    # Load page
    driver.get("https://steamcommunity.com/openid/login?openid.mode=checkid_setup&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0&openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.return_to=https%3A%2F%2Fapi.entertoroll.com%2Fauth%2Fsteam%2Freturn&openid.realm=https%3A%2F%2Fapi.entertoroll.com")
    
    # Login stage
    input("Login and press enter to continue...")
    account_name = ""
    while account_name == "":
        account_name = input("Enter account name: ")

    # Create directory if it doesn't exist
    if not os.path.exists("./config/steam_cookies/"):
        os.makedirs("./config/steam_cookies/")

    # Export cookies
    pickle.dump(driver.get_cookies(), open(
        f"./config/steam_cookies/{account_name}.pkl", "wb"))
    driver.quit()

    print(f"Cookies exported as {account_name}.pkl")

if __name__ == "__main__":
    main()
