"""
Temperature Monitor and Alarm Checker
-------------------------------------
Reads 5 temperature readings from a machine, stores them in a list,
prints the highest, lowest and average, and warns if any reading is
above the safe limit.

My own twist:
  1. The user sets the safe limit (different machines, different limits).
  2. Every reading gets a status: OK, WARNING (close to limit) or ALARM.
  3. The program saves a report with date and time to a log file.
"""

import math                      # used to reject nan and inf inputs
from datetime import datetime    # used to put the date and time in the log

NUM_READINGS = 5                 # how many readings we collect
WARNING_MARGIN = 5.0             # within this many degrees of the limit = WARNING
ABSOLUTE_ZERO = -273.15          # no temperature can be lower than this (in C)
LOG_FILE = "temperature_log.txt" # file where reports are saved


def get_number(prompt):
    """Ask the user for a number and keep asking until the input is valid."""
    while True:
        text = input(prompt).strip()
        try:
            value = float(text)              # convert the text to a decimal number
        except ValueError:
            # The user typed letters or symbols instead of a number
            print("  Invalid input. Please type a number, for example 72.5")
            continue                         # go back and ask again

        if not math.isfinite(value):         # catches "nan" and "inf"
            print("  That is not a real temperature. Try again.")
        elif value < ABSOLUTE_ZERO:          # physically impossible
            print("  Temperature cannot be below -273.15 C. Try again.")
        else:
            return value                     # input is good, send it back


def check_status(reading, limit):
    """Return the status of one reading compared with the safe limit."""
    if reading > limit:
        return "ALARM"                       # above the safe limit
    elif reading >= limit - WARNING_MARGIN:
        return "WARNING"                     # close to the limit
    else:
        return "OK"                          # safely below the limit


def collect_readings():
    """Ask the user for NUM_READINGS temperatures and store them in a list."""
    readings = []                            # empty list to store the readings
    for i in range(1, NUM_READINGS + 1):     # loop 5 times
        value = get_number(f"Enter reading {i} of {NUM_READINGS} (C): ")
        readings.append(value)               # add the reading to the list
    return readings


def build_report(readings, limit):
    """Build the full report as a list of text lines."""
    highest = max(readings)                  # largest value in the list
    lowest = min(readings)                   # smallest value in the list
    average = sum(readings) / len(readings)  # total divided by how many

    lines = []
    lines.append(f"Safe limit: {limit:.1f} C")
    lines.append("")
    for i, reading in enumerate(readings, start=1):
        lines.append(f"Reading {i}: {reading:.1f} C  [{check_status(reading, limit)}]")
    lines.append("")
    lines.append(f"Highest : {highest:.1f} C")
    lines.append(f"Lowest  : {lowest:.1f} C")
    lines.append(f"Average : {average:.2f} C")
    lines.append("")

    # Count how many readings went over the safe limit
    over_limit = [r for r in readings if r > limit]
    if len(over_limit) > 0:
        lines.append(f"*** ALARM: {len(over_limit)} reading(s) above the safe limit! "
                     "Check the machine. ***")
    elif highest >= limit - WARNING_MARGIN:
        lines.append("Warning: the machine is running close to the safe limit.")
    else:
        lines.append("All readings are within the safe range.")
    return lines


def save_report(lines):
    """Append the report to the log file with the date and time."""
    try:
        with open(LOG_FILE, "a") as file:    # "a" = add to the end, never erase
            file.write("=== " + datetime.now().strftime("%Y-%m-%d %H:%M:%S") + " ===\n")
            file.write("\n".join(lines) + "\n\n")
        print(f"Report saved to {LOG_FILE}")
    except OSError:
        # Saving can fail (for example, no permission to write)
        print("Could not save the report, but the results above are still correct.")


def main():
    """Run the program. It repeats until the user chooses to quit."""
    print("=== Temperature Monitor and Alarm Checker ===")
    while True:                              # main loop: repeat until the user quits
        limit = get_number("Enter the safe temperature limit for this machine (C): ")
        readings = collect_readings()

        report = build_report(readings, limit)
        print("\n--- REPORT ---")
        for line in report:
            print(line)
        print()

        save_report(report)

        again = input("\nCheck another machine? (y/n): ").strip().lower()
        if again != "y":                     # anything other than y ends the program
            print("Goodbye. Stay safe!")
            break


# Run main() only when this file is run directly
if __name__ == "__main__":
    main()
