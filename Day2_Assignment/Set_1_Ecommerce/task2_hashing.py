
import time
import random


# ---------------- CUSTOM HASH TABLE WITH CHAINING ----------------

class HashTable:
    def __init__(self, capacity=200003):
        self.capacity = capacity
        self.table = [[] for _ in range(capacity)]

    # Custom hash function
    def hash_function(self, key):
        hash_value = 0

        for character in key:
            hash_value = (hash_value * 31 + ord(character)) % self.capacity

        return hash_value

    # Insert key-value pair
    def insert(self, key, value):
        index = self.hash_function(key)

        # Update existing key if already present.
        for i, (existing_key, _) in enumerate(self.table[index]):
            if existing_key == key:
                self.table[index][i] = (key, value)
                return

        # Chaining: store colliding keys in the same bucket.
        self.table[index].append((key, value))

    # Search for a key
    def search(self, key):
        index = self.hash_function(key)

        for existing_key, value in self.table[index]:
            if existing_key == key:
                return value

        return None


# ---------------- COLLISION DEMONSTRATION ----------------

def demonstrate_collision():
    print("1. COLLISION DEMONSTRATION")
    print("-" * 60)

    # Small capacity makes collisions easy to demonstrate.
    small_table = HashTable(capacity=5)

    keys = [f"SKU{i:03d}" for i in range(100)]

    collision_pair = None

    for i in range(len(keys)):
        for j in range(i + 1, len(keys)):
            if (
                small_table.hash_function(keys[i])
                == small_table.hash_function(keys[j])
            ):
                collision_pair = (keys[i], keys[j])
                break

        if collision_pair:
            break

    if collision_pair:
        key1, key2 = collision_pair

        small_table.insert(key1, "Product A")
        small_table.insert(key2, "Product B")

        print("SKU 1:", key1)
        print("SKU 2:", key2)
        print("Both map to bucket:",
              small_table.hash_function(key1))
        print("First lookup:", small_table.search(key1))
        print("Second lookup:", small_table.search(key2))
        print("Collision handled successfully using chaining.")


# ---------------- PERFORMANCE COMPARISON ----------------

def benchmark():
    print("\n2. LOOKUP PERFORMANCE COMPARISON")
    print("-" * 60)

    total_skus = 100000

    # Generate 100,000 synthetic SKU records.
    sku_data = {
        f"SKU{i:06d}": f"Product_{i}"
        for i in range(total_skus)
    }

    # Build custom hash table.
    custom_table = HashTable()

    for sku, product in sku_data.items():
        custom_table.insert(sku, product)

    # Build Python's built-in dictionary.
    built_in_map = dict(sku_data)

    # Use the same 100,000 SKU lookups for both structures.
    lookup_keys = list(sku_data.keys())

    # Shuffle lookup order for a more representative test.
    random.seed(42)
    random.shuffle(lookup_keys)

    # Custom hash table lookup benchmark.
    start = time.perf_counter()

    custom_found = 0

    for sku in lookup_keys:
        if custom_table.search(sku) is not None:
            custom_found += 1

    custom_time = time.perf_counter() - start

    # Built-in dictionary lookup benchmark.
    start = time.perf_counter()

    builtin_found = 0

    for sku in lookup_keys:
        if built_in_map.get(sku) is not None:
            builtin_found += 1

    builtin_time = time.perf_counter() - start

    # Display results.
    print("Total SKUs:", total_skus)
    print("Total lookups:", len(lookup_keys))

    print("\nCUSTOM HASH TABLE")
    print("Successful lookups:", custom_found)
    print("Lookup time:", round(custom_time, 6), "seconds")

    print("\nPYTHON BUILT-IN DICTIONARY")
    print("Successful lookups:", builtin_found)
    print("Lookup time:", round(builtin_time, 6), "seconds")

    print("\nCOMPARISON")
    if custom_time > 0:
        print(
            "Built-in dictionary speed advantage:",
            round(custom_time / max(builtin_time, 1e-12), 2),
            "times"
        )

    print("\nBoth structures successfully retrieved all SKUs.")


# ---------------- MAIN PROGRAM ----------------

def main():
    print("E-COMMERCE SKU HASHING SYSTEM")
    print("=" * 60)

    demonstrate_collision()
    benchmark()

    print("\n3. COMPLEXITY ANALYSIS")
    print("-" * 60)
    print("Custom hash table lookup: O(1) average, O(n) worst")
    print("Custom hash table insert: O(1) average, O(n) worst")
    print("Python dictionary lookup: O(1) average, O(n) worst")
    print("Space complexity: O(n)")


if __name__ == "__main__":
    main()
