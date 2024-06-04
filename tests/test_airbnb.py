import sys
import unittest
from pathlib import Path

# Asegurarse de que el directorio 'src' esté en el PYTHONPATH
sys.path.append(str(Path(__file__).resolve().parent.parent / "src"))


from airbnb_data import get_airbnb_reservations
from config_utils import find_config_paths, load_configuration, print_pretty_json


class TestAirbnbReservations(unittest.TestCase):
    def test_airbnb_reservations_with_mock_data(self):
        config_paths = find_config_paths("config_test.json")
        for config_path in config_paths:
            config = load_configuration(config_path)
            if config:
                reservations = get_airbnb_reservations(
                    config, 30
                )  # 30 días hacia adelante
                self.assertIsInstance(reservations, dict)
                print(f"Reservations from {config_path}:")
                print_pretty_json(reservations)
            else:
                self.fail(f"Failed to load configuration from {config_path}")


if __name__ == "__main__":
    unittest.main()
