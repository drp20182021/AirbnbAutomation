import sys
import unittest
from pathlib import Path

# Add the src directory to the Python path
sys.path.append(str(Path(__file__).resolve().parents[1] / "src"))

from airbnb_data import get_airbnb_reservations
from config_utils import find_config_path, load_configuration


class TestAirbnbData(unittest.TestCase):
    def test_get_airbnb_reservations(self):
        config_path = find_config_path()
        self.assertIsNotNone(config_path, "Configuration file not found.")

        config = load_configuration(config_path)
        self.assertIsNotNone(config, f"Failed to load configuration from {config_path}")

        # Replace real URLs with mock URLs for testing
        config["airbnb_urls"] = config["mock_airbnb_urls"]
        reservations = get_airbnb_reservations(config, 7)

        self.assertTrue(reservations, "No reservations found.")
        for date, res in reservations.items():
            self.assertIn("checkins", res)
            self.assertIn("checkouts", res)
            print(
                f"Date: {date}, Check-ins: {res['checkins']}, Check-outs: {res['checkouts']}"
            )


if __name__ == "__main__":
    unittest.main()
