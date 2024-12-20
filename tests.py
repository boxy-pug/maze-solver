import unittest
from main import * 


class Tests(unittest.TestCase):
    def test_maze_create_cells(self):
        num_cols = 12
        num_rows = 10
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        self.assertEqual(
            len(m1._cells),
            num_cols,
        )
        self.assertEqual(
            len(m1._cells[0]),
            num_rows,
        )
    def test_maze_different_dimensions(self):
        test_cases = [(5, 5), (1, 1), (1, 2), (30, 20), (1, 10), (10, 1)]
        for num_rows, num_cols in test_cases:
            with self.subTest(num_rows=num_rows, num_cols=num_cols):
                m = Maze(0, 0, num_rows, num_cols, 10, 10)
                self.assertEqual(len(m._cells), num_cols)
                if num_rows > 0:
                    self.assertEqual(len(m._cells[0]), num_rows)

    def test_empty_maze(self):
        m = Maze(0, 0, 0, 0, 10, 10)
        self.assertEqual(len(m._cells), 0)

    """    
    def test_break_entrance_and_exit(self):
        num_rows = 10
        num_cols = 8
        m = Maze(0, 0, num_rows, num_cols, 10, 10)
        self.assertFalse(m._cells[0][0].has_top_wall)
    """
if __name__ == "__main__":
    unittest.main()
