
import time
import datetime
import requests

MY_LAT = 29.3956
MY_LON = 71.6833

API_URL = "https://iss-api.polluxlabs.io/iss-pass"


def is_iss_overhead():
    parameters = {
        "lat": MY_LAT,
        "lon": MY_LON,
        "n": 5
    }

    response = requests.get(
        API_URL,
        params=parameters,
        timeout=15
    )
    response.raise_for_status()

    data = response.json()
    passes = data.get("passes", [])

    if not passes:
        print("No upcoming ISS passes found.")
        return None

    next_time = passes[0]["rise"]["time"]

    pass_time = datetime.datetime.fromisoformat(
        next_time.replace("Z", "+00:00")
    ).astimezone()

    print(f"Next ISS pass at: {pass_time}")
    return pass_time


def notifier():
    while True:
        try:
            next_pass = is_iss_overhead()

            if next_pass is not None:
                now = datetime.datetime.now().astimezone()

                seconds_until_pass = (
                    next_pass - now
                ).total_seconds()

                if 0 <= seconds_until_pass <= 600:
                    print("Look up! ISS pass is approaching.")
                else:
                    print("Waiting for next ISS pass.")

        except (requests.RequestException, ValueError, KeyError) as error:
            print(f"Could not check ISS pass: {error}")

        time.sleep(60)


if __name__ == "__main__":
    notifier()
