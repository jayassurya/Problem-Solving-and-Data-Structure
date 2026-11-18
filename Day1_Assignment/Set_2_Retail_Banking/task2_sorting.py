
import csv
import os
import time
from collections import Counter

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
CSV_PATH = os.path.join(BASE_DIR, "data", "transactions.csv")


def load_transactions():
    with open(CSV_PATH, "r", newline="", encoding="utf-8") as file:
        return list(csv.DictReader(file))


def insertion_sort(records):
    arr = records.copy()

    for i in range(1, len(arr)):
        current = arr[i]
        j = i - 1

        # Strictly greater preserves the order of equal dates.
        while j >= 0 and arr[j]["postingDate"] > current["postingDate"]:
            arr[j + 1] = arr[j]
            j -= 1

        arr[j + 1] = current

    return arr


def merge_sort(records):
    if len(records) <= 1:
        return records.copy()

    middle = len(records) // 2
    left = merge_sort(records[:middle])
    right = merge_sort(records[middle:])

    result = []
    i = j = 0

    while i < len(left) and j < len(right):
        # <= ensures the left item comes first on equal dates.
        if left[i]["postingDate"] <= right[j]["postingDate"]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])
    return result


def main():
    transactions = load_transactions()

    # Select the customer with the largest number of transactions.
    counts = Counter(row["accountId"] for row in transactions)
    customer_id, _ = counts.most_common(1)[0]

    statement = [
        row for row in transactions
        if row["accountId"] == customer_id
    ]

    print("CUSTOMER STATEMENT SORTING")
    print("-" * 55)
    print("Selected account:", customer_id)
    print("Transactions in statement:", len(statement))

    start = time.perf_counter()
    insertion_result = insertion_sort(statement)
    insertion_time = time.perf_counter() - start

    start = time.perf_counter()
    merge_result = merge_sort(statement)
    merge_time = time.perf_counter() - start

    # Verify both algorithms produced the same date order.
    insertion_dates = [r["postingDate"] for r in insertion_result]
    merge_dates = [r["postingDate"] for r in merge_result]

    print("\nSORTING RESULTS")
    print("-" * 55)
    print("Insertion Sort time:", round(insertion_time, 6), "seconds")
    print("Merge Sort time:    ", round(merge_time, 6), "seconds")
    print("Both results correctly sorted:",
          insertion_dates == sorted(insertion_dates)
          and merge_dates == sorted(merge_dates))

    print("\nFIRST 5 SORTED TRANSACTIONS")
    print("-" * 55)
    for row in merge_result[:5]:
        print(
            row["transactionId"],
            "|",
            row["postingDate"],
            "| Amount:", row["amount"]
        )

    # Demonstrate stability using two transactions with the same timestamp.
    sample = [
        {"transactionId": "TXN-A", "postingDate": "2026-10-01 10:00:00"},
        {"transactionId": "TXN-B", "postingDate": "2026-10-01 09:00:00"},
        {"transactionId": "TXN-C", "postingDate": "2026-10-01 10:00:00"},
    ]

    print("\nSTABILITY DEMONSTRATION")
    print("-" * 55)

    insertion_sample = insertion_sort(sample)
    merge_sample = merge_sort(sample)

    print("Original order:  ", [r["transactionId"] for r in sample])
    print("Insertion Sort:  ", [r["transactionId"] for r in insertion_sample])
    print("Merge Sort:      ", [r["transactionId"] for r in merge_sample])

    print("\nBoth stable algorithms preserve TXN-A before TXN-C")
    print("because both transactions have the same timestamp.")


if __name__ == "__main__":
    main()
