
class Node:
    def __init__(self, claim_id):
        self.claim_id = claim_id
        self.left = None
        self.right = None


class BinarySearchTree:

    def __init__(self):
        self.root = None

    def insert(self, claim_id):
        if self.root is None:
            self.root = Node(claim_id)
        else:
            self._insert_recursive(self.root, claim_id)

    def _insert_recursive(self, current, claim_id):
        if claim_id < current.claim_id:
            if current.left is None:
                current.left = Node(claim_id)
            else:
                self._insert_recursive(current.left, claim_id)

        elif claim_id > current.claim_id:
            if current.right is None:
                current.right = Node(claim_id)
            else:
                self._insert_recursive(current.right, claim_id)

        else:
            print(f"Duplicate claim ID ignored: {claim_id}")

    def search(self, claim_id):
        return self._search_recursive(self.root, claim_id)

    def _search_recursive(self, current, claim_id):
        if current is None:
            return False

        if current.claim_id == claim_id:
            return True

        if claim_id < current.claim_id:
            return self._search_recursive(current.left, claim_id)

        return self._search_recursive(current.right, claim_id)

    def inorder(self, current):
        if current:
            self.inorder(current.left)
            print(current.claim_id, end=" ")
            self.inorder(current.right)

    def preorder(self, current):
        if current:
            print(current.claim_id, end=" ")
            self.preorder(current.left)
            self.preorder(current.right)

    def postorder(self, current):
        if current:
            self.postorder(current.left)
            self.postorder(current.right)
            print(current.claim_id, end=" ")


# Main program
bst = BinarySearchTree()

claim_ids = [
    1050, 1020, 1080, 1010, 1030,
    1060, 1090, 1005, 1025, 1070,
    1100, 1040, 1015, 1085, 1110
]

print("INSERTING CLAIM IDs")
for claim_id in claim_ids:
    bst.insert(claim_id)

print("\nInorder Traversal:")
bst.inorder(bst.root)

print("\n\nPreorder Traversal:")
bst.preorder(bst.root)

print("\n\nPostorder Traversal:")
bst.postorder(bst.root)

print("\n\n\nCLAIM SEARCH")
search_id = 1060

if bst.search(search_id):
    print(f"Claim ID {search_id} found.")
else:
    print(f"Claim ID {search_id} not found.")

search_id = 1200

if bst.search(search_id):
    print(f"Claim ID {search_id} found.")
else:
    print(f"Claim ID {search_id} not found.")
