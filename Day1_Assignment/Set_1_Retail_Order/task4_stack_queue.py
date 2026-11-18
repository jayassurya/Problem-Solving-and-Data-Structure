
from collections import deque

print("=" * 65)
print("       RETAIL ORDER DESK - STACK AND QUEUE")
print("=" * 65)


# ==================================================
# PART A: CUSTOM STACK IMPLEMENTATION
# ==================================================

class CustomStack:

    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if self.is_empty():
            return None
        return self.items.pop()

    def peek(self):
        if self.is_empty():
            return None
        return self.items[-1]

    def is_empty(self):
        return len(self.items) == 0

    def display(self):
        return self.items.copy()


# ==================================================
# PART B: CUSTOM QUEUE IMPLEMENTATION
# ==================================================

class CustomQueue:

    def __init__(self):
        self.items = []
        self.front = 0

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if self.is_empty():
            return None

        item = self.items[self.front]
        self.front += 1

        # Compact the queue occasionally
        if self.front > 50 and self.front >= len(self.items) // 2:
            self.items = self.items[self.front:]
            self.front = 0

        return item

    def peek(self):
        if self.is_empty():
            return None
        return self.items[self.front]

    def is_empty(self):
        return self.front >= len(self.items)

    def display(self):
        return self.items[self.front:].copy()


# ==================================================
# PART C: STACK - UNDO LAST ORDER EDIT
# ==================================================

print("\n1. CUSTOM STACK - ORDER EDIT HISTORY")

order = {
    "orderId": "ORD1001",
    "amount": 500
}

history = CustomStack()

print("Original Order:", order)

# First edit
history.push(("amount", order["amount"]))
order["amount"] = 700
print("After Edit 1:", order)

# Second edit
history.push(("amount", order["amount"]))
order["amount"] = 900
print("After Edit 2:", order)

# Third edit
history.push(("amount", order["amount"]))
order["amount"] = 1200
print("After Edit 3:", order)

# Undo last edit
last_edit = history.pop()

if last_edit:
    field, old_value = last_edit
    order[field] = old_value

print("After Undo:", order)
print("Remaining History:", history.display())


# ==================================================
# PART D: QUEUE - WAREHOUSE DISPATCH
# ==================================================

print("\n2. CUSTOM QUEUE - DISPATCH LINE")

dispatch = CustomQueue()

dispatch.enqueue("ORD1001")
dispatch.enqueue("ORD1002")
dispatch.enqueue("ORD1003")
dispatch.enqueue("ORD1004")

print("Dispatch Queue:", dispatch.display())

print("Next Order:", dispatch.peek())

print("Dispatched Order:", dispatch.dequeue())
print("Dispatched Order:", dispatch.dequeue())

print("Remaining Queue:", dispatch.display())


# ==================================================
# PART E: BUILT-IN STACK COMPARISON
# ==================================================

print("\n3. BUILT-IN STACK USING PYTHON LIST")

builtin_stack = []

builtin_stack.append("Edit 1")
builtin_stack.append("Edit 2")
builtin_stack.append("Edit 3")

print("Stack:", builtin_stack)
print("Undo:", builtin_stack.pop())
print("Remaining Stack:", builtin_stack)


# ==================================================
# PART F: BUILT-IN QUEUE COMPARISON
# ==================================================

print("\n4. BUILT-IN QUEUE USING DEQUE")

builtin_queue = deque()

builtin_queue.append("ORD1001")
builtin_queue.append("ORD1002")
builtin_queue.append("ORD1003")
builtin_queue.append("ORD1004")

print("Queue:", list(builtin_queue))

print("Dispatched:", builtin_queue.popleft())
print("Dispatched:", builtin_queue.popleft())

print("Remaining Queue:", list(builtin_queue))


# ==================================================
# PART G: COMPARISON
# ==================================================

print("\n5. DATA STRUCTURE COMPARISON")

print("\nCUSTOM STACK")
print("Push: O(1) amortized")
print("Pop: O(1) amortized")
print("Peek: O(1)")

print("\nCUSTOM QUEUE")
print("Enqueue: O(1) amortized")
print("Dequeue: O(1) amortized")
print("Peek: O(1)")

print("\nBUILT-IN STACK (LIST)")
print("Append: O(1) amortized")
print("Pop: O(1)")

print("\nBUILT-IN QUEUE (DEQUE)")
print("Append: O(1)")
print("Popleft: O(1)")
print("Peek: O(1)")

print("\n" + "=" * 65)
print("             TASK 4 COMPLETED")
print("=" * 65)
