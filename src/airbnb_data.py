import requests
from datetime import datetime, timedelta
from ics import Calendar
import json


def get_airbnb_reservations():
    """
    Fetches reservations from Airbnb URLs specified in the config.json file.

    Returns:
        dict: A dictionary containing check-ins and check-outs categorized by date.
    """
    # Load configuration
    with open("config.json", "r") as f:
        config = json.load(f)

    urls = config["airbnb_urls"]

    # Define date range for reservations to retrieve
    start_date = datetime.now().date()
    end_date = start_date + timedelta(days=2)

    reservations = {}

    for apt_number, url in urls.items():
        response = requests.get(url)
        calendar = Calendar(response.text)

        for event in calendar.events:
            checkin_date = event.begin.date()
            checkout_date = event.end.date()

            if checkin_date >= start_date and checkin_date <= end_date:
                checkin = {"apt_number": apt_number, "time": "15:00"}
                reservations.setdefault(
                    checkin_date, {"checkins": [], "checkouts": []}
                )["checkins"].append(checkin)

            if checkout_date >= start_date and checkout_date <= end_date:
                checkout = {"apt_number": apt_number, "time": "11:00"}
                reservations.setdefault(
                    checkout_date, {"checkins": [], "checkouts": []}
                )["checkouts"].append(checkout)

    return reservations
