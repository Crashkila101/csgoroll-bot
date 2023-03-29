import argparse

# Argument parser
parser = argparse.ArgumentParser()
parser.add_argument("--debug", help="Enters debugging mode (default: false)", action="store_true")
parser.add_argument("--browser_path", help="Manualy specify Chromium browser path (default: dynamic)", type=str)
parser.add_argument("--driver_path", help="Manualy specify Chromium driver path (default: dynamic)", type=str)
parser.add_argument("--interval", help="How many hours between each voting loop (deafult: 5)", type=int, default=5)


args = parser.parse_args()
