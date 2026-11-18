
def detect_duplicate_scans(scan_records):

    parcel_lookup = {}
    seen_scans = set()
    duplicates = []

    for record in scan_records:

        tracking_number = record["tracking_number"]
        hub_code = record["hub_code"]

        # Store parcel information in the hash map
        parcel_lookup[tracking_number] = record

        # Create a unique scan key
        scan_key = (tracking_number, hub_code)

        if scan_key in seen_scans:
            duplicates.append({
                "tracking_number": tracking_number,
                "hub_code": hub_code
            })
        else:
            seen_scans.add(scan_key)

    return parcel_lookup, duplicates


# Sample parcel scan records
scan_records = [
    {"tracking_number": "TRK1001", "hub_code": "CHN"},
    {"tracking_number": "TRK1002", "hub_code": "BLR"},
    {"tracking_number": "TRK1003", "hub_code": "HYD"},
    {"tracking_number": "TRK1001", "hub_code": "CHN"},
    {"tracking_number": "TRK1004", "hub_code": "MUM"},
    {"tracking_number": "TRK1002", "hub_code": "BLR"},
    {"tracking_number": "TRK1001", "hub_code": "DEL"},
    {"tracking_number": "TRK1005", "hub_code": "CBE"}
]


print("PARCEL SCAN RECORDS")

for record in scan_records:
    print(record)


# Detect duplicate scans
parcel_lookup, duplicates = detect_duplicate_scans(scan_records)

print("\nPARCEL LOOKUP")
for tracking_number, record in parcel_lookup.items():
    print(tracking_number, ":", record)


print("\nDUPLICATE SCANS")

if duplicates:
    for duplicate in duplicates:
        print(
            f"Parcel {duplicate['tracking_number']} "
            f"was scanned more than once at hub "
            f"{duplicate['hub_code']}."
        )
else:
    print("No duplicate scans found.")


# Empty input test
print("\nEMPTY INPUT TEST")

lookup, duplicate_result = detect_duplicate_scans([])

print("Parcel lookup:", lookup)
print("Duplicates:", duplicate_result)


# No duplicate scans test
print("\nNO DUPLICATE TEST")

unique_records = [
    {"tracking_number": "TRK2001", "hub_code": "CHN"},
    {"tracking_number": "TRK2001", "hub_code": "BLR"},
    {"tracking_number": "TRK2002", "hub_code": "HYD"}
]

lookup, duplicate_result = detect_duplicate_scans(unique_records)

print("Duplicates:", duplicate_result)
