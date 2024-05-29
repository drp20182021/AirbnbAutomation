from datetime import datetime, timedelta
from config_utils import load_configuration, find_config_paths
from airbnb_data import get_airbnb_reservations
from message_format import (
    format_basic_message,
    format_detailed_message,
    format_detailed_message_assign_mailboxes,
)
from telegram_bot import send_telegram_message
import sys


def main(config_filename=None, days=7):
    """
    Main function to run the application with a specified or default configuration file.

    Args:
        config_filename (str, optional): The configuration file to use. If None, defaults to 'config.json'.
        days (int, optional): The number of days to fetch reservations for. Defaults to 600.
    """
    config_paths = find_config_paths(
        config_filename if config_filename else "config.json"
    )

    if config_filename:
        # Filter paths to find the one that matches the provided filename
        config_path = next((p for p in config_paths if p.name == config_filename), None)
    else:
        # Use the first available config file as default
        config_path = config_paths[0] if config_paths else None

    if not config_path:
        print("Configuration file not found.")
        return

    config = load_configuration(config_path)
    if not config:
        print("Failed to load configuration.")
        return

    # Extract Telegram configuration details
    api_token = config["telegram"]["api_token"]
    chat_id = config["telegram"]["chat_id"]

    # Fetch reservations for the specified number of days from today
    reservations = get_airbnb_reservations(config, days)

    # Format messages to summarize the reservations
    basic_message = format_basic_message(reservations)
    detailed_message = format_detailed_message(reservations)
    detailed_message_with_mailboxes = format_detailed_message_assign_mailboxes(
        reservations
    )

    # Send the formatted messages to the Telegram bot; only one should be active to avoid spam
    # send_telegram_message(basic_message, api_token, chat_id)
    # send_telegram_message(detailed_message, api_token, chat_id)
    send_telegram_message(detailed_message_with_mailboxes, api_token, chat_id)

    print("Messages sent successfully!")


if __name__ == "__main__":
    # Allow passing the configuration filename and number of days as command-line arguments
    config_filename = sys.argv[1] if len(sys.argv) > 1 else None
    days = int(sys.argv[2]) if len(sys.argv) > 2 else 600
    main(config_filename, days)
