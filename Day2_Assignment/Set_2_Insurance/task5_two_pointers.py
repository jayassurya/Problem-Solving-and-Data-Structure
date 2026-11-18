
def merge_claims(region_a, region_b):

    i = 0
    j = 0

    merged_claims = []

    # Compare elements from both lists
    while i < len(region_a) and j < len(region_b):

        if region_a[i] <= region_b[j]:
            merged_claims.append(region_a[i])
            i += 1

        else:
            merged_claims.append(region_b[j])
            j += 1

    # Add remaining elements from Region A
    while i < len(region_a):
        merged_claims.append(region_a[i])
        i += 1

    # Add remaining elements from Region B
    while j < len(region_b):
        merged_claims.append(region_b[j])
        j += 1

    return merged_claims


# Sorted claim IDs from two regional offices
region_a_claims = [
    1005, 1010, 1020, 1040, 1060, 1090
]

region_b_claims = [
    1002, 1015, 1025, 1035, 1070, 1100
]


print("REGION A CLAIMS:")
print(region_a_claims)

print("\nREGION B CLAIMS:")
print(region_b_claims)


# Merge both sorted lists
print("\nMERGED CLAIM LIST:")

merged = merge_claims(region_a_claims, region_b_claims)

print(merged)


# Test empty Region A
print("\nEMPTY REGION A TEST")

result = merge_claims([], [1001, 1002, 1003])
print(result)


# Test empty Region B
print("\nEMPTY REGION B TEST")

result = merge_claims([2001, 2002, 2003], [])
print(result)


# Test both lists empty
print("\nBOTH REGIONS EMPTY TEST")

result = merge_claims([], [])
print(result)


# Test duplicate claim IDs
print("\nDUPLICATE CLAIM ID TEST")

result = merge_claims(
    [1001, 1003, 1005],
    [1001, 1002, 1005]
)

print(result)
