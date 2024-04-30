.PHONY: install reinstall run clean

# Install the project's dependencies
install:
	@pip install -r requirements.txt

# Uninstall the package and reinstall it in editable mode
reinstall:
	@pip uninstall -y airbnb_telegram_bot || :
	@pip install -e .

# Run the main script
run:
	@python src/main.py

# Clean up Python's cache files
clean:
	find . -type d -name "__pycache__" -exec rm -r {} + || :
	find . -name "*.pyc" -delete || :
	find . -name "*.pyo" -delete || :
