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

1. **Run the setup script**:
    ```sh
    make setup_config
    ```

    This script will guide you through the process of creating the `config.json` file by asking a series of questions such as:
    - Your Telegram API token
    - Your Telegram chat ID
    - The apartment number and its corresponding iCal URL
    - The mailboxes available for key storage
    - Any special mailboxes assigned to specific apartments

    Example of `config.json`:
    ```json
    {
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
        },
        "mailboxes": [
            "1", "2", "3", "4", "5"
        ],
        "special_mailboxes": {
            "1": "5",
            "2": "4"
        },
        "mock_airbnb_urls": {
            "1": "data/apartment_1.ics",
            "2": "data/apartment_2.ics",
            "3": "data/apartment_3.ics",
            "4": "data/apartment_4.ics",
            "5": "data/apartment_5.ics"
        },
        "mock_mailboxes": [
            "1", "2", "3"
        ],
        "mock_special_mailboxes": {
            "1": "3",
            "2": "1"
        }
    }
    ```

2. **Create mock data**:
    ```sh
    make mock
    ```

    This generates mock ICS files for testing purposes.

### Usage

1. **Run the main script with real data**:
    ```sh
    make run
    ```

    This will fetch reservations from the Airbnb URLs provided in the `config.json` file and send notifications to your Telegram bot.

2. **Run the main script with mock data**:
    ```sh
    make run_mock
    ```

    This will fetch reservations from the mock Airbnb URLs provided in the `config.json` file and send notifications to your Telegram bot.

### Testing

It's important to test your setup to ensure everything is working correctly. The Makefile includes several targets for running different sets of tests.

1. **Run all tests**:
    ```sh
    make test_all_tests
    ```

    This will run all the tests including those for real and mock data.

2. **Run specific tests**:
    - **Telegram Bot Tests**:
      ```sh
      make test_telegram
      ```
      Runs tests related to sending messages via Telegram.

    - **Airbnb Data Tests**:
      ```sh
      make test_airbnb
      ```
      Tests fetching and parsing of Airbnb reservations.

    - **Configuration Tests**:
      ```sh
      make test_config
      ```
      Verifies that the configuration utilities are working correctly.

    - **Message Formatting Tests**:
      ```sh
      make test_message_format
      ```
      Tests the formatting of messages sent to the user.

    - **Mock Airbnb Data Tests**:
      ```sh
      make test_mock_airbnb
      ```
      Tests fetching and parsing of mock Airbnb reservations.

    - **Mock Message Formatting Tests**:
      ```sh
      make test_mock_message_format
      ```
      Tests the formatting of messages using mock data.

    - **Mock Telegram Bot Tests**:
      ```sh
      make test_mock_telegram
      ```
      Tests sending messages via Telegram using mock data.

    - **Mock Configuration Tests**:
      ```sh
      make test_mock_config
      ```
      Verifies that the configuration utilities are working correctly with mock data.

### Example Output

When the script runs, it sends notifications to the specified Telegram chat. An example notification might look like:

📅 Thursday, 06 de June 2024
🔑 Check-ins: 3
  - Apt 1 - 📫 5
  - Apt 3 - 📫 1
  - Apt 5 - 📫 2
🚪 Check-outs: 0
----------
📅 Friday, 07 de June 2024
🔑 Check-ins: 1
  - Apt 3 - 📫 1
🚪 Check-outs: 1
  - Apt 4
----------
📅 Saturday, 08 de June 2024
🔑 Check-ins: 1
  - Apt 4 - 📫 1
🚪 Check-outs: 2
  - Apt 1
  - Apt 3
----------
📅 Sunday, 09 de June 2024
🔑 Check-ins: 2
  - Apt 3 - 📫 1
  - Apt 5 - 📫 2
🚪 Check-outs: 2
  - Apt 3
  - Apt 5
----------
📅 Monday, 10 de June 2024
🔑 Check-ins: 1
  - Apt 4 - 📫 1
🚪 Check-outs: 0
----------

## 💼 Features

- 🔔 Daily notifications about upcoming check-ins and check-outs.
- 🔑 Assignment of mailboxes for key storage.
- 📅 Customizable notification period (e.g., next 3 days).

## 🛠️ Technologies

- **Python**: Main programming language.
- **ICS (iCalendar)**: For calendar data parsing.
- **Telegram Bot API**: For sending notifications.
- **Makefile**: For managing build and test automation.

## 📃 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🙋‍♂️ Support

If you have any questions, feel free to open an issue or reach out to the maintainers.

Happy renting! 🏡

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
    - **Program/script**: `C:\path\to\telegramenv\Scripts\python.exe`
    - **Add arguments**: `C:\path\to\your\project\src\main.py config.json 3`
    - **Start in**: `C:\path\to\your\project`
