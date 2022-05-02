import unittest

import numpy as np
from occupancy_grid import OccupancyGrid

# define a testcase for occupancy grid
class TestOccupancyGrid(unittest.TestCase):
    def testCreation(self):
        grid = OccupancyGrid(cell_size=0.1, x_cells=10, y_cells=10)
        self.assertEqual(grid.get_cell_size(), 0.1)
        self.assertEqual(grid.get_x_cells(), 10)
        self.assertEqual(grid.get_y_cells(), 10)
        self.assertTrue(np.array_equal(grid.get_grid(), np.zeros((10, 10), dtype=np.int8)))


if __name__ == "__main__":
    unittest.main()