#!/usr/bin/python3
"""Simple templating utility for invitation generation."""


def generate_invitations(template, attendees):
    """Generate invitation files from a template and attendee data."""
    if not isinstance(template, str):
        print("Invalid input: template must be a string.")
        return

    if not isinstance(attendees, list):
        print("Invalid input: attendees must be a list of dictionaries.")
        return

    if any(not isinstance(attendee, dict) for attendee in attendees):
        print("Invalid input: attendees must be a list of dictionaries.")
        return

    if template == "":
        print("Template is empty, no output files generated.")
        return

    if attendees == []:
        print("No data provided, no output files generated.")
        return

    placeholders = ("name", "event_title", "event_date", "event_location")

    for index, attendee in enumerate(attendees, start=1):
        content = template
        for placeholder in placeholders:
            value = attendee.get(placeholder, "N/A")
            if value is None:
                value = "N/A"
            content = content.replace("{" + placeholder + "}", str(value))

        with open(f"output_{index}.txt", "w", encoding="utf-8") as output_file:
            output_file.write(content)
