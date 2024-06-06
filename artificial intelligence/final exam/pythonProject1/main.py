class Node:

    def __init__(self, a, b, z):
        self.x = a
        self.y = b
        self.level = z

    class BFS:
        def __init__(self):
            self.directions = 4
            self.x_move = [1, -1, 0, 0]
            self.y_move = [0, 0, 1, -1]
            self.found = False
            self.goal_level = 0
            self.source = None
            self.goal = None
            self.N = 0
            self.state = 0
            self.init()

        def __int__(self):
            graph = [
                [0, 0, 1, 0, 1],
                [0, 0, 0, 0, 0],
                [0, 0, 1, 0, 1],
                [0, 0, 0, 0, 0],
                [0, 0, 1, 0, 1]
            ]
            n = len(graph)

