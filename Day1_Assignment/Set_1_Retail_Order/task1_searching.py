
import csv
import time
from pathlib import Path

# -----------------------------------------
# STEP 1: LOAD DATASET
# -----------------------------------------

file_path = (
    Path(__file__).parent / "data" / "orders.csv"
)

with open(file_path, "r", newline="", encoding="utf-8") as file:
    reader = csv.DictReader(file)
    orders = list(reader)

# Use exactly 50,000 records as required
orders = orders[:50000]

print("=" * 55)
print("       RETAIL ORDER DESK - SEARCHING")
print("=" * 55)

print("Total orders loaded:", len(orders))


# -----------------------------------------
# STEP 2: LINEAR SEARCH
# -----------------------------------------

def linear_search(data, target):
    comparisons = 0

    for order in data:
        comparisons += 1

        if order["orderId"] == target:
            return order, comparisons

    return None, comparisons


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

        if data[mid]["orderId"] == target:
            return data[mid], comparisons

        elif data[mid]["orderId"] < target:
            low = mid + 1

        else:
            high = mid - 1

    return None, comparisons


# -----------------------------------------
# STEP 4: PREPARE SORTED DATA
# -----------------------------------------

sorted_orders = sorted(
    orders,
    key=lambda order: order["orderId"]
)

# Select the last order to demonstrate
# a worst-case linear search
target_id = orders[-1]["orderId"]

print("\nTarget Order ID:", target_id)


# -----------------------------------------
# STEP 5: TEST BOTH ALGORITHMS
# -----------------------------------------

linear_result, linear_count = linear_search(
    orders, target_id
)

binary_result, binary_count = binary_search(
    sorted_orders, target_id
)

print("\nLINEAR SEARCH RESULT")

if linear_result:
    print("Order Found:", linear_result)
else:
    print("Order Not Found")

print("Comparisons:", linear_count)


print("\nBINARY SEARCH RESULT")

if binary_result:
    print("Order Found:", binary_result)
else:
    print("Order Not Found")

print("Comparisons:", binary_count)


# -----------------------------------------
# STEP 6: BENCHMARK EXECUTION TIME
# -----------------------------------------

repetitions = 100

start = time.perf_counter()

for _ in range(repetitions):
    linear_search(orders, target_id)

linear_time = time.perf_counter() - start


start = time.perf_counter()

for _ in range(repetitions):
    binary_search(sorted_orders, target_id)

binary_time = time.perf_counter() - start


linear_average = linear_time / repetitions
binary_average = binary_time / repetitions


# -----------------------------------------
# STEP 7: DISPLAY PERFORMANCE
# -----------------------------------------

print("\n" + "=" * 55)
print("             PERFORMANCE COMPARISON")
print("=" * 55)

print("Dataset size:", len(orders))
print("Number of repetitions:", repetitions)

print("\nLinear Search")
print("Total time:", round(linear_time, 6), "seconds")
print("Average time:", round(linear_average, 8), "seconds")

print("\nBinary Search")
print("Total time:", round(binary_time, 6), "seconds")
print("Average time:", round(binary_average, 8), "seconds")

print("\nComparison Count")
print("Linear:", linear_count)
print("Binary:", binary_count)

print("\n" + "=" * 55)
print("             TASK 1 COMPLETED")
print("=" * 55)
