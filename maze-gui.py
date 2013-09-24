from Tkinter import *
from maze import *

class MazeGui:
    def __init__(self, root, maze_size = 800):
        root.title("Maze")

        self.maze_size = maze_size

        rlabel = Label(root, text="Rows:")
        rlabel.grid(row=0,column=0)

        self.rowbox = Spinbox(root, from_=10, to=100)
        self.rowbox.grid(row=0, column=1)

        clabel = Label(root, text="Cols:")
        clabel.grid(row=0, column=2)

        self.colbox = Spinbox(root, from_=10, to=100)
        self.colbox.grid(row=0,column=3)

        generate = Button(root, text="Generate", command=self.generate)
        generate.grid(row=0, column=4)

        solve = Button(root, text="Solve", command=self.solve)
        solve.grid(row=0, column=5)

        self.canvas = Canvas(root, width=maze_size + 20, height=maze_size + 20, bg='white')
        self.canvas.grid(row=1, column=0, columnspan=6)

    def generate(self):
        rows = int(self.rowbox.get())
        cols = int(self.colbox.get())
        self.maze = random_maze(rows, cols)
        self.draw(self.maze)

    def draw(self, maze):
        self.canvas.delete(ALL)

        # Upper-Left corner of the maze is at (10,10)
        startx = 10
        starty = 10

        # Size of the cell
        xcellsize = self.maze_size / maze.cols
        ycellsize = self.maze_size / maze.rows

        # Draw the border of the maze
        self.canvas.create_rectangle(startx, starty, \
                startx + maze.cols * xcellsize, \
                starty + maze.rows * ycellsize)

        # For each cell, draw the north and west walls
        for r in range(maze.rows):
            for c in range(maze.cols):
                
                # Compute coordinate of the upper-left corner of the cell
                x = startx + c * xcellsize
                y = starty + r * ycellsize
        
                open_dirs = maze.open_directions(r, c)

                if "N" not in open_dirs:
                    self.canvas.create_line( (x,y), (x+xcellsize, y))
                if "W" not in open_dirs:
                    self.canvas.create_line( (x,y), (x, y + ycellsize))

    def center_of_cell(self, cell):
        """Returns the canvas coordinates of the center of a cell"""
        row = cell[0]
        col = cell[1]
        xcellsize = self.maze_size / self.maze.cols
        ycellsize = self.maze_size / self.maze.rows
        return (10 + xcellsize * col + xcellsize/2, 10 + ycellsize * row + ycellsize / 2)

    def solve(self):
        path = solve_maze(self.maze)
        points = map(self.center_of_cell, path)
        self.canvas.create_line(points, fill="red")

root = Tk()
MazeGui(root)
root.mainloop()
