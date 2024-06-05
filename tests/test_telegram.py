import sys
import unittest
from pathlib import Path

# Add the src directory to the Python path
sys.path.append(str(Path(__file__).resolve().parents[1] / "src"))

from telegram_bot import send_telegram_message
from config_utils import find_config_path, load_configuration


class TestTelegramBot(unittest.TestCase):
    def test_send_telegram_message(self):
        config_path = find_config_path()
        self.assertIsNotNone(config_path, "Configuration file not found.")

        config = load_configuration(config_path)
        self.assertIsNotNone(config, f"Failed to load configuration from {config_path}")

        api_token = config["telegram"]["api_token"]
        chat_id = config["telegram"]["chat_id"]

        # Test sending a message
        response = send_telegram_message("Test message", api_token, chat_id)
        self.assertEqual(response["ok"], True, "Failed to send message.")


if __name__ == "__main__":
    unittest.main()
