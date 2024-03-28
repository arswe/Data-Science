from collections import deque


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

    def init(self):
        graph = [
            [0, 0, 1, 0, 1],
            [0, 1, 1, 1, 1],
            [0, 1, 0, 0, 1],
            [1, 1, 0, 1, 1],
            [1, 0, 0, 0, 1]
        ]
        self.N = len(graph)
        source_x, source_y = 0, 2
        goal_x, goal_y = 4, 4
        self.source = Node(source_x, source_y, 0)
        self.goal = Node(goal_x, goal_y, float('inf'))
        self.st_bfs(graph)
        if self.found:
            print("Goal found")
            print("Number of moves required =", self.goal_level)
        else:
            print("Goal can not be reached from starting block")

    def st_bfs(self, graph):
        q = deque()
        q.append(self.source)

        while q:
            u = q.popleft()

            for j in range(self.directions):
                v_x = u.x + self.x_move[j]
                v_y = u.y + self.y_move[j]

                if (0 <= v_x < self.N) and (0 <= v_y < self.N) and graph[v_x][v_y] == 1:
                    v_level = u.level + 1

                    if v_x == self.goal.x and v_y == self.goal.y:
                        self.found = True
                        self.goal_level = v_level
                        self.goal.level = v_level
                        return

                    graph[v_x][v_y] = 0
                    child = Node(v_x, v_y, v_level)
                    q.append(child)


b = BFS()
