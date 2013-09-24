from generate import *

class MazeCell:
    """
    Each entry on the stack is an instance of this class.
    It represents a cell we have visited but not yet backtracked out
    of, so stores the list of open passages that have not yet been
    checked.
    """
    def __init__(self, maze, point):
        self.point = point
        self.directions = maze.open_directions(point[0], point[1])

    def pop_direction(self):
        if len(self.directions) == 0:
            return None
        else:
            return self.directions.pop()

    def remove_opposite(self, direction):
        """Remove the opposite of the given direction from the list of open directions"""
        opposites = {"N" : "S", "S" : "N", "E" : "W", "W" : "E"}
        self.directions.remove(opposites[direction])

def solve_maze(maze, start=None, end=None):
    """
    Solves a maze finding a path between start and end.  If start and
    end are not given, it finds a path between (0,0) and (maze.rows-1,maze.cols-1)
    """

    if start == None:
        start = (0,0)
    if end == None:
        end = (maze.rows-1, maze.cols-1)

    # Start with the start cell on the stack
    stack = []
    stack.append(MazeCell(maze, start))

    while len(stack) > 0:
        # Look at the top of the stack, which is the last element in the list
        c = stack[-1]

        # Get the next passage to look at
        direction = c.pop_direction()

        if direction == None:
            # We have looked at all the open passages, time to backtrack by poping the cell
            stack.pop()

        else:
            p = maze.cell_in_direction(c.point[0], c.point[1], direction)

            # If this is the end, we have found the path
            if p == end:
                # The path consists of all the cells on the stack
                solution = []
                for c in stack:
                    solution.append(c.point)
                # Plus the end cell
                solution.append(p)
                return solution

            # Otherwise, move to the cell in the given direction
            n = MazeCell(maze, p)
            # Remove the direction we just came from from the list of open passages
            n.remove_opposite(direction)
            stack.append(n)

    # Backtracked all the way to the start without finding the end, so this maze
    # has no solution.
    return None


# Some test code
if __name__ == '__main__':
    m = random_maze(10, 10)
    m.print_maze()
    print solve_maze(m)
