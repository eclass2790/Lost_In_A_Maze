import random
from storage import *

def carve_passages_from(maze, row, col):
    directions = ["N", "S", "E", "W"]
    random.shuffle(directions)
    
    for d in directions:
        maze.print_maze()
        p = maze.cell_in_direction(row, col, d)

        # Check if the cell in the given direction is not outside the maze
        # and is not yet visited (not yet visited means the open directions
        # is the empty list).
        
        if p != None and maze.open_directions(p[0], p[1]) == []:
            maze.break_wall(row, col, d)
            carve_passages_from(maze, p[0], p[1])

#///the first back track occurs at the top left of the maze
#this code doesnt generate circles because of the backtracking therefore
#once you hit a wall you have to retract and go back to find a different path



# Below I have another implementation of the above function, using a
# stack instead of recursion but still working the same way.

class MazeCell:
    """
    Each entry on the stack is an instance of this class.
    It represents a cell we have visited but not yet backtracked out
    of, so stores the list of wall locations that have not yet been
    checked.
    """
    def __init__(self, r, c):
        self.row = r
        self.col = c
        self.directions = ["N", "S", "E", "W"]
        random.shuffle(self.directions)

    def pop_direction(self):
        if len(self.directions) == 0:
            return None
        else:
            return self.directions.pop()

def carve_passages_stack(maze):
    stack = []
    stack.append(MazeCell(0,0))

    while len(stack) > 0:
        # Look at the top of the stack, which is the last element in the list
        c = stack[-1]

        # Get the next wall to look at
        direction = c.pop_direction()

        if direction == None:
            # We have looked at all the walls, time to backtrack by poping the cell
            stack.pop()

        else:
            # Check the cell in the given direction
            p = maze.cell_in_direction(c.row, c.col, direction)
            if p != None and maze.open_directions(p[0], p[1]) == []:
                # Go to this cell by pushing onto the stack
                maze.break_wall(c.row, c.col, direction)
                stack.append(MazeCell(p[0], p[1]))


def random_maze(rows, cols):
    maze = Maze(rows, cols)
    carve_passages_stack(maze)
    return maze



#dead end function
def  random_maze_without_deadends(rows, cols):
    maze = random_maze(rows, cols)
    for row in range(rows):
        for col in range(cols):
            e = maze.open_directions(row,col)
            if len(e) == 1:
                walls = ['N','S','W','E'];
                boundary = []
                if row == 0:
                    walls.remove('N')
                elif row == rows -1:
                    boundary.append('S')
                if col == 0:
                    boundary.append('W')
                elif col == cols -1:
                    boundary.append('E')
                for x in boundary:
                    walls.remove(x)
                walls.remove(e[0])
                maze.break_wall(row, col, walls[0])
    return maze
#Question 1
#The maze goes into a infinte loop because since there are no deadends the path will currently
#end up in a circle causing the program constantly look for a path to solve since there are no deadends
#to break walls down.the program freezes and you must end the program


#Question 2-Extra credit
#The solution to the maze is to bring the deadends back to the program so that the  program
#can solve a solution to the maze by breaking th deadends now
    
    
if __name__ == '__main__':
    # Some test code
    m = random_maze_without_deadends(7, 7)
    m.print_maze()
