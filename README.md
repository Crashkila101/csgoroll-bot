# CSGORoll Auto Bot
**CSGORoll Auto Bot** is a Python program that automates opening cases **csgoroll.com**, a gambling website where daily rewards are given to players after a certain amount of money has been wagered. The program uses the **Selenium WebDriver** library to simulate human interaction with the website.

The program requires the user to have a valid Steam account and to generate Steam login cookies, which are used to bypass the website's login process.

The program is designed to be run on Linux or Windows and requires the user to download the appropriate Chromium browser and driver for their system from the Chromium Browser Snapshots website.

## Environment Setup

1. Clone the repository:

```bash
git clone https://github.com/yourusername/CSGORollBot.git
cd CSGORollBot
```

2. Create a new conda environment using the environment.yaml file:
```bash
conda env create -f environment.yaml
conda activate csgo-roll-bot
```

3. Download Chromium binary and driver for your system from [here](https://commondatastorage.googleapis.com/chromium-browser-snapshots/index.html).

- Find the latest version in a file called `LAST_CHANGE`.
- Download the binary and the driver. Most people will either want to download from Linux_x64 or Win_x64 directories.
- The files you want to download will be packaged into a zip archive with the following naming scheme `chrome-*.zip` and `chromedriver_*.zip`. For example, for Linux it will be `Linux_x64/<version>/chrome-linux.zip` and `Linux_x64/<version>/chromedriver_linux64.zip`.
Extract the downloaded files and move them to the `./browser` directory in the project folder.

## Configuration Setup

Run `python cookie_getter.py` and log in to your Steam account. Once you are logged in, press Enter and specify the account's name. You can add as many accounts as you want.

## Running the Program

To run the program, use the following command:

```bash
python main.py [--debug] [--slow <seconds>] [--width <pixels>] [--height <pixels>] [--headless] [--browser_path <path>] [--driver_path <path>] [--interval <hours>]
```

## Arguments

**--debug** (optional) - Enters debugging mode (default: False)

**--slow <seconds>** (optional) - Pauses the application for the specified time after preforming an action in the browser, mainly used in development and testing (*default: 0*)

**--width <pixels>** (optional) - Specify the width of the browser window (*default: 960*)

**--height <pixels>** (optional) - Specify the height of the browser window (*default: 960*)

**--headless** (recommended) - Runs the application in headless mode, which means that the GUI will not be displayed, useful in a server environment (*deafault: False)

**--browser_path <path>** (optional) - Manually specify Chromium browser path (*default: dynamic*)

**--driver_path <path>** (optional) - Manually specify Chromium driver path (*default: dynamic*)

**--interval <hours>** (optional) - How many hours between each case opening loop (*default: 24*)

For example, to run the program in debugging mode with a specific browser and driver path, use:

```bash
python main.py --debug --browser_path "/path/to/chrome.exe" --driver_path "/path/to/chromedriver"
```