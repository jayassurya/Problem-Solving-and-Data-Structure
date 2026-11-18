
from collections import deque


class LogisticsNetwork:

    def __init__(self):
        self.graph = {}

    # Add a hub
    def add_hub(self, hub):
        if hub not in self.graph:
            self.graph[hub] = []

    # Add a direct route (undirected)
    def add_route(self, hub1, hub2):
        self.add_hub(hub1)
        self.add_hub(hub2)

        self.graph[hub1].append(hub2)
        self.graph[hub2].append(hub1)

    # BFS to find the route with the fewest hops
    def shortest_route(self, start, destination):

        if start not in self.graph or destination not in self.graph:
            return None

        queue = deque([[start]])
        visited = {start}

        while queue:
            path = queue.popleft()
            current = path[-1]

            if current == destination:
                return path

            for neighbour in self.graph[current]:
                if neighbour not in visited:
                    visited.add(neighbour)
                    queue.append(path + [neighbour])

        return None

    # DFS to find all reachable hubs
    def reachable_hubs(self, start):

        if start not in self.graph:
            return []

        visited = set()
        result = []

        def dfs(hub):
            visited.add(hub)
            result.append(hub)

            for neighbour in self.graph[hub]:
                if neighbour not in visited:
                    dfs(neighbour)

        dfs(start)

        return result

    # Display adjacency list
    def display_graph(self):

        print("\nLOGISTICS NETWORK - ADJACENCY LIST")

        for hub, neighbours in self.graph.items():
            print(f"{hub} -> {neighbours}")


# Main program

network = LogisticsNetwork()

# Create 10 logistics hubs
hubs = [
    "CHN", "BLR", "HYD", "MUM", "DEL",
    "CBE", "KOC", "PUN", "AMD", "JAI"
]

for hub in hubs:
    network.add_hub(hub)

# Add direct routes between hubs
routes = [
    ("CHN", "BLR"),
    ("CHN", "HYD"),
    ("BLR", "CBE"),
    ("BLR", "HYD"),
    ("HYD", "MUM"),
    ("MUM", "PUN"),
    ("MUM", "DEL"),
    ("DEL", "JAI"),
    ("DEL", "AMD"),
    ("CBE", "KOC"),
    ("PUN", "AMD")
]

for hub1, hub2 in routes:
    network.add_route(hub1, hub2)


# Display network
network.display_graph()


# BFS: Find shortest route
print("\nSHORTEST ROUTE USING BFS")

start = "CHN"
destination = "DEL"

path = network.shortest_route(start, destination)

if path:
    print("Route:", " -> ".join(path))
    print("Number of hops:", len(path) - 1)
else:
    print("No route available.")


# DFS: Find reachable hubs
print("\nREACHABLE HUBS USING DFS")

central_depot = "CHN"

reachable = network.reachable_hubs(central_depot)

print("Central depot:", central_depot)
print("Reachable hubs:", reachable)
print("Total reachable hubs:", len(reachable))


# Test an unknown hub
print("\nUNKNOWN HUB TEST")

print(
    "Route result:",
    network.shortest_route("CHN", "XYZ")
)
