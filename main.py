import glob
from src.vote import vote_on_server
import json
import pickle
from datetime import datetime
from src.logs import log
import time
from src.args import args


def main():
    # Cookie search
    steam_cookies = "./config/steam_cookies"
    cookies_files = glob.glob(steam_cookies + "/*.pkl")
    print(f"Found {len(cookies_files)} cookie files")

    roll_url = "https://www.csgoroll.com"
    if len(cookies_files) == 0:
        print("No cookies found, exiting")
        return

    # Initial vote
    print("Beginning initial case opening")
    case_loop(roll_url, cookies_files)

    last_vote = datetime.now()
    while True:
        # Get the current time
        time_since = datetime.now() - last_vote

        # Check if it's been 5 hours since the last execution
        if time_since.seconds > 60*60*args.interval:
            last_vote = datetime.now()
            print(f"Beginning case opening at {datetime.now().strftime('%H:%M:%S')}")
            case_loop(roll_url, cookies_files)
        else:
            # Print the time left in hours
            print(
                f"Next opening attempt in {round((60*60*args.interval - time_since.seconds)/60/60, 2)} hours")

        # Wait for an hour before checking again
        time.sleep(60*60)


def case_loop(roll_url, cookies_files):
    # Results dict
    results = {
        "success": [],
        "fail": []
    }

    log(f"Started opening at {datetime.now().strftime('%H:%M:%S')}")

    # Vote loop

    log(f"Beginning roll loop for {roll_url}")

    for cookies_file in cookies_files:
        log(f"Beginning opening using {cookies_file}")
        cookies = pickle.load(open(cookies_file, "rb"))
        result = vote_on_server(roll_url, cookies)

        if result:
            results["success"].append((cookies_file, roll_url))
        else:
            results["fail"].append((cookies_file, roll_url))
        log("")

    # # Results
    # log(f"Finished voting at {datetime.now().strftime('%H:%M:%S')}")
    # print(f"Made {len(results['success'])} successful votes")
    # print(f"Failed {len(results['fail'])} votes")

    # # Log results
    # log(f"Made {len(results['success'])} successful votes")
    # for success in results["success"]:
    #     log(f"{success[0]}\t{success[1]}")

    # log(f"Failed {len(results['fail'])} votes")
    # for fail in results["fail"]:
    #     log(f"{fail[0]}\t{fail[1]}")

    # log("-"*50)


if __name__ == "__main__":
    main()
