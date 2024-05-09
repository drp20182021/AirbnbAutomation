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


def format_detailed_message_assign_mailboxes(reservations):
    """
    Formats a detailed message for each reservation and assigns mailboxes according to specific rules.
    Special mailboxes are reserved for specific apartments if they are available.

    Args:
        reservations (dict): A dictionary with dates as keys. Each key contains a dictionary
                             with lists of 'checkins' and 'checkouts'.

    Returns:
        str: A detailed string for each date, showing check-ins and check-outs with assigned mailbox for each apartment,
             ensuring that specific apartments receive dedicated mailboxes when possible.
    """
    result = ""
    # Main list of initially available mailboxes
    general_mailboxes = ["📫 Caja 1", "📫 Caja 2", "📫 Caja 3"]

    for date, res in sorted(reservations.items(), key=lambda x: x[0]):
        mailbox_assignments = {}
        special_mailboxes = {"411": "📫 Caja 411", "611": "📫 Caja 611"}
        # We check if 411 or 611 are at check-ins to reserve your boxes
        for checkin in res["checkins"]:
            apt_number = checkin["apt_number"]
            if apt_number in special_mailboxes:
                mailbox_assignments[apt_number] = special_mailboxes.pop(apt_number)

        result += f"📅 {date.strftime('%A, %d de %B %Y')}\n"
        result += f"🔑 Check-ins: {len(res['checkins'])}\n"

        for checkin in res["checkins"]:
            apt_number = checkin["apt_number"]
            if apt_number not in mailbox_assignments:
                if general_mailboxes:
                    mailbox_assignments[apt_number] = general_mailboxes.pop(0)
                elif (
                    special_mailboxes
                ):  # Assign special boxes if the general ones are sold out
                    key, box = special_mailboxes.popitem()
                    mailbox_assignments[apt_number] = box
                else:
                    mailbox_assignments[apt_number] = "📫 Caja ???"
            result += f"  - Apt {apt_number} - Box {mailbox_assignments[apt_number]}\n"

        result += f"🚪 Check-outs: {len(res['checkouts'])}\n"
        for checkout in res["checkouts"]:
            result += f"  - Apt {checkout['apt_number']}\n"
        result += "----------\n"

    return result


if __name__ == "__main__":
    from airbnb_data import get_airbnb_reservations
    from config_loader import find_config_path, load_configuration

    config_path = find_config_path()
    if config_path:
        config = load_configuration(config_path)
        reservations = get_airbnb_reservations(config, 600)  # Fetch for next 600 days
        print(format_detailed_message_assign_mailboxes(reservations))
    else:
        print("Configuration file not found.")
