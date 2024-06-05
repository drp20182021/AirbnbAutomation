import json


def create_config():
    config = {}

    # Get Telegram API token and chat ID
    config["telegram"] = {}
    config["telegram"]["api_token"] = input("Enter your Telegram API token: ")
    config["telegram"]["chat_id"] = input("Enter your Telegram chat ID: ")

    # Get Airbnb URLs
    config["airbnb_urls"] = {}
    while True:
        apt_number = input("Enter the apartment number (or 'done' to finish): ")
        if apt_number.lower() == "done":
            break
        ical_url = input(f"Enter the iCal URL for apartment {apt_number}: ")
        config["airbnb_urls"][apt_number] = ical_url

    # Get mailboxes
    config["mailboxes"] = []
    while True:
        mailbox = input("Enter a mailbox (or 'done' to finish): ")
        if mailbox.lower() == "done":
            break
        config["mailboxes"].append(mailbox)

    # Get special mailboxes
    config["special_mailboxes"] = {}
    while True:
        apt_number = input(
            "Enter the apartment number for special mailbox (or 'done' to finish): "
        )
        if apt_number.lower() == "done":
            break
        mailbox = input(f"Enter the special mailbox for apartment {apt_number}: ")
        config["special_mailboxes"][apt_number] = mailbox

    # Add mock data
    config["mock_airbnb_urls"] = {
        "1": "data/apartment_1.ics",
        "2": "data/apartment_2.ics",
        "3": "data/apartment_3.ics",
        "4": "data/apartment_4.ics",
        "5": "data/apartment_5.ics",
    }
    config["mock_mailboxes"] = ["1", "2", "3"]
    config["mock_special_mailboxes"] = {"1": "3", "2": "1"}

    # Save to config.json
    with open("config.json", "w") as f:
        json.dump(config, f, indent=4)
    print("Configuration saved to config.json")


if __name__ == "__main__":
    create_config()
