
class Node:
    def __init__(self, hub_code):
        self.hub_code = hub_code
        self.left = None
        self.right = None


class BinarySearchTree:

    def __init__(self):
        self.root = None

    def insert(self, hub_code):
        if self.root is None:
            self.root = Node(hub_code)
        else:
            self._insert_recursive(self.root, hub_code)

    def _insert_recursive(self, current, hub_code):
        if hub_code < current.hub_code:
            if current.left is None:
                current.left = Node(hub_code)
            else:
                self._insert_recursive(current.left, hub_code)

        elif hub_code > current.hub_code:
            if current.right is None:
                current.right = Node(hub_code)
            else:
                self._insert_recursive(current.right, hub_code)

        else:
            print(f"Duplicate hub code ignored: {hub_code}")

    def search(self, hub_code):
        current = self.root

        while current is not None:
            if current.hub_code == hub_code:
                return True
            elif hub_code < current.hub_code:
                current = current.left
            else:
                current = current.right

        return False

    def height(self, current):
        if current is None:
            return 0

        left_height = self.height(current.left)
        right_height = self.height(current.right)

        return 1 + max(left_height, right_height)

    def inorder(self, current):
        if current:
            self.inorder(current.left)
            print(current.hub_code, end=" ")
            self.inorder(current.right)


# Main program

hub_codes = [
    "CHN", "BLR", "HYD", "MUM", "DEL",
    "CBE", "KOC", "PUN", "AMD", "JAI"
]

bst = BinarySearchTree()

print("INSERTING HUB CODES")
for code in hub_codes:
    bst.insert(code)

print("\nINORDER TRAVERSAL")
bst.inorder(bst.root)

print("\n\nHUB SEARCH")

search_code = "HYD"

if bst.search(search_code):
    print(f"{search_code} found in the network.")
else:
    print(f"{search_code} not found.")

print("\nTREE HEIGHT")
print("Height:", bst.height(bst.root), "levels")


# Demonstrate the effect of sorted insertion

sorted_bst = BinarySearchTree()

sorted_codes = sorted(hub_codes)

for code in sorted_codes:
    sorted_bst.insert(code)

print("\nSORTED INSERTION TEST")
print("Sorted hub codes:", sorted_codes)
print("Height after sorted insertion:",
      sorted_bst.height(sorted_bst.root), "levels")
