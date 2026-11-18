
def highest_average_window(parcel_counts, window_size=4):

    if not parcel_counts or window_size <= 0:
        return None

    if window_size > len(parcel_counts):
        return None

    # Calculate the first window sum
    current_sum = sum(parcel_counts[:window_size])

    max_sum = current_sum
    best_start = 0

    # Slide the window through the remaining hours
    for i in range(window_size, len(parcel_counts)):

        # Remove outgoing value and add incoming value
        current_sum += parcel_counts[i]
        current_sum -= parcel_counts[i - window_size]

        if current_sum > max_sum:
            max_sum = current_sum
            best_start = i - window_size + 1

    average = max_sum / window_size

    return best_start, best_start + window_size - 1, max_sum, average


# Parcel counts for 24 hours
hourly_parcels = [
    45, 50, 55, 60,
    65, 70, 75, 80,
    90, 100, 120, 140,
    160, 180, 200, 190,
    170, 150, 130, 110,
    90, 80, 70, 60
]


print("HOURLY PARCEL COUNTS")

for hour, count in enumerate(hourly_parcels):
    print(f"Hour {hour}: {count} parcels")


# Find highest-average 4-hour window
print("\nHIGHEST-AVERAGE 4-HOUR WINDOW")

result = highest_average_window(hourly_parcels, 4)

if result:
    start, end, total, average = result

    print(f"Starting hour: {start}")
    print(f"Ending hour: {end}")
    print(f"Total parcels: {total}")
    print(f"Average parcels per hour: {average:.2f}")

    print("\nSelected parcel counts:")
    print(hourly_parcels[start:end + 1])
else:
    print("A valid 4-hour window is not available.")


# Empty input test
print("\nEMPTY INPUT TEST")
print(highest_average_window([], 4))


# Window larger than input test
print("\nWINDOW SIZE TEST")
print(highest_average_window([10, 20, 30], 4))


# All values are equal
print("\nEQUAL VALUES TEST")
print(highest_average_window([50, 50, 50, 50, 50], 4))
