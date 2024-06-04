import sys
import unittest
from pathlib import Path

# Add the src directory to the Python path
sys.path.append(str(Path(__file__).resolve().parents[1] / "src"))

from airbnb_data import get_airbnb_reservations
from config_utils import find_config_paths, load_configuration
from message_format import (
    format_basic_message,
    format_detailed_message,
    format_detailed_message_assign_mailboxes,
)


class TestMessageFormat(unittest.TestCase):
    def test_message_format_with_mock_data(self):
        config_paths = find_config_paths("config_test.json")
        self.assertGreater(len(config_paths), 0, "No mock configuration file found.")

        for config_path in config_paths:
            config = load_configuration(config_path)
            self.assertIsNotNone(
                config, f"Failed to load configuration from {config_path}"
            )
            reservations = get_airbnb_reservations(config, 7)
            print(f"Messages for reservations from {config_path}:")
            print("Basic Message:")
            print(format_basic_message(reservations))
            print("Detailed Message:")
            print(format_detailed_message(reservations))
            print("Detailed Message with Mailboxes:")
            print(format_detailed_message_assign_mailboxes(reservations))


if __name__ == "__main__":
    unittest.main()
