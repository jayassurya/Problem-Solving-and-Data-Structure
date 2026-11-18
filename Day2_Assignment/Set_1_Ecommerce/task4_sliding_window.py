
# E-Commerce Traffic Analysis - Sliding Window

import random


def find_busiest_window(requests, window_size):
    if not requests or window_size <= 0 or window_size > len(requests):
        return None

    # Calculate the first window's total.
    current_sum = sum(requests[:window_size])
    maximum_sum = current_sum
    best_start = 0

    # Slide the window across the remaining hours.
    for i in range(window_size, len(requests)):
        current_sum = (
            current_sum
            - requests[i - window_size]
            + requests[i]
        )

        if current_sum > maximum_sum:
            maximum_sum = current_sum
            best_start = i - window_size + 1

    return best_start, maximum_sum


def main():
    print("E-COMMERCE WEBSITE - TRAFFIC ANALYSIS")
    print("=" * 60)

    # Generate synthetic requests per minute for 24 hours.
    random.seed(42)

    requests = [
        random.randint(100, 1000)
        for _ in range(24)
    ]

    # Add a traffic spike to demonstrate the busiest window.
    requests[10] = 1800
    requests[11] = 2200
    requests[12] = 2000

    print("\nHOURLY REQUESTS PER MINUTE")
    print("-" * 60)

    for hour, rpm in enumerate(requests):
        print(f"Hour {hour:02d}:00 - {rpm} requests/minute")

    # Find the busiest continuous 3-hour window.
    window_size = 3

    result = find_busiest_window(requests, window_size)

    if result is None:
        print("Invalid input.")
        return

    start_hour, maximum_sum = result
    end_hour = start_hour + window_size

    average_rpm = maximum_sum / window_size

    print("\nBUSIEST 3-HOUR WINDOW")
    print("-" * 60)

    print(f"Starting hour: {start_hour:02d}:00")
    print(f"Ending hour:   {end_hour:02d}:00")

    print("\nTraffic during this window:")

    for hour in range(start_hour, end_hour):
        print(f"Hour {hour:02d}:00 - {requests[hour]} requests/minute")

    print("\nTotal RPM values:", maximum_sum)
    print("Average requests per minute:", round(average_rpm, 2))

    print("\nCOMPLEXITY ANALYSIS")
    print("-" * 60)
    print("Time complexity: O(n)")
    print("Space complexity: O(1) auxiliary space")


if __name__ == "__main__":
    main()
