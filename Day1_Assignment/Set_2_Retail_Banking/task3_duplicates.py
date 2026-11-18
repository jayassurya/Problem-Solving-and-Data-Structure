
import csv
import os
from collections import defaultdict, deque
from datetime import datetime
from decimal import Decimal

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
CSV_PATH = os.path.join(BASE_DIR, "data", "transactions.csv")


def parse_timestamp(value):
    """Convert ISO timestamp text into a datetime object."""
    return datetime.fromisoformat(value.replace("Z", "+00:00"))


def detect_duplicates(transactions):
    # Sort chronologically so the sliding time window works correctly.
    transactions.sort(key=lambda row: parse_timestamp(row["postingDate"]))

    # Hash map: transaction signature -> recent transactions.
    recent_transactions = defaultdict(deque)

    duplicate_count = 0
    duplicate_records = []

    for transaction in transactions:
        key = (
            transaction["accountId"],
            Decimal(transaction["amount"]).quantize(Decimal("0.01")),
            transaction["merchant"].strip().lower()
        )

        current_time = parse_timestamp(transaction["postingDate"])
        window_start = current_time.timestamp() - 60

        queue = recent_transactions[key]

        # Remove transactions older than 60 seconds.
        while queue and queue[0][0].timestamp() < window_start:
            queue.popleft()

        # If a matching transaction is still in the window,
        # the current transaction is a duplicate posting.
        if queue:
            previous_transaction = queue[-1][1]
            duplicate_count += 1

            duplicate_records.append((
                previous_transaction["transactionId"],
                transaction["transactionId"],
                transaction["accountId"],
                transaction["amount"],
                transaction["merchant"],
                transaction["postingDate"]
            ))

        # Keep the current transaction for future comparisons.
        queue.append((current_time, transaction))

    return duplicate_count, duplicate_records


def main():
    with open(CSV_PATH, "r", newline="", encoding="utf-8") as file:
        transactions = list(csv.DictReader(file))

    print("RETAIL BANKING - DUPLICATE POSTING REVIEW")
    print("-" * 65)
    print("Total transactions loaded:", len(transactions))

    duplicate_count, duplicates = detect_duplicates(transactions)

    print("Duplicate postings detected:", duplicate_count)

    print("\nDUPLICATE TRANSACTION DETAILS")
    print("-" * 65)

    if not duplicates:
        print("No duplicate postings found.")
    else:
        for previous_id, current_id, account, amount, merchant, timestamp in duplicates[:20]:
            print(
                f"Original: {previous_id} | "
                f"Duplicate: {current_id} | "
                f"Account: {account} | "
                f"Amount: {amount} | "
                f"Merchant: {merchant} | "
                f"Time: {timestamp}"
            )

        if len(duplicates) > 20:
            print(f"... and {len(duplicates) - 20} more duplicate postings.")

    print("\nDATA STRUCTURE JUSTIFICATION")
    print("-" * 65)
    print("Dictionary: Groups transactions using account, amount and merchant.")
    print("Deque: Maintains recent matching transactions within the 60-second window.")
    print("Sorting: Ensures transactions are processed in chronological order.")


if __name__ == "__main__":
    main()
