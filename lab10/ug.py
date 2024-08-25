import math


class UG:
    """represent an undirected graph"""

    def __init__(self, vertices=None, edges=None):
        """initializes a UG with a set of vertices and edges"""
        self.dict = {v: {} for v in vertices}
        for i, j, w in edges:
            self.dict[i][j] = w
            self.dict[j][i] = w

    def __len__(self):
        """returns the number of vertices in the UG"""
        return len(self.dict)

    def formatter(dict):
        """returns a formatted string representation of a dictionary"""
        matrix = "     "
        for v in dict:
            matrix += "%4s" % v + " "
        matrix += "\n"

        for v in dict:
            matrix += "%4s" % v + " "
            for w in dict:
                if w == v:
                    matrix += "%4.0f" % 0 + " "
                elif w not in dict[v]:
                    # matrix += "%4.0f" % math.inf + " "
                    matrix += "%4s" % "-" + " "
                else:
                    matrix += "%4.0f" % dict[v][w] + " "
            matrix += "\n"

        return matrix

    def __str__(self):
        """returns a string representation of the UG"""
        return UG.formatter(self.dict)

    def floyd(self):
        """returns a dictionary of shortest paths between all vertices"""
        floyd_dict = self.dict.copy()
        for v in floyd_dict:
            for w in floyd_dict:
                if w not in floyd_dict[v]:
                    floyd_dict[v][w] = math.inf
                if v == w:
                    floyd_dict[v][w] = 0

        for i in floyd_dict:
            for r in floyd_dict:
                for c in floyd_dict:
                    floyd_dict[r][c] = min(
                        floyd_dict[r][c], floyd_dict[r][i] + floyd_dict[i][c]
                    )

        return UG.formatter(floyd_dict)


def main():
    """The main function."""
    ug = UG(
        ("A", "B", "C", "D", "E", "F", "G", "H", "I", "J"),
        (
            ("A", "D", 462),
            ("A", "F", 451),
            ("A", "G", 366),
            ("B", "C", 92),
            ("B", "D", 98),
            ("B", "E", 86),
            ("B", "F", 79),
            ("C", "E", 99),
            ("D", "E", 61),
            ("D", "G", 82),
            ("E", "G", 70),
            ("F", "G", 50),
            ("G", "H", 73),
            ("G", "J", 90),
            ("G", "I", 389),
            ("H", "I", 80),
            ("H", "J", 250),
            ("I", "J", 97),
        ),
    )
    print("Part I: UG basics ------------")
    print(ug)

    print("\n\nPart II: Floyd algorithm ------------\n")
    print(ug.floyd())


if __name__ == "__main__":
    main()
