import random


def generate_maze(length):
    """Return a randomly generated maze of the specified dimension (length X length).
    This maze is represented as 2D python array. The first two dimension are i, j.
    The maze returns a set() of tuples which represent that locations neighbors.

    Keyword arguments:
    length: the length of 1 side of the maze to produce a Length X Length maze
    """

    visited = set()
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    def walk(maze, cur):
        #Randomly connect this node to an unvisited neighbor.

        random.shuffle(directions)
        for dir in directions:
            n = (cur[0] + dir[0], cur[1] + dir[1])
            if (n[0] >= 0 and n[0] < len(maze)) and (n[1] >= 0 and n[1] < len(maze)) \
                    and (n not in visited):
                maze[cur[0]][cur[1]].add(n)
                maze[n[0]][n[1]].add(cur)
                visited.add(n)
                visited.add(cur)
                return n
        return None

    def hunt_walk(maze, cur):
        #Randomly connect this node to a visited neighbor.

        random.shuffle(directions)
        for dir in directions:
            n = (cur[0] + dir[0], cur[1] + dir[1])
            if (n[0] >= 0 and n[0] < len(maze)) and (n[1] >= 0 and n[1] < len(maze)) \
                    and (n in visited):
                maze[cur[0]][cur[1]].add(n)
                maze[n[0]][n[1]].add(cur)
                visited.add(cur)
                return cur
        return None

    def hunt(maze, skip_rows = 0):
        #Top->bottom left->right search for an unvisited node adjacent to a visited node
        #and connect them.


        cur = None
        for i in range(skip_rows, len(maze)): # enumerate with slice doesn't work here?
            row_count = 0
            for j, cell in enumerate(maze[i]):
                if len(cell) == 0:
                    cur = hunt_walk(maze, (i, j))
                else:
                    row_count += 1
                if cur is not None:
                    return cur, skip_rows
            if(row_count == len(maze)): # if every node in row was visited already
                skip_rows += 1
        return None, skip_rows

    #---- Method Start ----

    if(length == 0):
        return [[[]]]
    maze = [[set() for j in range(length)] for i in range(length)]
    cur, done_rows = (random.randrange(length), random.randrange(length)), 0
    while 1:
        cur = walk(maze, cur)
        if cur is None:
            cur, done_rows = hunt(maze, done_rows)
            if cur is None:
                break
    return maze