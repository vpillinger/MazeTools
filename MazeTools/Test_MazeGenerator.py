import unittest
from collections import deque

from MazeTools import MazeGenerator


class MazeGeneratorTest(unittest.TestCase):

    # Size & Length Tests
    def test_size_0(self):
        """Test whether generate_maze returns an empty numpy array on size 0"""

        maze = MazeGenerator.generate_maze(0)
        self.assertEqual(1, len(maze))
        self.assertEqual(1, len(maze[0]))
        self.assertEqual(0, len(maze[0][0]))

    def test_size(self):
        """Test whether generate_maze returns a numpy array of the proper size
        and dimensions for several inputs"""

        lengths = [1,5,10]
        for i in lengths:
            maze = MazeGenerator.generate_maze(i)
            self.assertEqual(i, len(maze))
            self.assertEqual((i), len(maze[0]))

    # Graph completeness tests
    def bfs(self, maze):
        # return the number of visited nodes from a bfs

        directions = (-1, 0), (0, 1), (1, 0), (0, -1)
        q = deque()
        visited = set()
        q.append((0,0))
        while q:
            # pop to visited
            current = q.popleft()
            visited.add(current)
            # add neighbors to queue
            for neighbor in maze[current[0]][current[1]]:
                if neighbor not in visited:
                    q.append(neighbor)
        return len(visited)

    def test_completeness(self):
        """Use Breadth-First-Search to test that maze graph is complete (all nodes connected)
        The number of visited nodes should be equal to the maze's size"""

        for length in [1, 5, 20, 50, 100]:
            maze = MazeGenerator.generate_maze(length)
            self.assertEqual(len(maze) ** 2, self.bfs(maze))

if __name__ == '__main__':
    unittest.main()
