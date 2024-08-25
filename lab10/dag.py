from my_stack import Stack


class DAG:
    """represents a directed acyclic graph (DAG)"""

    def __init__(self, vertices=None, edges=None):
        """initializes a DAG with a set of vertices and edges"""
        self.dict = {v: [] for v in vertices}
        for i, j in edges:
            self.dict[i].append(j)

    def __len__(self):
        """returns the number of vertices in the DAG"""
        return len(self.dict)

    def __str__(self):
        """returns a string representation of the DAG"""
        return str(self.dict)

    def bfs(self):
        """returns a list of vertices in breadth-first search order"""
        visited_vertices = []

        processing_list = [list(self.dict)[0]]
        while len(processing_list) > 0:
            item = processing_list.pop(0)
            visited_vertices.append(item)
            processing_list = processing_list + self.dict[item]

        return visited_vertices

    def dfs(self):
        """returns a list of vertices in depth-first search order"""
        visited_vertices = []

        processing_list = [list(self.dict)[0]]
        while len(processing_list) > 0:
            item = processing_list.pop(0)
            visited_vertices.append(item)
            processing_list = self.dict[item] + processing_list

        return visited_vertices

    def topologicalSort(self):
        """returns a list of vertices after being sorted"""

        visited_vertices = []

        def dfs(v, sorted_vertices):
            visited_vertices.append(v)

            for w in self.dict[v]:
                if w not in visited_vertices:
                    dfs(w, sorted_vertices)

            sorted_vertices.push(v)

        sorted_vertices = Stack()
        for v in list(self.dict):
            if v not in visited_vertices:
                dfs(v, sorted_vertices)

        return sorted_vertices


def main():
    print("Part I: DAG basics ------------")
    dag = DAG(("a", "b", "c"), (("a", "b"), ("a", "c")))
    print(len(dag))
    print(dag)

    print("\nPart II: search ------------")
    dag = DAG(
        (1, 2, 3, 4, 5, 6, 7, 8),
        ((1, 2), (1, 3), (1, 4), (2, 5), (2, 6), (4, 7), (6, 8)),
    )
    print(dag)
    print("BFS: " + str(dag.bfs()))
    print("DFS: " + str(dag.dfs()))

    print("\nPart III: Topological sort ------------")
    dag = DAG(
        (
            "MATH121",
            "CSCI111",
            "CSCI112",
            "CSCI209",
            "CSCI210",
            "CSCI211",
            "CSCI312",
            "CSCI313",
        ),
        (
            ("CSCI111", "CSCI210"),
            ("CSCI111", "CSCI112"),
            ("MATH121", "CSCI211"),
            ("MATH121", "CSCI312"),
            ("CSCI312", "CSCI312"),
            ("CSCI112", "CSCI210"),
            ("CSCI112", "CSCI209"),
            ("CSCI112", "CSCI211"),
            ("CSCI312", "CSCI313"),
        ),
    )
    print(dag.topologicalSort())


if __name__ == "__main__":
    main()
