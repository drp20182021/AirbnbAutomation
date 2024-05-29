import unittest
import sys
from pathlib import Path

# Add the src directory to the Python path
sys.path.append(str(Path(__file__).resolve().parents[1] / "src"))

from config_utils import find_config_paths, load_configuration, print_pretty_json


class TestConfigLoader(unittest.TestCase):
    def test_load_mock_config(self):
        config_paths = find_config_paths("config_test.json")
        for config_path in config_paths:
            config = load_configuration(config_path)
            if config:
                print(f"Configuration loaded from {config_path}:")
                print_pretty_json(config)
                self.assertIsInstance(config, dict)
            else:
                self.fail(f"Failed to load configuration from {config_path}")


if __name__ == "__main__":
    unittest.main()
