
import csv
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
CSV_PATH = os.path.join(BASE_DIR, "data", "transactions.csv")


# ---------------- CUSTOM QUEUE ----------------

class ManualReviewQueue:
    def __init__(self):
        self.items = []
        self.front = 0

    def enqueue(self, transaction):
        self.items.append(transaction)

    def dequeue(self):
        if self.is_empty():
            return None

        transaction = self.items[self.front]
        self.front += 1

        # Compact the list occasionally to avoid retaining old entries.
        if self.front >= 100 and self.front >= len(self.items) // 2:
            self.items = self.items[self.front:]
            self.front = 0

        return transaction

    def is_empty(self):
        return self.front >= len(self.items)

    def size(self):
        return len(self.items) - self.front


# ---------------- CUSTOM STACK ----------------

class AdjustmentStack:
    def __init__(self):
        self.items = []

    def push(self, adjustment):
        self.items.append(adjustment)

    def pop(self):
        if self.is_empty():
            return None
        return self.items.pop()

    def is_empty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)


# ---------------- MAIN PROGRAM ----------------

def main():
    with open(CSV_PATH, "r", newline="", encoding="utf-8") as file:
        transactions = list(csv.DictReader(file))

    print("RETAIL BANKING - QUEUE AND STACK")
    print("=" * 60)

    # QUEUE: Manual review backlog
    print("\n1. MANUAL REVIEW QUEUE (FIFO)")
    print("-" * 60)

    review_queue = ManualReviewQueue()

    # Add the first five transactions to the review queue.
    for transaction in transactions[:5]:
        review_queue.enqueue(transaction)

    print("Transactions added to review queue:", review_queue.size())

    print("\nProcessing transactions in FIFO order:")
    while not review_queue.is_empty():
        transaction = review_queue.dequeue()
        print(
            "Reviewed:",
            transaction["transactionId"],
            "| Account:",
            transaction["accountId"],
            "| Amount:",
            transaction["amount"]
        )

    # STACK: Reverse last adjustment
    print("\n2. ADJUSTMENT HISTORY STACK (LIFO)")
    print("-" * 60)

    current_balance = 10000.00
    history = AdjustmentStack()

    print("Initial balance: Rs.", current_balance)

    # Apply adjustments and save their previous values.
    adjustments = [500.00, -200.00, 300.00]

    for adjustment in adjustments:
        previous_balance = current_balance
        current_balance += adjustment

        history.push({
            "adjustment": adjustment,
            "previous_balance": previous_balance,
            "new_balance": current_balance
        })

        print(
            f"Adjustment: {adjustment:+.2f} | "
            f"Balance: Rs. {current_balance:.2f}"
        )

    print("\nReversing the last adjustment:")

    last_adjustment = history.pop()

    if last_adjustment is not None:
        current_balance = last_adjustment["previous_balance"]

        print("Reversed adjustment:", last_adjustment["adjustment"])
        print("Restored balance: Rs.", current_balance)

    print("\nRemaining adjustment history:", history.size())


if __name__ == "__main__":
    main()
