from airbnb_data import get_airbnb_reservations
from telegram_bot import send_telegram_message


def assign_mailboxes(checkins):
    """
    Assigns mailboxes to the incoming reservations based on available slots.

    Args:
        checkins (list): A list of check-ins.

    Returns:
        dict: A dictionary mapping apartment numbers to assigned mailboxes.
    """
    mailbox_assignments = {}
    available_mailboxes = ["📫 Caja 1", "📫 Caja 2", "📫 Caja 3", "📫 Caja 611"]

    for checkin in checkins:
        apt_number = checkin["apt_number"]

        if apt_number == 411:
            mailbox_assignments[apt_number] = "📫 Caja 411"
        elif apt_number == 611 and "📫 Caja 611" not in mailbox_assignments.values():
            mailbox_assignments[apt_number] = "📫 Caja 611"
        else:
            if available_mailboxes:
                mailbox_assignments[apt_number] = available_mailboxes.pop(0)
            else:
                mailbox_assignments[apt_number] = "📫 Caja ???"

    return mailbox_assignments


def main():
    """
    Main function that retrieves reservations, generates the message content, and sends it to Telegram.
    """
    reservations = get_airbnb_reservations()

    result = ""

    for date, res in sorted(reservations.items()):
        result += "➖" * 12 + "\n"
        result += f"🚨🚨 **{date.strftime('%A %d de %B')}**\n\n"
        result += f"🔚🔚  {len(res['checkouts'])} CHECKOUTS\n"

        for checkout in res["checkouts"]:
            result += f"{checkout['apt_number']} checkout {checkout['time']}\n"

        result += "\n"
        result += f"🔜🔜  {len(res['checkins'])} CHECK-INS\n"

        for checkin in res["checkins"]:
            result += f"{checkin['apt_number']} check-in {checkin['time']}\n"

        mailbox_assignments = assign_mailboxes(res["checkins"])

        result += "\n"

        for apt_number, mailbox in mailbox_assignments.items():
            result += f"{mailbox}: {apt_number}\n"

        result += "\n"

    send_telegram_message(result)


if __name__ == "__main__":
    main()
