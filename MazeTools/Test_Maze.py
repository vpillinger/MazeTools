import unittest
from MazeTools import Maze


class MazeTest(unittest.TestCase):

    def test_init_maze(self):
        self.assertEquals(self.pre_made_maze, self.maze.maze)

    def test_make_maze(self):
        maze = Maze.make_maze(10)
        self.assertEquals(10, len(maze.maze))

    def test_is_adjacent_returns_false_when_not_adjacent(self):
        self.assertEquals(False, self.maze.is_adjacent((1, 0), (0, 1)))

    def test_is_adjacent_returns_true_when_adjacent(self):
        self.assertEquals(True, self.maze.is_adjacent((0, 0), (0, 1)))

    def test_get_neighbors_returns_all_neighbors(self):
        self.assertEquals({(1, 0), (0, 1)}, self.maze.get_neighbors((0,0)))

    def test_go_east_should_return_path(self):
        path = self.maze.go_east((0, 0))
        self.assertEquals([(0, 1), (0, 2), (0, 3)], path)

    def test_go_east_into_wall_should_return_empty_path(self):
        path = self.maze.go_east((0, 3))
        self.assertEquals([], path)

    def test_go_west_should_return_path(self):
        path = self.maze.go_west((0, 3))
        self.assertEquals([(0, 2), (0, 1), (0, 0)], path)

    def test_go_west_into_wall_should_return_empty_path(self):
        path = self.maze.go_west((0, 0))
        self.assertEquals([], path)

    def test_go_north_should_return_path(self):
        path = self.maze.go_north((9, 0))
        self.assertEquals([(8, 0), (7, 0), (6, 0)], path)

    def test_go_north_into_wall_should_return_empty_path(self):
        path = self.maze.go_north((0, 0))
        self.assertEquals([], path)

    def test_go_south_should_return_path(self):
        path = self.maze.go_south((6, 0))
        self.assertEquals([(7, 0), (8, 0), (9, 0)], path)

    def test_go_south_into_wall_should_return_empty_path(self):
        path = self.maze.go_south((9, 0))
        self.assertEquals([], path)

    def test_path_to_same_space_returns_empty_list(self):
        self.assertEquals([], self.maze.path_to((0, 0), (0, 0)))

    def test_path_to_space_distance_1_away(self):
        self.assertEquals([(0,1)], self.maze.path_to((0, 0), (0, 1)))

    def test_path_to_returns_shortest_path(self):
        self.assertEquals([(1, 0), (2, 0), (2, 1), (1, 1), (1, 2)],
                          self.maze.path_to((0, 0), (1, 2)))

    def setUp(self):
        self.pre_made_maze = [[{(0, 1), (1, 0)}, {(0, 2), (0, 0)}, {(0, 3), (0, 1)}, {(1, 3), (0, 2)}, {(0, 5), (1, 4)}, {(0, 6), (0, 4), (1, 5)}, {(0, 7), (0, 5)}, {(0, 8), (0, 6)}, {(0, 7), (1, 8)}, {(1, 9)}],
                [{(0, 0), (2, 0)}, {(2, 1), (1, 2)}, {(1, 1), (2, 2)}, {(1, 4), (0, 3)}, {(0, 4), (1, 3)}, {(0, 5), (1, 6)}, {(1, 5), (2, 6), (1, 7)}, {(1, 6), (2, 7)}, {(0, 8), (1, 9)}, {(1, 8), (2, 9), (0, 9)}],
                [{(1, 0), (2, 1)}, {(2, 0), (1, 1)}, {(1, 2), (3, 2)}, {(2, 4), (3, 3)}, {(2, 5), (2, 3)}, {(3, 5), (2, 4)}, {(1, 6), (3, 6)}, {(1, 7), (2, 8)}, {(2, 7)}, {(1, 9), (3, 9)}],
                [{(4, 0)}, {(3, 2), (4, 1)}, {(2, 2), (3, 1)}, {(2, 3), (3, 4)}, {(3, 3), (4, 4)}, {(3, 6), (2, 5)}, {(2, 6), (3, 5)}, {(3, 8), (4, 7)}, {(3, 9), (3, 7)}, {(2, 9), (3, 8)}],
                [{(5, 0), (3, 0)}, {(3, 1), (4, 2)}, {(4, 1), (5, 2)}, {(4, 4), (5, 3)}, {(3, 4), (4, 3)}, {(5, 5), (4, 6)}, {(4, 5), (5, 6)}, {(3, 7), (5, 7), (4, 8)}, {(4, 7), (4, 9)}, {(4, 8), (5, 9)}],
                [{(5, 1), (4, 0)}, {(5, 2), (5, 0)}, {(4, 2), (5, 1)}, {(4, 3), (5, 4)}, {(5, 3), (5, 5)}, {(5, 4), (4, 5)}, {(4, 6), (6, 6)}, {(4, 7), (6, 7)}, {(5, 9)}, {(4, 9), (6, 9), (5, 8)}],
                [{(6, 1), (7, 0)}, {(6, 2), (6, 0)}, {(6, 3), (6, 1)}, {(7, 3), (6, 2)}, {(6, 5), (7, 4)}, {(7, 5), (6, 4)}, {(5, 6)}, {(5, 7), (7, 7)}, {(6, 9), (7, 8)}, {(5, 9), (6, 8)}],
                [{(6, 0), (8, 0)}, {(8, 1), (7, 2)}, {(7, 1), (7, 3)}, {(7, 2), (6, 3)}, {(6, 4), (8, 4)}, {(7, 6), (6, 5)}, {(8, 6), (7, 5)}, {(6, 7), (8, 7)}, {(6, 8), (8, 8)}, {(8, 9)}],
                [{(7, 0), (9, 0)}, {(8, 2), (7, 1)}, {(9, 2), (8, 1)}, {(8, 4)}, {(7, 4), (8, 5), (8, 3)}, {(8, 4), (9, 5)}, {(8, 7), (7, 6)}, {(7, 7), (8, 6)}, {(7, 8), (9, 8)}, {(9, 9), (7, 9)}],
                [{(8, 0), (9, 1)}, {(9, 0)}, {(9, 3), (8, 2)}, {(9, 4), (9, 2)}, {(9, 5), (9, 3)}, {(8, 5), (9, 4), (9, 6)}, {(9, 5), (9, 7)}, {(9, 6)}, {(8, 8), (9, 9)}, {(9, 8), (8, 9)}]]

        self.maze = Maze.Maze(self.pre_made_maze)

if __name__ == '__main__':
    unittest.main()
