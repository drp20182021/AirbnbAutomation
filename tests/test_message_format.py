import sys
import unittest
from pathlib import Path

# Add the src directory to the Python path
sys.path.append(str(Path(__file__).resolve().parents[1] / "src"))

from airbnb_data import get_airbnb_reservations
from config_utils import find_config_path, load_configuration
from message_format import (
    format_basic_message,
    format_detailed_message,
    format_detailed_message_assign_mailboxes,
)


class TestMessageFormat(unittest.TestCase):
    def test_message_format_with_mock_data(self):
        config_path = find_config_path()
        self.assertIsNotNone(config_path, "Configuration file not found.")

        config = load_configuration(config_path)
        self.assertIsNotNone(config, f"Failed to load configuration from {config_path}")

        # Replace real URLs with mock URLs for testing
        config["airbnb_urls"] = config["mock_airbnb_urls"]
        reservations = get_airbnb_reservations(config, 7)

        mailboxes = config.get("mock_mailboxes", [])
        special_mailboxes = config.get("mock_special_mailboxes", {})

        print("Basic Message:")
        print(format_basic_message(reservations))
        print("Detailed Message:")
        print(format_detailed_message(reservations))
        print("Detailed Message with Mailboxes:")
        print(
            format_detailed_message_assign_mailboxes(
                reservations, mailboxes, special_mailboxes
            )
        )


if __name__ == "__main__":
    unittest.main()
