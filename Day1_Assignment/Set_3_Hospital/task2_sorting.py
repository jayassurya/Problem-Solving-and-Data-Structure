
import csv
import os
import time
import random

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
CSV_PATH = os.path.join(BASE_DIR, "data", "appointments.csv")

# Higher number means higher urgency.
URGENCY_RANK = {
    "critical": 4,
    "emergency": 4,
    "high": 3,
    "urgent": 3,
    "medium": 2,
    "normal": 2,
    "low": 1
}


def sorting_key(appointment):
    urgency = appointment["urgency"].strip().lower()

    # Support numeric urgency values too.
    if urgency.isdigit():
        rank = int(urgency)
    else:
        rank = URGENCY_RANK.get(urgency, 0)

    # Higher urgency first, then earlier arrival time.
    return (-rank, appointment["arrivalTime"])


# ---------------- SELECTION SORT ----------------

def selection_sort(records):
    arr = records.copy()
    swaps = 0
    n = len(arr)

    for i in range(n - 1):
        best_index = i

        for j in range(i + 1, n):
            if sorting_key(arr[j]) < sorting_key(arr[best_index]):
                best_index = j

        if best_index != i:
            arr[i], arr[best_index] = arr[best_index], arr[i]
            swaps += 1

    return arr, swaps


# ---------------- QUICK SORT ----------------

def quick_sort(records):
    arr = records.copy()
    swap_count = 0

    def partition(low, high):
        nonlocal swap_count

        # Random pivot helps avoid consistently poor partitions.
        pivot_index = random.randint(low, high)
        arr[pivot_index], arr[high] = arr[high], arr[pivot_index]

        if pivot_index != high:
            swap_count += 1

        pivot = sorting_key(arr[high])
        i = low - 1

        for j in range(low, high):
            if sorting_key(arr[j]) <= pivot:
                i += 1

                if i != j:
                    arr[i], arr[j] = arr[j], arr[i]
                    swap_count += 1

        if i + 1 != high:
            arr[i + 1], arr[high] = arr[high], arr[i + 1]
            swap_count += 1

        return i + 1

    def quick_sort_recursive(low, high):
        if low < high:
            pivot_position = partition(low, high)
            quick_sort_recursive(low, pivot_position - 1)
            quick_sort_recursive(pivot_position + 1, high)

    quick_sort_recursive(0, len(arr) - 1)

    return arr, swap_count


# ---------------- MAIN PROGRAM ----------------

def main():
    with open(CSV_PATH, "r", newline="", encoding="utf-8") as file:
        appointments = list(csv.DictReader(file))

    if not appointments:
        print("No appointment records found.")
        return

    print("HOSPITAL APPOINTMENT - SORTING COMPARISON")
    print("=" * 65)
    print("Total appointments:", len(appointments))

    # Selection Sort
    start = time.perf_counter()
    selection_result, selection_swaps = selection_sort(appointments)
    selection_time = time.perf_counter() - start

    # Quick Sort
    random.seed(42)
    start = time.perf_counter()
    quick_result, quick_swaps = quick_sort(appointments)
    quick_time = time.perf_counter() - start

    expected = sorted(appointments, key=sorting_key)

    selection_correct = (
        [sorting_key(x) for x in selection_result]
        == [sorting_key(x) for x in expected]
    )

    quick_correct = (
        [sorting_key(x) for x in quick_result]
        == [sorting_key(x) for x in expected]
    )

    print("\n1. SELECTION SORT")
    print("-" * 65)
    print("Swaps:", selection_swaps)
    print("Execution time:", round(selection_time, 6), "seconds")
    print("Correctly sorted:", selection_correct)

    print("\n2. QUICK SORT")
    print("-" * 65)
    print("Swaps:", quick_swaps)
    print("Execution time:", round(quick_time, 6), "seconds")
    print("Correctly sorted:", quick_correct)

    print("\n3. FIRST 10 SORTED APPOINTMENTS")
    print("-" * 65)

    for appointment in quick_result[:10]:
        print(
            "Appointment:", appointment["appointmentId"],
            "| Patient:", appointment["patientId"],
            "| Urgency:", appointment["urgency"],
            "| Arrival:", appointment["arrivalTime"]
        )

    print("\n4. COMPLEXITY COMPARISON")
    print("-" * 65)
    print("Selection Sort: O(n²) time, O(n) extra space in this implementation")
    print("Quick Sort: O(n log n) average, O(n²) worst-case time")
    print("Quick Sort: O(log n) average recursion space, O(n) worst case")


if __name__ == "__main__":
    main()
