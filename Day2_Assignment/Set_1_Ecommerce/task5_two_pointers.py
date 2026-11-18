
# E-Commerce Gift Card Pair Finder - Two Pointers

import random


def find_gift_card_pairs(order_values, target):
    left = 0
    right = len(order_values) - 1

    pairs = []

    while left < right:
        current_sum = order_values[left] + order_values[right]

        if current_sum == target:
            pairs.append(
                (order_values[left], order_values[right])
            )

            # Skip repeated values to avoid duplicate pairs.
            left_value = order_values[left]
            right_value = order_values[right]

            while left < right and order_values[left] == left_value:
                left += 1

            while left < right and order_values[right] == right_value:
                right -= 1

        elif current_sum < target:
            # Increase the sum.
            left += 1

        else:
            # Decrease the sum.
            right -= 1

    return pairs


def main():
    print("E-COMMERCE - GIFT CARD PAIR FINDER")
    print("=" * 60)

    # Generate synthetic order values.
    random.seed(42)

    order_values = [
        random.choice([100, 150, 200, 250, 300, 350,
                       400, 450, 500, 550, 600, 650,
                       700, 750, 800, 850, 900])
        for _ in range(30)
    ]

    # Add known values to guarantee matching pairs.
    order_values.extend([200, 800, 300, 700, 400, 600])

    # Two pointers require sorted input.
    order_values.sort()

    gift_card_value = 1000

    print("\nSORTED ORDER VALUES")
    print("-" * 60)
    print(order_values)

    print("\nGIFT CARD VALUE")
    print("-" * 60)
    print("Target amount: Rs.", gift_card_value)

    # Find matching pairs.
    matching_pairs = find_gift_card_pairs(
        order_values,
        gift_card_value
    )

    print("\nMATCHING ORDER PAIRS")
    print("-" * 60)

    if matching_pairs:
        for first, second in matching_pairs:
            print(
                f"Rs. {first} + Rs. {second} = "
                f"Rs. {gift_card_value}"
            )
    else:
        print("No matching pairs found.")

    print("\nTotal unique pairs found:", len(matching_pairs))

    print("\nCOMPLEXITY ANALYSIS")
    print("-" * 60)
    print("Sorting: O(n log n)")
    print("Two-pointer search: O(n)")
    print("Overall time including sorting: O(n log n)")
    print("Auxiliary search space: O(1), excluding output")


if __name__ == "__main__":
    main()
