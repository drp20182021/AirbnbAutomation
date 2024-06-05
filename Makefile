.PHONY: install reinstall run clean test test_telegram test_airbnb test_config test_message_format mock test_all_tests setup_config

# Variables
PYTHON = python
PIP = pip
SRC_DIR = src
TEST_DIR = tests
DATA_DIR = data

# Install the project's dependencies
install:
	@$(PIP) install -r requirements.txt

# Uninstall the package and reinstall it in editable mode
reinstall:
	@$(PIP) uninstall -y airbnb_telegram_bot || :
	@$(PIP) install -e .

# Run the main script with a specified number of days (default: 600)
run:
	@$(PYTHON) $(SRC_DIR)/main.py config.json 600

# Run the main script with mock data and a specified number of days (default: 7)
run_mock:
	@$(PYTHON) $(SRC_DIR)/main.py config.json 7 --mock

# Clean up Python's cache files and other artifacts
clean:
	@find . -type d -name "__pycache__" -exec rm -rf {} +
	@find . -name "*.pyc" -delete
	@find . -name "*.pyo" -delete

# Set up the configuration file
setup_config:
	@$(PYTHON) setup_config.py

# Test targets for real data
test: test_telegram test_airbnb test_config test_message_format

test_telegram:
	@$(PYTHON) $(SRC_DIR)/telegram_bot.py

test_airbnb:
	@$(PYTHON) $(SRC_DIR)/airbnb_data.py

test_config:
	@$(PYTHON) $(SRC_DIR)/config_utils.py

test_message_format:
	@$(PYTHON) $(SRC_DIR)/message_format.py

# Create mock files
mock:
	@$(PYTHON) $(DATA_DIR)/mock_data.py

# Test targets for mock data
test_mock_airbnb:
	@$(PYTHON) -m unittest $(TEST_DIR)/test_airbnb.py

test_mock_message_format:
	@$(PYTHON) -m unittest $(TEST_DIR)/test_message_format.py

test_mock_telegram:
	@$(PYTHON) -m unittest $(TEST_DIR)/test_telegram.py

test_mock_config:
	@$(PYTHON) -m unittest $(TEST_DIR)/test_config.py

# Run all tests
test_all_tests: test test_mock_airbnb test_mock_message_format test_mock_telegram test_mock_config
