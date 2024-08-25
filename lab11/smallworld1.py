import networkx as nx
import matplotlib.pyplot as plot


def small_world_graph(n, k, p):
    """create a small world graph with n nodes, k nearest neighbors, and rewiring probability p. Prints the graph."""
    graph = nx.watts_strogatz_graph(n, k, p)
    # plot.figure(figsize=(10, 10))
    # nx.draw(graph, font_size=12, node_size=100, node_color="red")
    # plot.show()

    print(
        f"Created a small world graph with {n} nodes, {k} nearest neighbors, and rewiring probability {p}."
    )
    print(
        f"Average Shortest Path Length: {round(nx.average_shortest_path_length(graph), 3)}"
    )
    # print(
    #     f"Average Clustering Coefficient: {round(nx.average_clustering(graph), 3)}",
    # )
    print("-" * 25)


def main():
    """The main function."""
    small_world_graph(100, 4, 0)
    small_world_graph(100, 4, 0.5)
    small_world_graph(100, 4, 1)


if __name__ == "__main__":
    main()
