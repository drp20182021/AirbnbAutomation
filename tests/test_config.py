import sys
import unittest
from pathlib import Path

# Add the src directory to the Python path
sys.path.append(str(Path(__file__).resolve().parents[1] / "src"))

from config_utils import find_config_path, load_configuration, print_pretty_json


class TestConfigUtils(unittest.TestCase):
    def test_load_configuration(self):
        config_path = find_config_path()
        self.assertIsNotNone(config_path, "Configuration file not found.")

        config = load_configuration(config_path)
        self.assertIsNotNone(config, f"Failed to load configuration from {config_path}")

        # Check that the required keys are present in the config
        self.assertIn("telegram", config)
        self.assertIn("airbnb_urls", config)
        self.assertIn("mock_airbnb_urls", config)
        self.assertIn("mock_mailboxes", config)
        self.assertIn("mock_special_mailboxes", config)

    def test_print_pretty_json(self):
        config_path = find_config_path()
        self.assertIsNotNone(config_path, "Configuration file not found.")

        config = load_configuration(config_path)
        self.assertIsNotNone(config, f"Failed to load configuration from {config_path}")

        # This test just ensures that the function runs without error
        try:
            print_pretty_json(config)
        except Exception as e:
            self.fail(f"print_pretty_json raised an exception: {e}")


if __name__ == "__main__":
    unittest.main()
