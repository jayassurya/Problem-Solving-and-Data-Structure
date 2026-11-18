
# ==========================================
# RETAIL ORDER DESK
# TASK 5: GREEDY VS DYNAMIC PROGRAMMING
# ==========================================

# ------------------------------------------
# PART A: GREEDY ALGORITHM
# ------------------------------------------

def greedy_change(amount, denominations):

    denominations = sorted(denominations, reverse=True)

    result = []

    for coin in denominations:

        count = amount // coin

        if count > 0:
            result.append((coin, count))
            amount = amount % coin

    if amount != 0:
        return None

    return result


# ------------------------------------------
# PART B: DYNAMIC PROGRAMMING
# ------------------------------------------

def dp_change(amount, denominations):

    INF = float("inf")

    # dp[i] stores minimum coins for amount i
    dp = [INF] * (amount + 1)

    # Previous denomination used to reach amount i
    previous = [None] * (amount + 1)

    dp[0] = 0

    # Calculate minimum coins for every amount
    for current in range(1, amount + 1):

        for coin in denominations:

            if coin <= current:

                if dp[current - coin] + 1 < dp[current]:

                    dp[current] = dp[current - coin] + 1
                    previous[current] = coin

    # Check if amount is possible
    if dp[amount] == INF:
        return None

    # Reconstruct the selected denominations
    result = []
    current = amount

    while current > 0:

        coin = previous[current]

        result.append(coin)
        current -= coin

    return result


# ------------------------------------------
# PART C: DISPLAY RESULTS
# ------------------------------------------

def display_result(name, result):

    print("\n" + name)

    if result is None:
        print("Refund amount cannot be formed.")
        return

    if result and isinstance(result[0], tuple):

        total = sum(count for coin, count in result)

        for coin, count in result:
            print(f"Rs. {coin} x {count}")

        print("Total notes/coins:", total)

    else:

        for coin in result:
            print("Rs.", coin)

        print("Total notes/coins:", len(result))


# ==========================================
# TEST 1: REALISTIC RETAIL REFUND
# ==========================================

print("=" * 60)
print("       RETAIL ORDER DESK - REFUND SYSTEM")
print("=" * 60)

refund_amount = 786

indian_denominations = [
    500, 200, 100, 50, 20, 10, 5, 2, 1
]

print("\nREFUND AMOUNT: Rs.", refund_amount)

greedy_result = greedy_change(
    refund_amount,
    indian_denominations
)

dp_result = dp_change(
    refund_amount,
    indian_denominations
)

display_result("GREEDY ALGORITHM", greedy_result)
display_result("DYNAMIC PROGRAMMING", dp_result)


# ==========================================
# TEST 2: SHOW GREEDY FAILURE
# ==========================================

print("\n" + "=" * 60)
print("          GREEDY FAILURE DEMONSTRATION")
print("=" * 60)

test_amount = 6
test_denominations = [1, 3, 4]

print("Refund Amount: Rs.", test_amount)
print("Denominations:", test_denominations)

greedy_failure = greedy_change(
    test_amount,
    test_denominations
)

dp_solution = dp_change(
    test_amount,
    test_denominations
)

display_result("GREEDY RESULT", greedy_failure)
display_result("DP RESULT", dp_solution)


# ==========================================
# TEST 3: PERFORMANCE COMPARISON
# ==========================================

print("\n" + "=" * 60)
print("             FINAL COMPARISON")
print("=" * 60)

greedy_count = sum(
    count for coin, count in greedy_result
)

dp_count = len(dp_result)

print("Refund Amount: Rs.", refund_amount)
print("Greedy Notes/Coins:", greedy_count)
print("DP Notes/Coins:", dp_count)

print("\nFor denomination set [1, 3, 4]:")
print("Greedy:", len(greedy_failure), "coins")
print("DP:", len(dp_solution), "coins")

print("\n" + "=" * 60)
print("             TASK 5 COMPLETED")
print("=" * 60)
