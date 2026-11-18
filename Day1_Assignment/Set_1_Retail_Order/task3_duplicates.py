
import csv
from pathlib import Path
from collections import defaultdict

# -----------------------------------------
# STEP 1: LOAD ORDER DATASET
# -----------------------------------------

file_path = Path(__file__).parent / "data" / "orders.csv"

with open(file_path, "r", newline="", encoding="utf-8") as file:
    reader = csv.DictReader(file)
    orders = list(reader)

print("=" * 60)
print("       RETAIL ORDER DESK - DUPLICATE DETECTION")
print("=" * 60)

print("Total orders loaded:", len(orders))


# -----------------------------------------
# STEP 2: HASH-BASED DUPLICATE DETECTION
# -----------------------------------------

def detect_duplicates(data):

    order_map = defaultdict(list)
    duplicate_groups = []

    for order in data:

        customer_id = order["customerId"]
        amount = round(float(order["amount"]), 2)

        # Extract date and hour-minute only
        created_at = order["createdAt"]
        minute = created_at[:16]

        # Composite hash key
        key = (customer_id, amount, minute)

        # If key already exists, this is a duplicate
        if order_map[key]:
            order_map[key].append(order)

        else:
            order_map[key].append(order)

    # Collect groups containing more than one order
    for key, matching_orders in order_map.items():

        if len(matching_orders) > 1:
            duplicate_groups.append({
                "customerId": key[0],
                "amount": key[1],
                "minute": key[2],
                "orders": matching_orders
            })

    return duplicate_groups


# -----------------------------------------
# STEP 3: EXECUTE DUPLICATE DETECTION
# -----------------------------------------

duplicates = detect_duplicates(orders)

print("\nDUPLICATE DETECTION RESULTS")

print("Duplicate groups found:", len(duplicates))

duplicate_order_count = sum(
    len(group["orders"]) - 1
    for group in duplicates
)

print("Additional duplicate orders:", duplicate_order_count)


# -----------------------------------------
# STEP 4: DISPLAY SAMPLE DUPLICATES
# -----------------------------------------

print("\nSAMPLE DUPLICATE ORDERS")

for group in duplicates[:10]:

    print("\nCustomer ID:", group["customerId"])
    print("Amount: Rs.", group["amount"])
    print("Date and Minute:", group["minute"])

    for order in group["orders"]:
        print("  Order ID:", order["orderId"])


# -----------------------------------------
# STEP 5: COMPLEXITY INFORMATION
# -----------------------------------------

print("\n" + "=" * 60)
print("             COMPLEXITY ANALYSIS")
print("=" * 60)

print("Time Complexity: O(n) expected")
print("Space Complexity: O(n)")
print("Data Structure: Hash Map / Dictionary")

print("\n" + "=" * 60)
print("             TASK 3 COMPLETED")
print("=" * 60)
