
import csv
import time
from pathlib import Path

# -----------------------------------------
# STEP 1: LOAD 100,000 TRANSACTION IDs
# -----------------------------------------

file_path = Path(__file__).parent / "data" / "transactions.csv"

with open(file_path, "r", newline="", encoding="utf-8") as file:
    reader = csv.DictReader(file)
    transactions = list(reader)

transaction_ids = [
    row["transactionId"] for row in transactions[:100000]
]

# Sort transaction IDs
transaction_ids.sort()

n = len(transaction_ids)

print("=" * 65)
print("       RETAIL BANKING - SEARCHING TRANSACTIONS")
print("=" * 65)

print("Total transaction IDs:", n)


# -----------------------------------------
# STEP 2: LINEAR SEARCH
# -----------------------------------------

def linear_search(data, target):
    comparisons = 0

    for i in range(len(data)):
        comparisons += 1

        if data[i] == target:
            return i, comparisons

    return -1, comparisons


# -----------------------------------------
# STEP 3: BINARY SEARCH
# -----------------------------------------

def binary_search(data, target):
    low = 0
    high = len(data) - 1
    comparisons = 0

    while low <= high:
        mid = (low + high) // 2

        comparisons += 1

        if data[mid] == target:
            return mid, comparisons

        elif data[mid] < target:
            low = mid + 1

        else:
            high = mid - 1

    return -1, comparisons


# -----------------------------------------
# STEP 4: BEST CASE
# -----------------------------------------

# Middle element is found immediately by binary search
best_target = transaction_ids[n // 2]

linear_best = linear_search(transaction_ids, transaction_ids[0])
binary_best = binary_search(transaction_ids, best_target)

print("\nBEST CASE")
print("Linear Search Comparisons:", linear_best[1])
print("Binary Search Comparisons:", binary_best[1])


# -----------------------------------------
# STEP 5: AVERAGE CASE
# -----------------------------------------

# Linear search average comparisons for
# uniformly distributed successful searches
linear_average = (n + 1) / 2

# Calculate exact binary search average
binary_total = 0

for target in transaction_ids:
    _, count = binary_search(transaction_ids, target)
    binary_total += count

binary_average = binary_total / n

print("\nAVERAGE CASE")
print("Linear Search Average Comparisons:", linear_average)
print("Binary Search Average Comparisons:", round(binary_average, 4))


# -----------------------------------------
# STEP 6: WORST CASE
# -----------------------------------------

# Linear search worst case: last element
linear_worst = linear_search(
    transaction_ids, transaction_ids[-1]
)

# Find actual maximum binary search comparisons
binary_worst = 0

for target in transaction_ids:
    _, count = binary_search(transaction_ids, target)
    binary_worst = max(binary_worst, count)

print("\nWORST CASE")
print("Linear Search Comparisons:", linear_worst[1])
print("Binary Search Comparisons:", binary_worst)


# -----------------------------------------
# STEP 7: PERFORMANCE BENCHMARK
# -----------------------------------------

target = transaction_ids[-1]
repetitions = 100

start = time.perf_counter()

for _ in range(repetitions):
    linear_search(transaction_ids, target)

linear_time = time.perf_counter() - start


start = time.perf_counter()

for _ in range(repetitions):
    binary_search(transaction_ids, target)

binary_time = time.perf_counter() - start


print("\n" + "=" * 65)
print("             EXECUTION TIME COMPARISON")
print("=" * 65)

print("Dataset Size:", n)
print("Repetitions:", repetitions)

print("\nLinear Search:")
print("Total Time:", round(linear_time, 6), "seconds")
print("Average Time:", round(linear_time / repetitions, 8), "seconds")

print("\nBinary Search:")
print("Total Time:", round(binary_time, 6), "seconds")
print("Average Time:", round(binary_time / repetitions, 8), "seconds")


# -----------------------------------------
# STEP 8: COMPLEXITY SUMMARY
# -----------------------------------------

print("\n" + "=" * 65)
print("             COMPLEXITY ANALYSIS")
print("=" * 65)

print("Linear Search: O(n)")
print("Binary Search: O(log n)")
print("Auxiliary Space: O(1) for both searches")

print("\nTASK 1 COMPLETED")
print("=" * 65)
