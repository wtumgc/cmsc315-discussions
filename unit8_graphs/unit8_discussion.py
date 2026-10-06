"""
===========================================================
UNIT 8 DISCUSSION: BREADTH-FIRST SEARCH (BFS)
===========================================================

STUDENT INSTRUCTIONS:

This assignment is designed to help you understand how graphs
are traversed using Breadth-First Search (BFS) and how this
applies to real-world systems (e.g., networks, routes,
social connections).

===========================================================
"""

from collections import deque


def bfs(graph, start):
    """
    TODO (Student):
    Implement Breadth-First Search (BFS).

    Requirements:
    - Use a queue to manage traversal order.
    - Track visited nodes to prevent revisiting nodes.
    - Visit nodes level by level.
    - Return the order in which nodes were visited.

    Add comments explaining:
    - Why a queue is used.
    - Why neighbors are added to the queue.
    - How BFS differs from depth-first traversal.
    """

    #   Create variables to track traversed and visited nodes
    visited_nodes = set()       # prevents revisiting
    traversal_queue = deque()   # tracks BFS order
    results = []                # record result hops

    #   BFS uses a FIFO queue to track the order
    #   in which nodes are visited
    traversal_queue.append(start)
    visited_nodes.add(start)

    while traversal_queue:
        current = traversal_queue.popleft()
        results.append(current)

        #   Add unvisited adjacent nodes to the visited
        #   and traversal queues so that the BFS search
        #   can visit the current level first.
        for neighbor in graph[current]:
            if neighbor not in visited_nodes:
                visited_nodes.add(neighbor)
                traversal_queue.append(neighbor)

    #   BFS differs from DFS in that it uses a queue
    #   to traverse a graph one level at a time instead
    #   drilling down levels and reversing

    return results


def main():
    print("=== UNIT 8: BREADTH-FIRST SEARCH ===")

    # ===============================
    # TODO (Student): CREATE A GRAPH
    # ===============================
    #
    # Requirements:
    # 1. Create a graph using an adjacency list.
    # 2. Include at least 6 nodes.
    # 3. Include multiple connections between nodes.
    # 4. Clearly display the graph structure.
    # 5. Use comments to explain what the nodes and edges represent.

    print("\n=== GRAPH STRUCTURE ===")
    print("TODO: Create and display a graph.")

    #   Each node represents a device or network component
    #   Each edge represents a direct network connection between
    #        two nodes. All edge connections are bidirectional
    network_graph = {
        "Internet": ["Firewall"],
        "Firewall": ["Internet", "Router1", "Router2"],
        "Router1": ["Switch1"],
        "Router2": ["Switch2"],
        "Switch1": ["Switch2", "Server1", "PC1", "Router1"],
        "Switch2": ["Switch1", "Server2", "PC2", "Router2", "Printer2"],
        "Server1": ["Switch1"],
        "Server2": ["Switch2"],
        "PC1": ["Switch1"],
        "PC2": ["Switch2"],
        "Printer2": ["Switch2"]
    }

    #   Print the above network graph/map
    print("\nGraph:")
    for node, neighbors in network_graph.items():
        print(f"{node}: {neighbors}")

    # ===============================
    # TODO (Student): BFS TRAVERSAL
    # ===============================
    #
    # Requirements:
    # 1. Select a starting node.
    # 2. Perform BFS traversal.
    # 3. Display the traversal order.
    # 4. Use comments to explain how BFS visits nodes level by level.
    # 5. Add at least one additional node or edge
    #    and demonstrate the updated traversal.

    print("\n=== BFS TRAVERSAL ===")
    print("TODO: Perform and explain BFS traversal.")

    #   Start the traversal at the top (Internet) level
    node_start = "Internet"

    #   Perform BFS search. This search should traverse
    #   the graph map one level at a time before going
    #   deeper into any given level
    traverse = bfs(network_graph, node_start)

    #   Display the order the BFS visited each
    #   level and node
    print("\nBFS Traversal:")
    print(" -> ".join(traverse))

    #   Add a monitor server node to the graph map
    #       and attach it to Switch 2
    network_graph["Switch2"].append("ServerMonitor")
    network_graph["ServerMonitor"] = ["Switch2"]

    #   Run a BFS again abd show the updated graph
    updated_traversal = bfs(network_graph, node_start)

    print("\nUpdated BFS Traversal (ServerMonitor to Switch 2:")
    print(" -> ".join(updated_traversal))


    # ===============================
    # TODO (Student): EDGE CASES
    # ===============================
    #
    # Demonstrate at least two edge cases.
    #
    # Example ideas:
    # - Start from a different node X
    # - Use a disconnected graph
    # - Handle a missing start node safely X
    # - Graph containing only one node
    # - Empty graph
    #
    # Explain what happens in each case.

    print("\n=== EDGE CASE TESTS ===")
    print("TODO: Demonstrate and explain edge cases.")

    #   Edge Case 1: Start from a different node
    #   Start from a PC node to get the traversal
    #   from an end user's perspective
    node_start = "PC1"
    traverse = bfs(network_graph, node_start)

    print("\nEdge Case 1 - BFS starting from PC1:")
    print(" -> ".join(traverse))

    #   Edge Case 2: Handle a missing start node safely
    #   Search with a start node that does not exist i.e., PC67
    node_start = "PC67"

    if node_start in network_graph:
        traversal = bfs(network_graph, node_start)
        print("\nEdge Case 2 - BFS starting from PC67:")
        print(" -> ".join(traversal))
    else:
        print("\nEdge Case 2 - Start node does not exist:")
        print(f"{node_start} is not in the graph.")


if __name__ == "__main__":
    main()