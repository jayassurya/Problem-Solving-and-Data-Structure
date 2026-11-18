
from collections import deque


# ---------------- DIRECTED GRAPH ----------------

class DeploymentGraph:
    def __init__(self):
        self.graph = {}

    def add_service(self, service):
        if service not in self.graph:
            self.graph[service] = []

    def add_dependency(self, source, destination):
        self.add_service(source)
        self.add_service(destination)

        if destination not in self.graph[source]:
            self.graph[source].append(destination)

    # ---------------- BFS TRAVERSAL ----------------

    def bfs(self, start):
        if start not in self.graph:
            return []

        visited = set()
        queue = deque([start])
        visited.add(start)
        result = []

        while queue:
            service = queue.popleft()
            result.append(service)

            for neighbour in self.graph[service]:
                if neighbour not in visited:
                    visited.add(neighbour)
                    queue.append(neighbour)

        return result

    # ---------------- DFS TRAVERSAL ----------------

    def dfs(self, start):
        if start not in self.graph:
            return []

        visited = set()
        result = []

        def visit(service):
            visited.add(service)
            result.append(service)

            for neighbour in self.graph[service]:
                if neighbour not in visited:
                    visit(neighbour)

        visit(start)
        return result

    # ---------------- CYCLE DETECTION USING DFS ----------------

    def has_cycle(self):
        # 0 = unvisited, 1 = currently visiting, 2 = completed
        state = {service: 0 for service in self.graph}

        def detect(service):
            state[service] = 1

            for neighbour in self.graph[service]:
                if state[neighbour] == 1:
                    return True

                if state[neighbour] == 0:
                    if detect(neighbour):
                        return True

            state[service] = 2
            return False

        for service in self.graph:
            if state[service] == 0:
                if detect(service):
                    return True

        return False

    # ---------------- TOPOLOGICAL SORT USING BFS ----------------

    def deployment_order(self):
        indegree = {
            service: 0 for service in self.graph
        }

        # Calculate incoming edges.
        for service in self.graph:
            for neighbour in self.graph[service]:
                indegree[neighbour] += 1

        # Start with services having no prerequisites
        # according to the directed edges.
        queue = deque(
            service for service in self.graph
            if indegree[service] == 0
        )

        order = []

        while queue:
            service = queue.popleft()
            order.append(service)

            for neighbour in self.graph[service]:
                indegree[neighbour] -= 1

                if indegree[neighbour] == 0:
                    queue.append(neighbour)

        # If some services remain, a cycle exists.
        if len(order) != len(self.graph):
            return None

        return order


# ---------------- MAIN PROGRAM ----------------

def main():

    print("E-COMMERCE MICROSERVICE DEPLOYMENT")
    print("=" * 65)

    graph = DeploymentGraph()

    # Directed edges:
    # Source service must be deployed before destination service.
    dependencies = [
        ("Cart", "Pricing"),
        ("Pricing", "Inventory"),
        ("Cart", "Authentication"),
        ("Authentication", "Payment"),
        ("Inventory", "Payment"),
        ("Payment", "Order"),
        ("Order", "Notification")
    ]

    for source, destination in dependencies:
        graph.add_dependency(source, destination)

    print("\n1. GRAPH ADJACENCY LIST")
    print("-" * 65)

    for service, neighbours in graph.graph.items():
        print(service, "->", neighbours)

    print("\n2. BFS TRAVERSAL")
    print("-" * 65)
    print("Starting from Cart:")
    print(" -> ".join(graph.bfs("Cart")))

    print("\n3. DFS TRAVERSAL")
    print("-" * 65)
    print("Starting from Cart:")
    print(" -> ".join(graph.dfs("Cart")))

    print("\n4. CIRCULAR DEPENDENCY CHECK")
    print("-" * 65)

    if graph.has_cycle():
        print("Circular dependency detected!")
    else:
        print("No circular dependency detected.")

    print("\n5. VALID DEPLOYMENT ORDER (BFS)")
    print("-" * 65)

    order = graph.deployment_order()

    if order is None:
        print("Deployment order cannot be generated.")
        print("Circular dependency exists.")
    else:
        print(" -> ".join(order))

    # Demonstrate a circular dependency.
    print("\n6. CIRCULAR DEPENDENCY DEMONSTRATION")
    print("-" * 65)

    cyclic_graph = DeploymentGraph()

    cyclic_graph.add_dependency("Cart", "Pricing")
    cyclic_graph.add_dependency("Pricing", "Inventory")
    cyclic_graph.add_dependency("Inventory", "Cart")

    if cyclic_graph.has_cycle():
        print("Cycle detected:")
        print("Cart -> Pricing -> Inventory -> Cart")
    else:
        print("No cycle detected.")


if __name__ == "__main__":
    main()
