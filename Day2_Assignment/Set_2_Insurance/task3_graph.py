
from collections import deque


class ClaimApprovalGraph:

    def __init__(self):
        self.graph = {}

    # Add a stage to the graph
    def add_stage(self, stage):
        if stage not in self.graph:
            self.graph[stage] = []

    # Add a directed connection
    def add_connection(self, source, destination):
        self.add_stage(source)
        self.add_stage(destination)

        self.graph[source].append(destination)

    # BFS to find the shortest path
    def shortest_path_bfs(self, start, target):

        if start not in self.graph or target not in self.graph:
            return None

        queue = deque([[start]])
        visited = {start}

        while queue:
            path = queue.popleft()
            current = path[-1]

            if current == target:
                return path

            for neighbour in self.graph[current]:
                if neighbour not in visited:
                    visited.add(neighbour)
                    queue.append(path + [neighbour])

        return None

    # DFS-based cycle detection
    def has_cycle(self):

        visited = set()
        recursion_stack = set()

        def dfs(stage):

            visited.add(stage)
            recursion_stack.add(stage)

            for neighbour in self.graph[stage]:

                if neighbour not in visited:
                    if dfs(neighbour):
                        return True

                elif neighbour in recursion_stack:
                    return True

            recursion_stack.remove(stage)
            return False

        for stage in self.graph:
            if stage not in visited:
                if dfs(stage):
                    return True

        return False

    # Display adjacency list
    def display_graph(self):

        print("\nCLAIM APPROVAL GRAPH")

        for stage, connections in self.graph.items():
            print(f"{stage} -> {connections}")


# Main program
approval = ClaimApprovalGraph()

# Add approval stages
stages = [
    "Registration",
    "Assessment",
    "Surveyor",
    "Settlement"
]

for stage in stages:
    approval.add_stage(stage)

# Add directed connections
approval.add_connection("Registration", "Assessment")
approval.add_connection("Assessment", "Surveyor")
approval.add_connection("Surveyor", "Settlement")

# Fast-track settlement route
approval.add_connection("Assessment", "Settlement")

# Reassessment route, which creates a cycle
approval.add_connection("Surveyor", "Assessment")

# Display graph
approval.display_graph()

# Find shortest path using BFS
print("\nSHORTEST APPROVAL PATH")

start = "Registration"
target = "Settlement"

path = approval.shortest_path_bfs(start, target)

if path:
    print(" -> ".join(path))
    print("Number of transitions:", len(path) - 1)
else:
    print("No path found.")

# Detect cycles using DFS
print("\nCYCLE DETECTION")

if approval.has_cycle():
    print("Cycle detected in the approval process.")
else:
    print("No cycle detected.")
