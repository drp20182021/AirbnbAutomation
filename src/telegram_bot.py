import requests
from config_utils import find_config_paths, load_configuration


def send_telegram_message(text, api_token, chat_id):
    """
    Sends a message to a specified Telegram chat using the provided API token and chat ID.
    Args:
        text (str): The message content to be sent.
        api_token (str): Telegram bot API token.
        chat_id (str): Telegram chat ID.
    Returns:
        dict: The response from the Telegram API as a dictionary.
    """
    url = f"https://api.telegram.org/bot{api_token}/sendMessage"
    payload = {
        "chat_id": chat_id,
        "text": text,
        "parse_mode": "Markdown",
        "disable_web_page_preview": True,
    }
    response = requests.post(url, data=payload)
    return response.json()


if __name__ == "__main__":
    config_paths = find_config_paths()
    if not config_paths:
        print("Configuration file not found.")
        exit(1)

    for config_path in config_paths:
        config = load_configuration(config_path)
        if config and "telegram" in config:
            api_token = config["telegram"]["api_token"]
            chat_id = config["telegram"]["chat_id"]
            send_telegram_message(
                "Congratulations, the message to Telegram has been sent successfully",
                api_token,
                chat_id,
            )
            print(f"Message sent using {config_path}")
        else:
            print(f"Failed to load configuration from {config_path}.")
