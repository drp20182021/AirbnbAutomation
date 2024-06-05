import json
import logging
from pathlib import Path
from datetime import date, datetime


def find_config_path(config_filename="config.json"):
    """
    Searches for the configuration file in the current directory, parent directories (up to two levels), and the user's home directory.

    Args:
        config_filename (str): The name of the configuration file to search for, default is 'config.json'.

    Returns:
        Path: The path to the configuration file if found, otherwise None.
    """
    # Define directories to search
    directories_to_search = [
        Path.cwd(),  # Current directory
        Path.cwd().parent,  # Parent directory
        Path.cwd().parent.parent,  # Parent's parent directory
        Path.home(),  # User's home directory
    ]

    for directory in directories_to_search:
        potential_path = directory / config_filename
        if potential_path.exists():
            return potential_path

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
        print(f"Configuration file found at: {config_path}")
        config = load_configuration(config_path)
        if config is not None:
            print("Configuration loaded successfully:")
            print_pretty_json(config)
        else:
            print(f"Failed to load configuration from {config_path}.")
    else:
        print("Configuration file not found.")
