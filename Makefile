.PHONY: install reinstall run clean test test_telegram test_airbnb test_config test_message_format

# Variables
PYTHON = python
PIP = pip
SRC_DIR = src
DATA_DIR = data

# Install the project's dependencies
install:
	@$(PIP) install -r requirements.txt

# Uninstall the package and reinstall it in editable mode
reinstall:
	@$(PIP) uninstall -y airbnb_telegram_bot || :
	@$(PIP) install -e .

# Run the main script
run:
	@$(PYTHON) $(SRC_DIR)/main.py

# Clean up Python's cache files and other artifacts
clean:
	@find . -type d -name "__pycache__" -exec rm -rf {} +
	@find . -name "*.pyc" -delete
	@find . -name "*.pyo" -delete

# Test targets
test: test_telegram test_airbnb test_config test_message_format

test_telegram:
	@$(PYTHON) $(SRC_DIR)/telegram_bot.py

test_airbnb:
	@$(PYTHON) $(SRC_DIR)/airbnb_data.py

test_config:
	@$(PYTHON) $(SRC_DIR)/config_loader.py

test_message_format:
	@$(PYTHON) $(SRC_DIR)/message_format.py

# Creat mock files
mock:
	@$(PYTHON) $(DATA_DIR)/mock_data.py
