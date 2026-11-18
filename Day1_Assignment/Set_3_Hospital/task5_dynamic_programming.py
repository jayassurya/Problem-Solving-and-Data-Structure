
from datetime import datetime


# ---------------- SAMPLE APPOINTMENT DATA ----------------
# Each appointment has a start time and an end time.
# Different appointments have different durations.

appointments = [
    {"id": "A1", "start": "09:00", "end": "12:00"},
    {"id": "A2", "start": "09:00", "end": "10:00"},
    {"id": "A3", "start": "10:00", "end": "11:00"},
    {"id": "A4", "start": "11:00", "end": "12:00"},
    {"id": "A5", "start": "12:00", "end": "13:00"},
    {"id": "A6", "start": "09:30", "end": "11:30"},
    {"id": "A7", "start": "13:00", "end": "14:30"},
]


def to_minutes(time_string):
    """Convert HH:MM into minutes from midnight."""
    time_value = datetime.strptime(time_string, "%H:%M")
    return time_value.hour * 60 + time_value.minute


# ---------------- DYNAMIC PROGRAMMING ----------------

def maximum_appointments_dp(records):
    # Sort appointments by finishing time.
    sorted_records = sorted(
        records,
        key=lambda appointment: to_minutes(appointment["end"])
    )

    n = len(sorted_records)

    # Find the last compatible appointment for each appointment.
    previous = []

    for i in range(n):
        compatible_index = -1
        current_start = to_minutes(sorted_records[i]["start"])

        for j in range(i - 1, -1, -1):
            previous_end = to_minutes(sorted_records[j]["end"])

            if previous_end <= current_start:
                compatible_index = j
                break

        previous.append(compatible_index)

    # dp[i] stores the maximum appointments among first i records.
    dp = [0] * (n + 1)

    for i in range(1, n + 1):
        include = 1 + dp[previous[i - 1] + 1]
        exclude = dp[i - 1]

        dp[i] = max(include, exclude)

    # Reconstruct the selected appointments.
    selected = []
    i = n

    while i > 0:
        include = 1 + dp[previous[i - 1] + 1]
        exclude = dp[i - 1]

        if include > exclude:
            selected.append(sorted_records[i - 1])
            i = previous[i - 1] + 1
        else:
            i -= 1

    selected.reverse()

    return dp[n], selected


# ---------------- GREEDY APPROACH ----------------

def greedy_earliest_start(records):
    # A simple greedy strategy: choose the earliest starting
    # appointment that does not overlap the previous selection.
    sorted_records = sorted(
        records,
        key=lambda appointment: to_minutes(appointment["start"])
    )

    selected = []
    last_end = -1

    for appointment in sorted_records:
        start = to_minutes(appointment["start"])
        end = to_minutes(appointment["end"])

        if start >= last_end:
            selected.append(appointment)
            last_end = end

    return selected


# ---------------- MAIN PROGRAM ----------------

def main():
    print("HOSPITAL - APPOINTMENT SCHEDULING")
    print("=" * 65)

    print("\nAVAILABLE APPOINTMENTS")
    print("-" * 65)

    for appointment in appointments:
        print(
            appointment["id"],
            "| Start:", appointment["start"],
            "| End:", appointment["end"]
        )

    # Dynamic Programming
    dp_count, dp_selected = maximum_appointments_dp(appointments)

    print("\n1. DYNAMIC PROGRAMMING RESULT")
    print("-" * 65)
    print("Maximum appointments:", dp_count)

    for appointment in dp_selected:
        print(
            appointment["id"],
            "|", appointment["start"],
            "-", appointment["end"]
        )

    # Greedy
    greedy_selected = greedy_earliest_start(appointments)

    print("\n2. GREEDY RESULT (EARLIEST START)")
    print("-" * 65)
    print("Appointments selected:", len(greedy_selected))

    for appointment in greedy_selected:
        print(
            appointment["id"],
            "|", appointment["start"],
            "-", appointment["end"]
        )

    # Comparison
    print("\n3. COMPARISON")
    print("-" * 65)
    print("Dynamic Programming:", dp_count)
    print("Greedy:", len(greedy_selected))

    if dp_count > len(greedy_selected):
        print("Dynamic Programming selected more appointments.")
    elif dp_count == len(greedy_selected):
        print("Both approaches selected the same number.")
    else:
        print("Greedy selected more appointments.")

    print("\n4. COMPLEXITY")
    print("-" * 65)
    print("Dynamic Programming: O(n²) time, O(n) space")
    print("Greedy earliest-start: O(n log n) time, O(n) space")


if __name__ == "__main__":
    main()
