
def longest_high_claim_streak(claims, threshold=100):

    if not claims:
        return 0, None, None

    max_length = 0
    current_length = 0

    best_start = None
    best_end = None
    current_start = None

    for day, count in enumerate(claims):

        if count > threshold:

            # Start a new consecutive window
            if current_length == 0:
                current_start = day

            current_length += 1

            # Update the longest streak
            if current_length > max_length:
                max_length = current_length
                best_start = current_start
                best_end = day

        else:
            # Break the consecutive streak
            current_length = 0
            current_start = None

    return max_length, best_start, best_end


# Daily insurance claim counts for 30 days
daily_claims = [
    85, 110, 125, 140, 115,
    95, 105, 120, 135, 150,
    160, 90, 80, 115, 130,
    145, 155, 170, 180, 190,
    95, 100, 105, 115, 125,
    90, 85, 110, 120, 130
]


print("DAILY INSURANCE CLAIM COUNTS")
for day, count in enumerate(daily_claims, start=1):
    print(f"Day {day}: {count} claims")


# Find the longest consecutive high-claim streak
print("\nLONGEST HIGH-CLAIM STREAK")

length, start, end = longest_high_claim_streak(daily_claims)

if length > 0:
    print(f"Longest streak: {length} consecutive days")
    print(f"Starting day: {start + 1}")
    print(f"Ending day: {end + 1}")
else:
    print("No days exceeded 100 claims.")


# Empty input test
print("\nEMPTY INPUT TEST")

result = longest_high_claim_streak([])

print("Result:", result)


# No high-claim days test
print("\nNO HIGH-CLAIM DAYS TEST")

result = longest_high_claim_streak([50, 80, 100, 90])

print("Result:", result)


# All days exceed the threshold
print("\nALL DAYS EXCEED THRESHOLD TEST")

result = longest_high_claim_streak([110, 120, 130, 140])

print("Result:", result)
