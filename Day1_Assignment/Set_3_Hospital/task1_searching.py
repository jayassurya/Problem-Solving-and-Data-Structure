
import csv
import os
import random
import time

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
CSV_PATH = os.path.join(BASE_DIR, "data", "patients.csv")


# ---------------- LINEAR SEARCH ----------------

def linear_search(records, target):
    comparisons = 0

    for record in records:
        comparisons += 1

        if record["patientId"] == target:
            return record, comparisons

    return None, comparisons


# ---------------- BINARY SEARCH ----------------

def binary_search(records, target):
    low = 0
    high = len(records) - 1
    comparisons = 0

    while low <= high:
        middle = (low + high) // 2
        comparisons += 1

        current_id = records[middle]["patientId"]

        if current_id == target:
            return records[middle], comparisons
        elif current_id < target:
            low = middle + 1
        else:
            high = middle - 1

    return None, comparisons


# ---------------- MAIN PROGRAM ----------------

def main():
    with open(CSV_PATH, "r", newline="", encoding="utf-8") as file:
        patients = list(csv.DictReader(file))

    if not patients:
        print("No patient records found.")
        return

    # Create a sorted copy for binary search.
    sorted_patients = sorted(
        patients,
        key=lambda record: record["patientId"]
    )

    # Select 1,000 different patient IDs across the dataset.
    random.seed(42)
    lookup_count = min(1000, len(patients))

    targets = random.sample(
        [record["patientId"] for record in patients],
        lookup_count
    )

    print("HOSPITAL APPOINTMENT DESK - PATIENT SEARCH")
    print("=" * 60)
    print("Total patient records:", len(patients))
    print("Number of lookups:", lookup_count)

    # Linear search benchmark
    linear_comparisons = 0
    linear_found = 0

    start = time.perf_counter()

    for target in targets:
        result, comparisons = linear_search(patients, target)
        linear_comparisons += comparisons

        if result is not None:
            linear_found += 1

    linear_time = time.perf_counter() - start

    # Binary search benchmark
    binary_comparisons = 0
    binary_found = 0

    start = time.perf_counter()

    for target in targets:
        result, comparisons = binary_search(sorted_patients, target)
        binary_comparisons += comparisons

        if result is not None:
            binary_found += 1

    binary_time = time.perf_counter() - start

    # Display comparison
    print("\n1. LINEAR SEARCH RESULTS")
    print("-" * 60)
    print("Patients found:", linear_found)
    print("Total comparisons:", linear_comparisons)
    print("Average comparisons per lookup:",
          round(linear_comparisons / lookup_count, 2))
    print("Total execution time:",
          round(linear_time, 6), "seconds")
    print("Average time per lookup:",
          round(linear_time / lookup_count, 8), "seconds")

    print("\n2. BINARY SEARCH RESULTS")
    print("-" * 60)
    print("Patients found:", binary_found)
    print("Total comparisons:", binary_comparisons)
    print("Average comparisons per lookup:",
          round(binary_comparisons / lookup_count, 2))
    print("Total execution time:",
          round(binary_time, 6), "seconds")
    print("Average time per lookup:",
          round(binary_time / lookup_count, 8), "seconds")

    print("\n3. VALIDATION")
    print("-" * 60)
    print("Both methods found the same number of patients:",
          linear_found == binary_found)

    print("\n4. COMPLEXITY")
    print("-" * 60)
    print("Linear Search : O(n) time, O(1) auxiliary space")
    print("Binary Search : O(log n) time, O(1) auxiliary space")
    print("Binary search requires sorted patient IDs.")


if __name__ == "__main__":
    main()
