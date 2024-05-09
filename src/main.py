from datetime import datetime, timedelta
from config_loader import load_configuration, find_config_path
from airbnb_data import get_airbnb_reservations
from message_format import (
    format_basic_message,
    format_detailed_message,
    format_detailed_message_assign_mailboxes,
)
from telegram_bot import send_telegram_message


def main():
    """
    Main execution function that handles the flow of fetching Airbnb reservation data,
    formatting messages, and sending them through Telegram based on configurations.

    Args:
        None

    Returns:
        None
    """
    # Load the configuration file path
    config_path = find_config_path()
    if not config_path:
        print("Configuration file not found.")
        return

    # Load configuration settings
    config = load_configuration(config_path)
    if not config:
        print("Failed to load configuration.")
        return

    # Extract Telegram configuration details
    api_token = config["telegram"]["api_token"]
    chat_id = config["telegram"]["chat_id"]

    # Fetch reservations for the specified number of days from today
    days = 600
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
    main()
