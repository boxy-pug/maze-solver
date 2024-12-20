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


if __name__ == "__main__":
    unittest.main()
