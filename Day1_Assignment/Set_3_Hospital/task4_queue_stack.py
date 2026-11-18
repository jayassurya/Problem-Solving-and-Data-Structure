
import csv
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
CSV_PATH = os.path.join(BASE_DIR, "data", "patients.csv")


# ---------------- CUSTOM QUEUE ----------------

class WalkInQueue:
    def __init__(self):
        self.items = []
        self.front = 0

    # Add a patient to the end of the queue.
    def enqueue(self, patient):
        self.items.append(patient)

    # Remove the patient at the front.
    def dequeue(self):
        if self.is_empty():
            return None

        patient = self.items[self.front]
        self.front += 1

        # Compact the queue occasionally.
        if self.front >= 100 and self.front >= len(self.items) // 2:
            self.items = self.items[self.front:]
            self.front = 0

        return patient

    def is_empty(self):
        return self.front >= len(self.items)

    def size(self):
        return len(self.items) - self.front


# ---------------- CUSTOM STACK ----------------

class PatientHistoryStack:
    def __init__(self):
        self.items = []

    # Add recently viewed patient.
    def push(self, patient):
        self.items.append(patient)

    # Retrieve the most recently viewed patient.
    def pop(self):
        if self.is_empty():
            return None

        return self.items.pop()

    def peek(self):
        if self.is_empty():
            return None

        return self.items[-1]

    def is_empty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)


# ---------------- MAIN PROGRAM ----------------

def main():
    with open(CSV_PATH, "r", newline="", encoding="utf-8") as file:
        patients = list(csv.DictReader(file))

    if not patients:
        print("No patient records found.")
        return

    print("HOSPITAL - QUEUE AND STACK MANAGEMENT")
    print("=" * 65)

    # QUEUE: Walk-in token management
    print("\n1. WALK-IN TOKEN QUEUE (FIFO)")
    print("-" * 65)

    walk_in_queue = WalkInQueue()

    # Add the first five patients to the queue.
    for patient in patients[:5]:
        walk_in_queue.enqueue(patient)

    print("Patients waiting:", walk_in_queue.size())

    print("\nCalling patients in arrival order:")

    token_number = 1

    while not walk_in_queue.is_empty():
        patient = walk_in_queue.dequeue()

        print(
            f"Token {token_number}: "
            f"Patient ID: {patient['patientId']} | "
            f"Name: {patient['patientName']}"
        )

        token_number += 1

    # STACK: Recently viewed patient history
    print("\n2. RECENTLY VIEWED PATIENT HISTORY (LIFO)")
    print("-" * 65)

    history = PatientHistoryStack()

    # Simulate viewing three patient records.
    for patient in patients[:3]:
        history.push(patient)
        print("Viewed patient:", patient["patientId"])

    print("\nTotal patients in history:", history.size())

    # Display most recently viewed patient.
    recent = history.peek()

    if recent:
        print(
            "Most recently viewed:",
            recent["patientId"],
            "|",
            recent["patientName"]
        )

    # Retrieve the latest viewed patient.
    print("\nOpening the latest viewed patient:")

    last_viewed = history.pop()

    if last_viewed:
        print(
            "Patient opened:",
            last_viewed["patientId"],
            "|",
            last_viewed["patientName"]
        )

    print("Remaining history entries:", history.size())


if __name__ == "__main__":
    main()
