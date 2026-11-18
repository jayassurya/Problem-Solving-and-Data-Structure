
# Binary Search Tree for E-Commerce Product Categories

class Node:
    def __init__(self, category):
        self.category = category
        self.left = None
        self.right = None


class BinarySearchTree:
    def __init__(self):
        self.root = None

    # Insert a category into the BST
    def insert(self, category):
        new_node = Node(category)

        if self.root is None:
            self.root = new_node
            return

        current = self.root

        while True:
            if category.lower() < current.category.lower():
                if current.left is None:
                    current.left = new_node
                    return
                current = current.left

            elif category.lower() > current.category.lower():
                if current.right is None:
                    current.right = new_node
                    return
                current = current.right

            else:
                print("Duplicate category ignored:", category)
                return

    # Search for a category
    def search(self, category):
        current = self.root

        while current is not None:
            if category.lower() == current.category.lower():
                return True

            elif category.lower() < current.category.lower():
                current = current.left

            else:
                current = current.right

        return False

    # Inorder: Left -> Root -> Right
    def inorder(self, node):
        if node:
            self.inorder(node.left)
            print(node.category, end=" | ")
            self.inorder(node.right)

    # Preorder: Root -> Left -> Right
    def preorder(self, node):
        if node:
            print(node.category, end=" | ")
            self.preorder(node.left)
            self.preorder(node.right)

    # Postorder: Left -> Right -> Root
    def postorder(self, node):
        if node:
            self.postorder(node.left)
            self.postorder(node.right)
            print(node.category, end=" | ")


def main():
    bst = BinarySearchTree()

    categories = [
        "Electronics",
        "Fashion",
        "Books",
        "Home",
        "Beauty",
        "Sports",
        "Toys",
        "Furniture",
        "Mobiles",
        "Laptops",
        "Shoes",
        "Watches",
        "Groceries",
        "Kitchen",
        "Gaming"
    ]

    print("E-COMMERCE PRODUCT CATEGORY BST")
    print("=" * 55)

    # Insert categories
    for category in categories:
        bst.insert(category)

    print("Total categories inserted:", len(categories))

    # Search demonstration
    search_category = "Mobiles"

    print("\nSEARCH OPERATION")
    print("-" * 55)

    if bst.search(search_category):
        print(search_category, "category found!")
    else:
        print(search_category, "category not found!")

    # Test unsuccessful search
    print("Camera found:", bst.search("Camera"))

    # Display traversals
    print("\nINORDER TRAVERSAL")
    print("-" * 55)
    bst.inorder(bst.root)

    print("\n\nPREORDER TRAVERSAL")
    print("-" * 55)
    bst.preorder(bst.root)

    print("\n\nPOSTORDER TRAVERSAL")
    print("-" * 55)
    bst.postorder(bst.root)

    print("\n")


if __name__ == "__main__":
    main()
