
from tkinter import Tk, BOTH, Canvas

class Window():
    def __init__(self, width, height):
        self.width = width
        self.height = height
        
        self.root = Tk()
        self.root.title("Maze solver")

        self.canvas = Canvas(self.root, width=self.width, height=self.height)
        self.canvas.pack()

        self.running = False
        self.root.protocol("WM_DELETE_WINDOW", self.close)

    def redraw(self):
        self.root.update_idletasks()
        self.root.update()

    def wait_for_close(self):
        self.running = True
        while self.running:
            self.redraw()

    def draw_line(self, line, fill_color):
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

    def draw(self, canvas, fill_color):
        x1, y1 = self.point1.x, self.point1.y
        x2, y2 = self.point2.x, self.point2.y
        canvas.create_line(x1, y1, x2, y2, fill=fill_color, width=2)

class Cell():
    def __init__(self, x1, x2, y1, y2, window):
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self._x1 = x1 # left
        self._x2 = x2 # right
        self._y1 = y1 # up
        self._y2 = y2 # down
        self._win = window

    def draw(self):
        if self.has_left_wall:
            self._win.canvas.create_line(self._x1, self._y1, self._x1, self._y2, fill="black", width=2)
        if self.has_right_wall:
            self._win.canvas.create_line(self._x2, self._y1, self._x2, self._y2, fill="black", width=2)
        if self.has_top_wall:
            self._win.canvas.create_line(self._x1, self._y1, self._x2, self._y1, fill="black", width=2)
        if self.has_bottom_wall:
            self._win.canvas.create_line(self._x1, self._y2, self._x2, self._y2, fill="black", width=2)






def main():
    win = Window(800, 600)


    cell1 = Cell(100, 100, 150, 150, win)
    cell2 = Cell(200, 100, 250, 150, win)
    cell3 = Cell(300, 100, 350, 150, win)

    cell2.has_left_wall = True  # Remove left wall
    cell3.has_top_wall = False   # Remove top wall
    cell3.has_bottom_wall = False  # Remove bottom wall


    cell1.draw()
    cell2.draw()
    cell3.draw()


    win.wait_for_close()





if __name__ == "__main__":
    main()
