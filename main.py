
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




def main():
    win = Window(800, 600)


    p1 = Point(100, 100)
    p2 = Point(200, 200)
    p3 = Point(300, 100)
    p4 = Point(400, 200)


    line1 = Line(p1, p2)
    line2 = Line(p3, p4)


    win.draw_line(line1, "black")
    win.draw_line(line2, "red")
    win.wait_for_close()





if __name__ == "__main__":
    main()
