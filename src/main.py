from datetime import datetime, timedelta
from config_utils import load_configuration, find_config_path
from airbnb_data import get_airbnb_reservations
from message_format import (
    format_basic_message,
    format_detailed_message,
    format_detailed_message_assign_mailboxes,
)
from telegram_bot import send_telegram_message
import sys


def main(config_filename=None, days=7, use_mock=False):
    """
    Main function to run the application with a specified or default configuration file.

    Args:
        config_filename (str, optional): The configuration file to use. If None, defaults to 'config.json'.
        days (int, optional): The number of days to fetch reservations for. Defaults to 600.
        use_mock (bool, optional): Whether to use mock data or not. Defaults to False.
    """
    config_path = find_config_path(
        config_filename if config_filename else "config.json"
    )

    if not config_path:
        print("Configuration file not found.")
        return

    config = load_configuration(config_path)
    if not config:
        print("Failed to load configuration.")
        return

    if use_mock:
        print("Using mock data")
        config["airbnb_urls"] = config["mock_airbnb_urls"]

    # Extract Telegram configuration details
    api_token = config["telegram"]["api_token"]
    chat_id = config["telegram"]["chat_id"]

    # Fetch reservations for the specified number of days from today
    reservations = get_airbnb_reservations(config, days)

    # Format messages to summarize the reservations
    basic_message = format_basic_message(reservations)
    detailed_message = format_detailed_message(reservations)
    detailed_message_with_mailboxes = format_detailed_message_assign_mailboxes(
        reservations, config["mailboxes"], config["special_mailboxes"]
    )

    if not reservations:
        print("No reservations found.")
    else:
        # Send the formatted messages to the Telegram bot; only one should be active to avoid spam
        # send_telegram_message(basic_message, api_token, chat_id)
        # send_telegram_message(detailed_message, api_token, chat_id)
        send_telegram_message(detailed_message_with_mailboxes, api_token, chat_id)
        print("Messages sent successfully!")


if __name__ == "__main__":
    # Allow passing the configuration filename and number of days as command-line arguments
    config_filename = sys.argv[1] if len(sys.argv) > 1 else None
    days = int(sys.argv[2]) if len(sys.argv) > 2 else 600
    use_mock = "--mock" in sys.argv  # Check if '--mock' is in the arguments
    main(config_filename, days, use_mock)
