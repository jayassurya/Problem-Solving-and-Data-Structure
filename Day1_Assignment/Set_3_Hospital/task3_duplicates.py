
import csv
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
CSV_PATH = os.path.join(BASE_DIR, "data", "appointments.csv")


def detect_double_bookings(appointments):
    booked_slots = set()
    duplicates = []

    for appointment in appointments:
        # A patient should have only one appointment in a given slot.
        booking_key = (
            appointment["patientId"].strip(),
            appointment["slot"].strip()
        )

        if booking_key in booked_slots:
            duplicates.append(appointment)
        else:
            booked_slots.add(booking_key)

    return duplicates


def main():
    with open(CSV_PATH, "r", newline="", encoding="utf-8") as file:
        appointments = list(csv.DictReader(file))

    print("HOSPITAL - DOUBLE BOOKING DETECTION")
    print("=" * 65)
    print("Total appointments loaded:", len(appointments))

    duplicates = detect_double_bookings(appointments)

    print("Double-booked appointments detected:", len(duplicates))

    print("\nDUPLICATE BOOKING DETAILS")
    print("-" * 65)

    if not duplicates:
        print("No double-bookings found.")
    else:
        for appointment in duplicates[:20]:
            print(
                "Duplicate appointment:", appointment["appointmentId"],
                "| Patient:", appointment["patientId"],
                "| Slot:", appointment["slot"],
                "| Urgency:", appointment["urgency"],
                "| Arrival:", appointment["arrivalTime"]
            )

        if len(duplicates) > 20:
            print("... and", len(duplicates) - 20, "more duplicates.")

    print("\nDATA STRUCTURE JUSTIFICATION")
    print("-" * 65)
    print("Data structure: Set")
    print("Key used: (patientId, slot)")
    print("Average lookup time: O(1)")
    print("Average insertion time: O(1)")
    print("Overall time complexity: O(n)")
    print("Space complexity: O(n)")


if __name__ == "__main__":
    main()
