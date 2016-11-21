import sys
from MazeTools import MazeGenerator
from queue import PriorityQueue


class Maze:

    def __init__(self, maze):

        self.maze = maze

    def is_adjacent(self, first, second):
        """
        Return true if the two locations are adjacent to each other.
        Else return false.

        :param first: a tuple (i,j) for the first location
        :param second: a tuple (i,j) for the second location
        """
        return second in self.maze[first[0]][first[1]]

    def get_neighbors(self, location):
        """Return an array of tuples that represents the given locations neighbors."""
        return self.maze[location[0]][location[1]]

    def go_direction(self, start, direction):
        """
        Return a list of tuples that represents the straight-line path of
        going right in the specified direction until hitting a wall

        :param start: a tuple (i,j) for the starting location
        """
        path = []
        while 1:
            cur = (start[0] + direction[0], start[1] + direction[1])
            if cur not in self.maze[start[0]][start[1]]:
                return path
            start = cur
            path.append(cur)

    def go_east(self, start):
        """
        Return a list of tuples that represents the straight-line path of
        going right east until hitting a wall

        :param start: a tuple (i,j) for the starting location
        """
        return self.go_direction(start, (0,1))

    def go_west(self, start):
        """
        Return a list of tuples that represents the straight-line path of
        going right west until hitting a wall

        :param start: a tuple (i,j) for the starting location
        """
        return self.go_direction(start, (0, -1))

    def go_north(self, start):
        """
        Return a list of tuples that represents the straight-line path of
        going right north until hitting a wall

        :param start: a tuple (i,j) for the starting location
        """
        return self.go_direction(start, (-1, 0))

    def go_south(self, start):
        """
        Return a list of tuples that represents the straight-line path of
        going right east until hitting a wall.

        :param start: a tuple (i,j) for the starting location
        """
        return self.go_direction(start, (1, 0))

    def path_to(self, start, end):
        """
        Dijkstra's search for shortest path from start tuple to end tuple.
        :param start: tuple to start
        :param end: Tuple to end
        :return: Array of tuples not including starting location but including ending location
        """
        visited = set()
        dist = {start:0}
        prev_list = {}
        queue = PriorityQueue()

        queue.put((0, start)) # dijkstra's
        while queue is not queue.empty():
            cur = queue.get()[1]
            if(cur == end):
                break
            for neighbor in self.maze[cur[0]][cur[1]]:
                cur_distance = dist[cur] + 1
                neighbor_distance =  dist[neighbor] if (neighbor in dist) else sys.maxsize
                if cur_distance < neighbor_distance:
                    dist[neighbor] = cur_distance
                    prev_list[neighbor] = cur
                    queue.put((cur_distance, neighbor))

        path = [] #constuct path
        prev = end
        while 1:
            if(prev == start):
                break
            path.insert(0,prev)
            prev = prev_list[prev]

        return path

    def __str__(self):

        str = ""
        for row in self.maze:  # top of maze
            str += " _"
        str += "\n"
        # We only need to do one side of each connection: so start in top-left look east&south.
        for i, row in enumerate(self.maze):
            str += "|"  # left of maze
            for j, cell in enumerate(row):
                if (i + 1, j) in cell:
                    str += " "
                else:
                    str += "_"
                if (i, j + 1) in cell:
                    str += " "
                else:
                    str += "|"
            str += "\n"
        return str


def make_maze(length):  # is this kind of method pythonic?
    """
    Factory method for making mazes that are already pre-generated at the specified size

    :param length: the dimensions of the maze (length X length)
    :return: Maze Object
    """
    return Maze(MazeGenerator.generate_maze(length))