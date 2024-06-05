import requests
from datetime import datetime, timedelta
from ics import Calendar
import logging
from config_utils import find_config_path, load_configuration, print_pretty_json
import os

# Configure logging
logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
)


def fetch_calendar_data(url_or_path):
    """
    Fetch calendar data from a specified URL or file path.

    Args:
        url_or_path (str): The URL or file path from which to fetch calendar data.

    Returns:
        str: The calendar data as a string if successful, or None if an error occurs.
    """
    try:
        if os.path.isfile(url_or_path):
            with open(url_or_path, "r") as file:
                return file.read()
        else:
            response = requests.get(url_or_path)
            response.raise_for_status()  # Throw an error for 4xx/5xx responses
            return response.text
    except (requests.RequestException, FileNotFoundError) as e:
        logging.error(f"Error getting data from {url_or_path}: {e}")
        return None


def parse_calendar_events(calendar_data):
    """
    Parse calendar events from ICS format data.

    Args:
        calendar_data (str): Calendar data in ICS format to parse.

    Returns:
        list: A list of Event objects parsed from the calendar data, or None if parsing fails.
    """
    calendar = Calendar(calendar_data)
    return calendar.events if calendar else None


def get_airbnb_reservations(config, days):
    """
    Fetches reservations from Airbnb URLs specified in the configuration for the next given days.

    Args:
        config (dict): Configuration dictionary containing Airbnb URLs.
        days (int): Number of days from today to fetch reservations.

    Returns:
        dict: A dictionary containing check-ins and check-outs categorized by date.
    """
    if not config:
        logging.error("Configuration is missing.")
        return {}

    start_date = datetime.now().date()
    end_date = start_date + timedelta(days=days)
    urls = config.get("airbnb_urls", {})
    reservations = {}

    for apt_number, url_or_path in urls.items():
        calendar_data = fetch_calendar_data(url_or_path)
        if calendar_data:
            events = parse_calendar_events(calendar_data)
            for event in events:
                checkin_date = event.begin.date()
                checkout_date = event.end.date()

                if start_date <= checkin_date <= end_date:
                    reservations.setdefault(
                        checkin_date, {"checkins": [], "checkouts": []}
                    )["checkins"].append({"apt_number": apt_number})

                if start_date <= checkout_date <= end_date:
                    reservations.setdefault(
                        checkout_date, {"checkins": [], "checkouts": []}
                    )["checkouts"].append({"apt_number": apt_number})

    return reservations


if __name__ == "__main__":
    config_path = find_config_path()
    if not config_path:
        print("Configuration file not found.")
        exit(1)

    config = load_configuration(config_path)
    if config:
        reservations = get_airbnb_reservations(config, 600)  # Fetch for next 600 days
        print(f"Reservations from {config_path}:")
        print_pretty_json(reservations)
    else:
        print(f"Failed to load configuration from {config_path}.")
