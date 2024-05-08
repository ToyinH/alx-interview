# Island Perimeter

## Description
This project contains a Python function to calculate the perimeter of an island represented by a grid of 0s and 1s.

## Functionality
The function `island_perimeter(grid)` takes a grid as input and returns the perimeter of the island described in the grid.

- `grid` is a list of lists of integers where:
  - 0 represents water
  - 1 represents land
- Each cell is square, with a side length of 1
- Cells are connected horizontally/vertically (not diagonally)
- The grid is completely surrounded by water
- There is only one island (or nothing)
- The island doesn’t have “lakes” (water inside that isn’t connected to the water surrounding the island)

