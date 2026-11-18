
import re


def is_palindrome_route(route):

    # Extract hub codes, ignoring separators and spaces
    hub_codes = re.findall(r"[A-Za-z0-9]+", route)

    # Convert all hub codes to uppercase
    hub_codes = [code.upper() for code in hub_codes]

    left = 0
    right = len(hub_codes) - 1

    # Compare codes from both ends
    while left < right:

        if hub_codes[left] != hub_codes[right]:
            return False

        left += 1
        right -= 1

    return True


# Main program

routes = [
    "CHN-BLR-HYD-BLR-CHN",
    "CHN/BLR/HYD/DEL",
    "chn,blr,hyd,blr,chn",
    "MUM - PUN - DEL - PUN - MUM"
]

print("DELIVERY ROUTE PALINDROME CHECK")

for route in routes:

    result = is_palindrome_route(route)

    print("\nRoute:", route)

    if result:
        print("Result: Palindrome route")
    else:
        print("Result: Not a palindrome route")


# Empty input test
print("\nEMPTY INPUT TEST")

print("Result:", is_palindrome_route(""))


# Single hub test
print("\nSINGLE HUB TEST")

print("Result:", is_palindrome_route("CHN"))


# Case-insensitive test
print("\nCASE-INSENSITIVE TEST")

print("Result:", is_palindrome_route("chn-BLR-CHN"))


# Route with different starting and ending hubs
print("\nNON-PALINDROME TEST")

print("Result:", is_palindrome_route("CHN-BLR-HYD-DEL"))
