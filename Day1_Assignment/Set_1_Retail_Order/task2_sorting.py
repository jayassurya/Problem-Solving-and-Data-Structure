
import csv
import time
from pathlib import Path

# -----------------------------------------
# STEP 1: LOAD 10,000 ORDERS
# -----------------------------------------

file_path = Path(__file__).parent / "data" / "orders.csv"

with open(file_path, "r", newline="", encoding="utf-8") as file:
    reader = csv.DictReader(file)
    orders = list(reader)

orders = orders[:10000]

print("=" * 60)
print("          RETAIL ORDER DESK - SORTING")
print("=" * 60)

print("Total orders:", len(orders))


# -----------------------------------------
# STEP 2: BUBBLE SORT - O(n^2)
# DESCENDING ORDER
# -----------------------------------------

def bubble_sort(data):
    arr = data.copy()
    n = len(arr)

    for i in range(n):
        swapped = False

        for j in range(0, n - i - 1):

            if float(arr[j]["amount"]) < float(arr[j + 1]["amount"]):
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True

        if not swapped:
            break

    return arr


# -----------------------------------------
# STEP 3: MERGE SORT - O(n log n)
# DESCENDING ORDER
# -----------------------------------------

def merge(left, right):
    result = []
    i = 0
    j = 0

    while i < len(left) and j < len(right):

        if float(left[i]["amount"]) >= float(right[j]["amount"]):
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])

    return result


def merge_sort(data):

    if len(data) <= 1:
        return data.copy()

    mid = len(data) // 2

    left = merge_sort(data[:mid])
    right = merge_sort(data[mid:])

    return merge(left, right)


# -----------------------------------------
# STEP 4: TRACE FIRST THREE BUBBLE PASSES
# -----------------------------------------

sample = [250, 100, 400, 150, 300]

print("\nBUBBLE SORT - FIRST THREE PASSES")
print("Original:", sample)

trace = sample.copy()
n = len(trace)

for i in range(3):

    for j in range(n - i - 1):

        if trace[j] < trace[j + 1]:
            trace[j], trace[j + 1] = trace[j + 1], trace[j]

    print(f"Pass {i + 1}:", trace)


# -----------------------------------------
# STEP 5: BENCHMARK ALL THREE METHODS
# -----------------------------------------

# Bubble Sort
start = time.perf_counter()
bubble_result = bubble_sort(orders)
bubble_time = time.perf_counter() - start


# Merge Sort
start = time.perf_counter()
merge_result = merge_sort(orders)
merge_time = time.perf_counter() - start


# Built-in Sort
start = time.perf_counter()

builtin_result = sorted(
    orders,
    key=lambda order: float(order["amount"]),
    reverse=True
)

builtin_time = time.perf_counter() - start


# -----------------------------------------
# STEP 6: VERIFY SORTING CORRECTNESS
# -----------------------------------------

def is_sorted_descending(data):
    return all(
        float(data[i]["amount"]) >= float(data[i + 1]["amount"])
        for i in range(len(data) - 1)
    )


print("\nSORTING VALIDATION")

print("Bubble Sort:", is_sorted_descending(bubble_result))
print("Merge Sort:", is_sorted_descending(merge_result))
print("Built-in Sort:", is_sorted_descending(builtin_result))


# -----------------------------------------
# STEP 7: DISPLAY PERFORMANCE
# -----------------------------------------

print("\n" + "=" * 60)
print("              PERFORMANCE COMPARISON")
print("=" * 60)

print("Dataset size:", len(orders))

print("\nBubble Sort")
print("Execution time:", round(bubble_time, 4), "seconds")

print("\nMerge Sort")
print("Execution time:", round(merge_time, 4), "seconds")

print("\nPython Built-in Sort")
print("Execution time:", round(builtin_time, 4), "seconds")


# -----------------------------------------
# STEP 8: DISPLAY TOP FIVE ORDERS
# -----------------------------------------

print("\nTOP FIVE ORDERS BY AMOUNT")

for order in merge_result[:5]:
    print(
        order["orderId"],
        "Amount: Rs.",
        order["amount"]
    )


print("\n" + "=" * 60)
print("             TASK 2 COMPLETED")
print("=" * 60)
