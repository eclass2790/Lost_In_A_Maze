import numpy

class Maze:
    def __init__(self, rows, cols):

        self.rows = rows
        self.cols = cols

        # Create a numpy matrix initialized to zero so all cells have walls between them.
        self.M = numpy.zeros((rows,cols),int)

    def open_directions(self, r, c):
        """
        Returns a list of open (non-wall) directions from the cell given by row r and column c
        """
        dirs = []
        val = self.M[r,c]
        
        # Test if the 4th bit is set by ANDING with 1000.  The result of the AND will
        # either be 0000 or 1000 (8 in decimal).
        if val & int('1000', 2) != 0:
            # This means the 4th bit is non-zero, i.e. non-wall
            dirs.append("N")

        if val & int('0100', 2) != 0:
            # 3rd bit is non-zero
            dirs.append("E")

        if val & int('0010', 2) != 0:
            # 2nd bit is non-zero
            dirs.append("S")

        if val & int('0001', 2) != 0:
            dirs.append("W")

        return dirs

    def cell_in_direction(self, r, c, direction):
        """
        Returns the coordinates of the cell in the given direction from (r,c).
        Returns None if the direction from (r,c) is outside the maze.
        """
        rowchange = { "N": -1, "S": 1, "E": 0, "W": 0}
        colchange = { "N": 0,  "S": 0, "E": 1, "W": -1}
        r2 = r + rowchange[direction]
        c2 = c + colchange[direction]

        # Check the new cell is within the bounds.  If not, return.
        if r2 < 0 or r2 >= self.rows or c2 < 0 or c2 >= self.cols:
            return None
        else:
            return (r2, c2)

    def break_wall(self, r, c, direction):
        """
        Breaks a wall between the cell given by row r and column c in direction.
        Direction should be a string "N", "E", "S", "W".
        """

        r2, c2 = self.cell_in_direction(r, c, direction)

        opposite = {"N":"S", "S":"N", "E":"W", "W":"E"}

        # Remove the wall from (r,c) and from (r2,c2)
        self._remove_wall_from_cell(r, c, direction)
        self._remove_wall_from_cell(r2, c2, opposite[direction])

    def _remove_wall_from_cell(self, r, c, direction):
        """
        Internal method which updates the matrix to remove the wall in the given direction.
        """
        val = self.M[r, c]
        if direction == "N":
            # We need to change the 4th bit from zero to 1.  To do that, we use a bitwise OR
            # between the value and the number 1000 in binary.  Since (b OR 1 = 1) the fourth
            # bit will be one.  Also, (b OR 0 = b) so the other bits will not change.
            val |= int('1000', 2)
        elif direction == "E":
            val |= int('0100', 2)
        elif direction == "S":
            val |= int('0010', 2)
        elif direction == "W":
            val |= int('0001', 2)

        self.M[r, c] = val

    def print_maze(self):
        # Some print code which I have here for testing
        print " " + "_" * (2*self.cols - 1)
        for row in range(self.rows):
            txt = "|"
            for col in range(self.cols):
                open_dirs = self.open_directions(row, col)
                if "S" in open_dirs:
                    txt += " "
                else:
                    txt += "_"
                if "E" in open_dirs:
                    if "S" in open_dirs or "S" in self.open_directions(row, col+1):
                        txt += " "
                    else:
                        txt += "_"
                else:
                    txt += "|"
            print txt
                    

if __name__ == '__main__':
    # Some test code
    m = Maze(10, 10)
    print m.open_directions(3, 3)
    m.break_wall(3, 3, "N")
    print m.M
    m.print_maze()
    print "(3,3) = %s" % m.open_directions(3, 3)
    print "(2,3) = %s" % m.open_directions(2, 3)

    m.break_wall(3, 3, "E")
    print m.M
    m.print_maze()
    print "(3,3) = %s" % m.open_directions(3, 3)
    print "(2,3) = %s" % m.open_directions(3, 4)

    m.break_wall(3, 2, "E")
    m.print_maze()
    print "(3,3) = %s" % m.open_directions(3, 3)
