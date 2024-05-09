def generate_mock_ics(file_path):
    ics_content = """BEGIN:VCALENDAR
VERSION:2.0
PRODID:-//Airbnb Inc//Hosting Calendar 0.8.8//EN
CALSCALE:GREGORIAN
BEGIN:VEVENT
DTSTART;VALUE=DATE:20250510
DTEND;VALUE=DATE:20250512
SUMMARY:Reserved
UID:123456789-abcd1234@airbnb.com
DESCRIPTION:Reservation URL: https://www.airbnb.com/reservation/itinerary
END:VEVENT
BEGIN:VEVENT
DTSTART;VALUE=DATE:20250501
DTEND;VALUE=DATE:20250502
SUMMARY:Airbnb (Not available)
UID:abcdef1234-5678efgh@airbnb.com
END:VEVENT
BEGIN:VEVENT
DTSTART;VALUE=DATE:20250420
DTEND;VALUE=DATE:20250422
SUMMARY:Airbnb (Not available)
UID:5678efgh-1234abcd@airbnb.com
END:VEVENT
BEGIN:VEVENT
DTSTART;VALUE=DATE:20250501
DTEND;VALUE=DATE:20250505
SUMMARY:Reserved
UID:abcd5678-efgh1234@airbnb.com
DESCRIPTION:Reservation URL: https://www.airbnb.com/reservation/itinerary
END:VEVENT
END:VCALENDAR
"""

    with open(file_path, "w") as f:
        f.write(ics_content)


# Generate and save the .ics file
generate_mock_ics("mock_airbnb_calendar.ics")
