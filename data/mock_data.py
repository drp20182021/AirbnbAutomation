import datetime
from ics import Calendar, Event
import random
import os
import logging

# Set up basic configuration for logging
logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
)


def generate_mock_ics(file_path, days_forward=30, num_events=10):
    """
    Generates a mock ICS file with random reservation and availability events.
    All events are set as all-day events.

    Args:
        file_path (str): The path where the .ics file will be saved.
        days_forward (int): Number of days forward from today for which to generate events.
        num_events (int): Number of events to generate.
    """
    today = datetime.datetime.now().date()
    cal = Calendar()

    for _ in range(num_events):
        start_date = today + datetime.timedelta(days=random.randint(0, days_forward))
        end_date = start_date + datetime.timedelta(days=random.randint(1, 4))
        event = Event()

        # Marking the event as all-day to ensure DATE format in DTSTART and DTEND
        event.begin = start_date
        event.end = end_date
        event.make_all_day()

        event.uid = f"{random.randint(100000000, 999999999)}@airbnb.com"

        # More likely to have reserved events than not available
        if random.choice([True] * 3 + [False]):
            event.name = "Reserved"
            event.description = (
                "Reservation details: https://www.airbnb.com/reservation/itinerary"
            )
        else:
            event.name = "Airbnb (Not available)"

        cal.events.add(event)

    # Try writing to file, handle potential IO errors
    try:
        with open(file_path, "w") as f:
            f.write(
                cal.serialize()
            )  # Using serialize method to ensure correct ICS formatting
    except IOError as e:
        logging.error(f"Failed to write to file {file_path}: {e}")


# Dictionary to map apartment names to file names
apartment_files = {
    "Apartment 1": "apartment_1.ics",
    "Apartment 2": "apartment_2.ics",
    "Apartment 3": "apartment_3.ics",
    "Apartment 4": "apartment_4.ics",
    "Apartment 5": "apartment_5.ics",
}

if __name__ == "__main__":
    directory = "data"  # Specify the directory to save the files
    try:
        os.makedirs(
            directory, exist_ok=True
        )  # Safely create the directory if it does not exist
    except Exception as e:
        logging.error(f"Failed to create directory {directory}: {e}")
        exit(1)

    # Generate ICS files for each apartment
    for apt_name, file_name in apartment_files.items():
        full_path = os.path.join(directory, file_name)
        generate_mock_ics(full_path, days_forward=30, num_events=random.randint(5, 15))
        logging.info(f"Generated mock data for {apt_name} in {full_path}")
