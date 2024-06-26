from airbnb_data import get_airbnb_reservations
from config_utils import find_config_path, load_configuration, print_pretty_json


def format_basic_message(reservations):
    """
    Formats a basic message summarizing reservations.

    Args:
        reservations (dict): A dictionary with dates as keys. Each key has a dictionary
                             indicating lists of check-ins and check-outs.

    Returns:
        str: A string that summarizes the number of check-ins and check-outs per date,
             formatted as 'Fecha: YYYY-MM-DD - Check-ins: X, Check-outs: Y' for each date.
    """
    result = "Reservations Summary:\n"
    for date, res in sorted(reservations.items()):
        result += f"Fecha: {date.strftime('%Y-%m-%d')} - Check-ins: {len(res['checkins'])}, Check-outs: {len(res['checkouts'])}\n"
    return result


def format_detailed_message(reservations):
    """
    Formats a detailed message with specific information for each reservation.

    Args:
        reservations (dict): A dictionary with dates as keys. Each key has a dictionary
                             of 'checkins' and 'checkouts' lists.

    Returns:
        str: A string detailing each date's reservations, including the check-in and check-out times for each apartment,
             formatted with icons and timestamps.
    """
    result = ""
    for date, res in sorted(reservations.items()):
        result += f"📅 {date.strftime('%A, %d de %B %Y')}\n"
        result += f"🔑 Check-ins: {len(res['checkins'])}\n"
        for checkin in res["checkins"]:
            result += f"  - Apt {checkin['apt_number']}\n"
        result += f"🚪 Check-outs: {len(res['checkouts'])}\n"
        for checkout in res["checkouts"]:
            result += f"  - Apt {checkout['apt_number']}\n"
        result += "----------\n"
    return result


def format_detailed_message_assign_mailboxes(
    reservations, mailboxes, special_mailboxes
):
    """
    Formats a detailed message for each reservation and assigns mailboxes according to specific rules.
    Special mailboxes are reserved for specific apartments if they are available.

    Args:
        reservations (dict): A dictionary with dates as keys. Each key contains a dictionary
                             with lists of 'checkins' and 'checkouts'.
        mailboxes (list): A list of general mailboxes.
        special_mailboxes (dict): A dictionary mapping specific apartments to special mailboxes.

    Returns:
        str: A detailed string for each date, showing check-ins and check-outs with assigned mailbox for each apartment,
             ensuring that specific apartments receive dedicated mailboxes when possible.
    """
    result = ""

    for date, res in sorted(reservations.items(), key=lambda x: x[0]):

        # Reset mailboxes for each day
        available_mailboxes = mailboxes[:]
        mailbox_assignments = {}

        result += f"📅 {date.strftime('%A, %d de %B %Y')}\n"
        result += f"🔑 Check-ins: {len(res['checkins'])}\n"

        # Assign special mailboxes first if applicable
        for checkin in res["checkins"]:
            apt_number = checkin["apt_number"]
            if (
                apt_number in special_mailboxes
                and special_mailboxes[apt_number] not in mailbox_assignments.values()
            ):
                mailbox_assignments[apt_number] = special_mailboxes[apt_number]
                available_mailboxes.remove(special_mailboxes[apt_number])

        # Assign general mailboxes
        for checkin in res["checkins"]:
            apt_number = checkin["apt_number"]
            if apt_number not in mailbox_assignments:
                if available_mailboxes:
                    mailbox_assignments[apt_number] = available_mailboxes.pop(0)
                else:
                    # If no mailboxes left, assign default
                    mailbox_assignments[apt_number] = "???"

            result += f"  - Apt {apt_number} - 📫 {mailbox_assignments[apt_number]}\n"

        result += f"🚪 Check-outs: {len(res['checkouts'])}\n"
        for checkout in res["checkouts"]:
            result += f"  - Apt {checkout['apt_number']}\n"
        result += "----------\n"

    return result


if __name__ == "__main__":
    config_path = find_config_path()
    if not config_path:
        print("Configuration file not found.")
        exit(1)

    config = load_configuration(config_path)
    if config:
        reservations = get_airbnb_reservations(config, 600)  # Fetch for next 600 days
        print(f"Messages for reservations from {config_path}:")
        print("Basic Message:")
        print(format_basic_message(reservations))
        print("Detailed Message:")
        print(format_detailed_message(reservations))
        print("Detailed Message with Mailboxes:")
        mailboxes = config.get("mailboxes", [])
        special_mailboxes = config.get("special_mailboxes", {})
        print(
            format_detailed_message_assign_mailboxes(
                reservations, mailboxes, special_mailboxes
            )
        )
    else:
        print(f"Failed to load configuration from {config_path}.")
