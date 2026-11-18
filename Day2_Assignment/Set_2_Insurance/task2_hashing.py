
def normalize(value):
    """
    Remove spaces and convert text to uppercase.
    This helps identify values that differ only
    in letter case or spacing.
    """
    return "".join(value.split()).upper()


def detect_duplicate_claims(claims):

    seen_claims = {}
    duplicates = []

    for claim in claims:

        policy = normalize(claim["policy_number"])
        incident_date = normalize(claim["incident_date"])

        # Create a composite key
        key = (policy, incident_date)

        if key in seen_claims:
            duplicates.append({
                "duplicate_claim": claim["claim_id"],
                "original_claim": seen_claims[key],
                "policy_number": policy,
                "incident_date": incident_date
            })
        else:
            seen_claims[key] = claim["claim_id"]

    return duplicates


# Sample insurance claims
claims = [
    {
        "claim_id": "CLM1001",
        "policy_number": "POL 12345",
        "incident_date": "2026-10-10"
    },
    {
        "claim_id": "CLM1002",
        "policy_number": "pol12345",
        "incident_date": "2026-10-10"
    },
    {
        "claim_id": "CLM1003",
        "policy_number": "POL 67890",
        "incident_date": "2026-10-12"
    },
    {
        "claim_id": "CLM1004",
        "policy_number": "POL 67890",
        "incident_date": "2026-10-12"
    },
    {
        "claim_id": "CLM1005",
        "policy_number": "POL 54321",
        "incident_date": "2026-10-15"
    },
    {
        "claim_id": "CLM1006",
        "policy_number": "POL 12345",
        "incident_date": "2026-10-11"
    }
]


# Display all claims
print("INSURANCE CLAIM RECORDS")
for claim in claims:
    print(claim)


# Detect duplicates
print("\nDUPLICATE CLAIM DETECTION")

duplicates = detect_duplicate_claims(claims)

if duplicates:
    for duplicate in duplicates:
        print(
            f"Duplicate: {duplicate['duplicate_claim']} | "
            f"Original: {duplicate['original_claim']} | "
            f"Policy: {duplicate['policy_number']} | "
            f"Date: {duplicate['incident_date']}"
        )
else:
    print("No duplicate claims found.")


# Test with empty input
print("\nEMPTY INPUT TEST")

empty_result = detect_duplicate_claims([])

if not empty_result:
    print("No claims available. Duplicate list is empty.")


# Test with no duplicates
print("\nNO DUPLICATE TEST")

unique_claims = [
    {
        "claim_id": "CLM2001",
        "policy_number": "POL 111",
        "incident_date": "2026-10-01"
    },
    {
        "claim_id": "CLM2002",
        "policy_number": "POL 222",
        "incident_date": "2026-10-02"
    }
]

unique_result = detect_duplicate_claims(unique_claims)

if not unique_result:
    print("No duplicates found. Test passed.")
