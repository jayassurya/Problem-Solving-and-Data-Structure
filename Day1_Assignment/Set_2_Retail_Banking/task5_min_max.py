
import csv
import os
import time

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
CSV_PATH = os.path.join(BASE_DIR, "data", "transactions.csv")


# ---------------- BRUTE-FORCE APPROACH ----------------

def brute_force_min_max(values):
    minimum = maximum = values[0]
    comparisons = 0

    for value in values[1:]:
        comparisons += 1
        if value < minimum:
            minimum = value

        comparisons += 1
        if value > maximum:
            maximum = value

    return minimum, maximum, comparisons


# ---------------- DIVIDE-AND-CONQUER APPROACH ----------------

def divide_conquer_min_max(values, low, high):
    # Base case: only one element
    if low == high:
        return values[low], values[low], 0

    # Base case: exactly two elements
    if high == low + 1:
        if values[low] < values[high]:
            return values[low], values[high], 1
        else:
            return values[high], values[low], 1

    # Divide the array into two halves
    middle = (low + high) // 2

    left_min, left_max, left_count = divide_conquer_min_max(
        values, low, middle
    )

    right_min, right_max, right_count = divide_conquer_min_max(
        values, middle + 1, high
    )

    # Combine the results
    comparisons = 2
    minimum = min(left_min, right_min)
    maximum = max(left_max, right_max)

    return minimum, maximum, left_count + right_count + comparisons


# ---------------- MAIN PROGRAM ----------------

def main():
    with open(CSV_PATH, "r", newline="", encoding="utf-8") as file:
        transactions = list(csv.DictReader(file))

    amounts = [float(row["amount"]) for row in transactions]

    if not amounts:
        print("No transaction records found.")
        return

    print("RETAIL BANKING - MINIMUM AND MAXIMUM TRANSACTION")
    print("=" * 65)
    print("Total transactions:", len(amounts))

    # Brute-force execution
    start = time.perf_counter()
    brute_min, brute_max, brute_comparisons = brute_force_min_max(amounts)
    brute_time = time.perf_counter() - start

    # Divide-and-conquer execution
    start = time.perf_counter()
    dc_min, dc_max, dc_comparisons = divide_conquer_min_max(
        amounts, 0, len(amounts) - 1
    )
    dc_time = time.perf_counter() - start

    # Display results
    print("\n1. BRUTE-FORCE APPROACH")
    print("-" * 65)
    print(f"Lowest transaction amount : Rs. {brute_min:.2f}")
    print(f"Highest transaction amount: Rs. {brute_max:.2f}")
    print("Comparisons:", brute_comparisons)
    print("Execution time:", round(brute_time, 6), "seconds")

    print("\n2. DIVIDE-AND-CONQUER APPROACH")
    print("-" * 65)
    print(f"Lowest transaction amount : Rs. {dc_min:.2f}")
    print(f"Highest transaction amount: Rs. {dc_max:.2f}")
    print("Comparisons:", dc_comparisons)
    print("Execution time:", round(dc_time, 6), "seconds")

    print("\n3. RESULT VALIDATION")
    print("-" * 65)
    print("Minimum values match:", brute_min == dc_min)
    print("Maximum values match:", brute_max == dc_max)

    print("\n4. COMPLEXITY COMPARISON")
    print("-" * 65)
    print("Brute force       : O(n) time, O(1) auxiliary space")
    print("Divide and conquer: O(n) time, O(log n) recursion space")


if __name__ == "__main__":
    main()
