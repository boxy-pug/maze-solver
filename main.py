
from tkinter import Tk, BOTH, Canvas
import time

class Window():
    def __init__(self, width, height):
        
        self.root = Tk()
        self.root.title("Maze solver")

        self.canvas = Canvas(self.root, bg="white", width=width, height=height)
        self.canvas.pack(fill=BOTH, expand=1)

        self.running = False
        self.root.protocol("WM_DELETE_WINDOW", self.close)

    def redraw(self):
        self.root.update_idletasks()
        self.root.update()

    def wait_for_close(self):
        self.running = True
        while self.running:
            self.redraw()
        print("Window closed.")

    def draw_line(self, line, fill_color="black"):
        line.draw(self.canvas, fill_color)

    def close(self):
        self.running = False


class Point():
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

class Line():
    def __init__(self, point1, point2):
        self.point1 = point1
        self.point2 = point2

    def draw(self, canvas, fill_color="black"):
        x1, y1 = self.point1.x, self.point1.y
        x2, y2 = self.point2.x, self.point2.y
        canvas.create_line(x1, y1, x2, y2, fill=fill_color, width=2)

class Cell():
    def __init__(self, window=None):
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self._x1 = None# left
        self._x2 = None# right
        self._y1 = None# up
        self._y2 = None# down
        self._win = window

    def draw(self, x1, x2, y1, y2):
        self._x1 = x1 # left
        self._x2 = x2 # right
        self._y1 = y1 # up
        self._y2 = y2 # down
        if self.has_left_wall:
            self._win.draw_line(Line(Point(x1, y1), Point(x1, y2)))
        if self.has_right_wall:
            self._win.draw_line(Line(Point(x2, y1), Point(x2, y2)))
        if self.has_top_wall:
            self._win.draw_line(Line(Point(x1, y1), Point(x2, y1)))
        if self.has_bottom_wall:
            self._win.draw_line(Line(Point(x1, y2), Point(x2, y2)))

    def draw_move(self, to_cell, undo=False):
        fill = "gray"
        if not undo:
            self.fill = "red"

        from_x = (self._x1 + self._x2) / 2
        from_y = (self._y1 + self._y2) / 2

        to_x = (to_cell._x1 + to_cell._x2) / 2
        to_y = (to_cell._y1 + to_cell._y2) / 2

        self._win.draw_line(Line(Point(from_x, from_y), Point(to_x, to_y)), fill)

class Maze():
    def __init__(self, x1, y1, num_rows, num_cols, cell_size_x, cell_size_y, window=None):
        self.x1 = x1
        self.y1 = y1
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.cell_size_x = cell_size_x
        self.cell_size_y = cell_size_y
        self.win = window
        self._create_cells()

    def _create_cells(self):
        self._cells = []
        for i in range(self.num_rows):
            row = []
            for j in range(self.num_cols):
                cell = self._draw_cell(i, j)
                row.append(cell)
            self._cells.append(row)

    def _draw_cell(self, i, j):
        if self.win is None:
            return
        x1 = self.x1 + j * self.cell_size_x
        y1 = self.y1 + i * self.cell_size_y
        x2 = x1 + self.cell_size_x
        y2 = y1 + self.cell_size_y
        cell = Cell(self.win)
        cell.draw(x1, y1, x2, y2)
        self._animate()
        return cell


    def _animate(self):
        self.win.redraw()
        time.sleep(0.1)
        

def main():
    win = Window(800, 600)
    """
    maze = Maze(50, 50, 5, 5, 50, 50, win)

    l = Line(Point(50, 50), Point(100, 100))
    win.draw_line(l, "black")

    c1 = Cell(win)
    c1.has_left_wall = True
    c1.draw(50, 100, 50, 100)

    c2 = Cell(win)
    c2.has_right_wall = True
    c2.draw(125, 200, 125, 200)

    c3 = Cell(win)
    c3.has_bottom_wall = False
    c3.draw(225, 225, 250, 250)

    c4 = Cell(win)
    c4.has_top_wall = False
    c4.draw(300, 300, 500, 500)

    # Draw a move from cell1 to cell2
    c1.draw_move(c2, undo=False)

    # Draw a backtrack move from cell2 to cell1
    c2.draw_move(c1, undo=True)
    """


    win.wait_for_close()



if __name__ == "__main__":
    main()

