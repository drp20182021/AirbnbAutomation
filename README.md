# 🏠 Airbnb House Renting Notification Bot 🤖

Welcome to the Airbnb House Renting Notification Bot! This project automates the process of notifying users about their Airbnb property reservations via Telegram. It sends daily updates on check-ins and check-outs for the next few days, including information on which mailbox to use for key storage. 🌟

## 🚀 Getting Started

### Prerequisites

1. **Python 3.10+**: Ensure you have Python installed. You can download it from [python.org](https://www.python.org/downloads/).
2. **Virtual Environment**: It is recommended to use a virtual environment to manage dependencies. You can learn how to create one [here](https://docs.python.org/3/tutorial/venv.html).

### Installation

1. **Clone the repository**:
    ```sh
    git clone https://github.com/drp20182021/AirbnbAutomation.git
    cd AirbnbAutomation
    ```

2. **Create and activate a virtual environment**:
    ```sh
    python -m venv telegramenv
    source telegramenv/bin/activate  # On Windows use `telegramenv\Scripts\activate`
    ```

3. **Install the dependencies**:
    ```sh
    make install
    ```

### Configuration

#### Telegram Bot Setup

1. **Create a new Telegram bot** by talking to the BotFather and receive the bot HTTP API token. Follow these guides:
    - [How to create a bot](https://core.telegram.org/bots#how-do-i-create-a-bot)
    - [YouTube Guide](https://www.youtube.com/watch?v=UQrcOj63S2o)

#### Airbnb ICS URLs

To obtain your Airbnb calendar URLs, follow the guide [here](https://www.airbnb.com/help/article/99/how-do-i-sync-my-airbnb-calendar-with-another-calendar).

#### Set Up Configuration Files

1. **Create `config.json`**:
    Replace the placeholders with your actual Airbnb iCal URLs and Telegram bot token and chat ID.
    ```sh
    echo '{
      "telegram": {
        "api_token": "YOUR_TELEGRAM_API_TOKEN",
        "chat_id": "YOUR_CHAT_ID"
      },
      "airbnb_urls": {
        "1": "https://www.airbnb.com/calendar/ical/YOUR_ICAL_URL_1.ics",
        "2": "https://www.airbnb.com/calendar/ical/YOUR_ICAL_URL_2.ics",
        "3": "https://www.airbnb.com/calendar/ical/YOUR_ICAL_URL_3.ics",
        "4": "https://www.airbnb.com/calendar/ical/YOUR_ICAL_URL_4.ics",
        "5": "https://www.airbnb.com/calendar/ical/YOUR_ICAL_URL_5.ics",
        "6": "https://www.airbnb.com/calendar/ical/YOUR_ICAL_URL_6.ics",
        "7": "https://www.airbnb.com/calendar/ical/YOUR_ICAL_URL_7.ics"
      }
    }' > config.json
    ```

2. **Create `config_test.json`** for testing with mock data. You need to generate mock data by running `make mock`:
    ```sh
    make mock
    ```

### Usage

1. **Run the main script with real data**:
    ```sh
    python src/main.py config.json 7  # 7 is the number of days to fetch reservations for
    ```

2. **Run the main script with mock data**:
    ```sh
    python src/main.py tests/config_test.json 7  # 7 is the number of days to fetch reservations for
    ```

3. **Run tests**:
    - For real data:
      ```sh
      make test
      ```
    - For mock data:
      ```sh
      make test_all_tests
      ```

## 💼 Features

- 🔔 Daily notifications about upcoming check-ins and check-outs.
- 🔑 Assignment of mailboxes for key storage.
- 📅 Customizable notification period (e.g., next 3 days).

## 🛠️ Technologies

- **Python**: Main programming language.
- **ICS (iCalendar)**: For calendar event handling.
- **Requests**: For making HTTP requests.
- **Telegram Bot API**: For interacting with Telegram.

## 📃 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙋‍♂️ Support

If you have any questions, feel free to open an issue or reach out to the maintainers.

Happy automating! 🏡

## File Structure

### Project Directory

- **data/**: Contains ICS files and mock data generator.
  - `apartment_1.ics`, `apartment_2.ics`, `apartment_3.ics`, `apartment_4.ics`, `apartment_5.ics`, `mock_data.py`
- **src/**: Contains the source code for the project.
  - `airbnb_data.py`: Handles fetching and parsing Airbnb reservation data.
  - `config_utils.py`: Utilities for loading and managing configuration files.
  - `main.py`: Main script to run the application.
  - `message_format.py`: Functions for formatting messages.
  - `telegram_bot.py`: Functions for interacting with the Telegram API.
- **tests/**: Contains tests and mock configurations.
  - `config_test.json`: Mock configuration for testing.
  - `test_airbnb.py`: Tests for Airbnb data handling.
  - `test_config.py`: Tests for configuration utilities.
  - `test_message_format.py`: Tests for message formatting.
  - `test_telegram.py`: Tests for Telegram bot functionality.
- **telegramenv/**: Virtual environment directory.
- **.envrc**: Environment variable configuration file.
- **.gitignore**: Git ignore file.
- **.python-version**: Python version file.
- **config.json**: Configuration file for real data.
- **Makefile**: Makefile for building and running the project.
- **README.md**: This README file.
- **requirements.txt**: Project dependencies.

## Automation

To automate the script to run daily, you can use cron jobs on Linux or Task Scheduler on Windows.

### Setting up a Cron Job (Linux)

1. Open the cron table:
    ```sh
    crontab -e
    ```

2. Add the following line to run the script every day at 8 AM:
    ```sh
    0 8 * * * /path/to/telegramenv/bin/python /path/to/your/project/src/main.py config.json 3
    ```

### Setting up a Task Scheduler (Windows)

1. Open Task Scheduler and create a new task.
2. Set the trigger to run daily at your desired time.
3. Set the action to start a program and point it to your Python executable and the script:
    ```
    Program/script: C:\path\to\telegramenv\Scripts\python.exe
    Add arguments: C:\path\to\your\project\src\main.py config.json 3
    ```

---
