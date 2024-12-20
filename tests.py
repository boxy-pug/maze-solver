import unittest
from main import Maze


class Tests(unittest.TestCase):
    def test_maze_create_cells(self):
        num_cols = 14
        num_rows = 13
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        self.assertEqual(
            len(m1._cells),
            num_rows,
        )
        self.assertEqual(
            len(m1._cells[0]),
            num_cols,
        )

    def test_maze_different_dimensions(self):
        test_cases = [(5, 5), (1, 1), (1, 2), (30, 20), (0, 0), (0, 10), (10, 0)]
        for num_rows, num_cols in test_cases:
            with self.subTest(num_rows=num_rows, num_cols=num_cols):
                m = Maze(0, 0, num_rows, num_cols, 10, 10)
                self.assertEqual(len(m._cells), num_rows)
                if num_rows > 0:
                    self.assertEqual(len(m._cells[0]), num_cols)

    def test_empty_maze(self):
        m = Maze(0, 0, 0, 0, 10, 10)
        self.assertEqual(len(m._cells), 0)


if __name__ == "__main__":
    unittest.main()
