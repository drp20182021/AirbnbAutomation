import unittest
from telegram_bot import send_telegram_message
from config_utils import find_config_paths, load_configuration


class TestTelegram(unittest.TestCase):
    def test_send_telegram_message(self):
        config_paths = find_config_paths("config_test.json")
        self.assertGreater(len(config_paths), 0, "No mock configuration file found.")

        for config_path in config_paths:
            config = load_configuration(config_path)
            self.assertIsNotNone(
                config, f"Failed to load configuration from {config_path}"
            )
            if "telegram" in config:
                api_token = config["telegram"]["api_token"]
                chat_id = config["telegram"]["chat_id"]
                response = send_telegram_message(
                    "This is a test message from the mock test",
                    api_token,
                    chat_id,
                )
                self.assertEqual(
                    response["ok"], True, f"Failed to send message using {config_path}"
                )


if __name__ == "__main__":
    unittest.main()
