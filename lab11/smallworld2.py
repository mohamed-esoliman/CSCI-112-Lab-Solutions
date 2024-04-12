from ug import UG
import random


def small_world_graph(n, k, p):
    """create a small world graph with n nodes, k nearest neighbors, and rewiring probability p."""
    vertices = [str(i) for i in range(1, n + 1)]
    edges = []

    for i in range(n):
        for j in range(i - (k // 2), i + (k - (k // 2)) + 1):
            if i != j:
                edges.append((vertices[i], vertices[j % n], 1))

    for edge in edges:
        if random.random() < p:
            i = edge[0]
            edges.remove(edge)
            j = random.choice(vertices)
            while j == i or (i, j, 1) in edges:
                j = random.choice(vertices)
            edges.append((i, j, 1))

    print(
        f"Created a small world graph with {n} nodes, {k} nearest neighbors, and rewiring probability {p}."
    )
    return UG(vertices, edges)


def average_shortest_path_length(graph):
    """returns the average shortest path length of a graph"""
    # graph_matrix = graph.floyd()
    # total = 0
    # for i in range(len(graph_matrix)):
    #     for j in range(i):
    #         total += graph_matrix[i][j]

    # avg = total / (len(graph_matrix) * (len(graph_matrix) - 1) / 2)
    # return round(avg, 3)

    graph_matrix = graph.floyd()
    total = 0
    count = 0
    for i in graph_matrix:
        for j in i:
            if j != 0:
                total += j
                count += 1
    avg = total / count
    return round(avg, 3)


def main():
    """The main function."""
    graph1 = small_world_graph(100, 4, 0)
    print(f"Average Shortest Path Length: {average_shortest_path_length(graph1)}")
    print("-" * 25)

    graph2 = small_world_graph(100, 4, 0.5)
    print(f"Average Shortest Path Length: {average_shortest_path_length(graph2)}")
    print("-" * 25)

    graph3 = small_world_graph(100, 4, 1)
    print(f"Average Shortest Path Length: {average_shortest_path_length(graph3)}")
    print("-" * 25)


if __name__ == "__main__":
    main()
