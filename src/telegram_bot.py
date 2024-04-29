import requests
import json


def send_telegram_message(text):
    """
    Sends a message to a specified Telegram chat using the API token from config.json.

    Args:
        text (str): The message content to be sent.
    """
    # Load configuration
    with open("config.json", "r") as f:
        config = json.load(f)

    api_token = config["telegram"]["api_token"]
    chat_id = config["telegram"]["chat_id"]

    url = f"https://api.telegram.org/bot{api_token}/sendMessage"
    payload = {
        "chat_id": chat_id,
        "text": text,
        "parse_mode": "Markdown",
        "disable_web_page_preview": True,
    }
    response = requests.post(url, data=payload)
    return response.json()
