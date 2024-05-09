import json
import logging
from pathlib import Path
from datetime import date, datetime


def find_config_path():
    """
    Searches for the 'config.json' file starting from the parent directory and its subdirectories.
    If not found, it checks the parent parent directory and its subdirectories.
    If not found, it checks the current working directory and the user's home directory.
    """
    # Start by checking the parent directory and its subdirectories
    parent_directory = Path.cwd().parent
    for path in parent_directory.rglob("config.json"):
        if path.exists():
            return path

    # Continue by checking the parent parent directory and its subdirectories
    parent_parent_directory = Path.cwd().parent.parent
    for path in parent_parent_directory.rglob("config.json"):
        if path.exists():
            return path

    # Define additional paths to check if not found in parent directory
    additional_paths = [
        Path.cwd() / "config.json",  # Current working directory
        Path.home() / "config.json",  # User's home directory
    ]

    # Check additional paths
    for path in additional_paths:
        if path.exists():
            return path

    # If no file is found, return None
    return None


def load_configuration(path):
    """
    Load configuration from a specified JSON file.

    Args:
        path (str): The file path to the JSON configuration file.

    Returns:
        dict: A dictionary containing the loaded configuration, or None if an error occurs.
    """
    try:
        with open(path, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        logging.error(f"File {path} not found.")
        return None
    except json.JSONDecodeError:
        logging.error(f"Error decoding JSON in file {path}.")
        return None


def json_serial(obj):
    """
    JSON serializer for objects not serializable by default json code. Handles conversion of date and datetime objects to string.

    Args:
        obj (Any): The object to be serialized. Expected to be primarily date or datetime objects.

    Returns:
        str: A string representation of the input object if it is a date or datetime.
        Raises TypeError if the input object is not of a serializable type recognized by this function.
    """
    if isinstance(obj, (datetime, date)):
        return obj.isoformat()
    raise TypeError(f"Type {type(obj)} not serializable")


def print_pretty_json(data):
    """
    Prints the given data in a pretty formatted JSON style, handling non-serializable objects.
    Modifies dictionary keys to ensure they are serializable to JSON format by converting date and datetime objects to strings.

    Args:
        data (dict | Any): The data to print, typically a dictionary. If data is a dictionary, its keys are processed to ensure they are strings.

    Returns:
        None: This function does not return anything; it directly prints to the console. Logs an error if serialization fails.
    """
    if isinstance(data, dict):
        # Ensure all dict keys are strings, convert if necessary
        new_data = {
            json_serial(k) if not isinstance(k, str) else k: v for k, v in data.items()
        }
    else:
        new_data = data

    try:
        print(json.dumps(new_data, indent=4, sort_keys=True, default=json_serial))
    except TypeError as e:
        logging.error(f"Error serializing data: {e}")


if __name__ == "__main__":
    config_path = find_config_path()
    if config_path:
        # Print the path of the config file
        print(f"Configuration file found at: {config_path}")
        config = load_configuration(config_path)
        if config is not None:
            # Print the content of the config file
            print("Configuration loaded successfully:")
            print_pretty_json(config)
        else:
            print("Failed to load configuration.")
    else:
        print("Configuration file not found.")
