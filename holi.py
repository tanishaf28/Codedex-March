"""
🌈 Holi Festival Grid Challenge 🌈

Problem:
We are given a 7x7 grid representing an area covered in Holi powders.
Each cell contains one emoji representing a color from the list:

["🟥", "🟧", "🟨", "🟩", "🟦", "🟪", "🟫"]

Some colors may be missing from the grid.

Task:
Write a function `find_missing_colors(grid)` that:
- Takes a 2D list (7x7 grid) of emoji strings.
- Returns a list of emojis that are missing from the grid.
- The missing emojis must be returned in the same order as the original color list.

------------------------------------------------------------
 Approach:

1. Store all possible Holi colors in a list called `all_colors`.
2. Traverse the 2D grid row by row.
3. Add every color found into a set called `found_colors`.
   (Using a set ensures uniqueness and allows fast lookup.)
4. Compare `all_colors` with `found_colors`.
5. Any color not present in `found_colors` is added to the `missing` list.
6. Return the `missing` list.

------------------------------------------------------------
Key Concepts Used:
- 2D list traversal
- Nested loops
- Set for fast membership checking
- Order-preserving comparison

Time Complexity:
O(n²) for traversing the grid (n = grid size)
Comparison step is O(1) since color list size is constant (7)

"""


def find_missing_colors(grid):
  # Write code below 💖
  all_colors=["🟥", "🟧", "🟨", "🟩", "🟦", "🟪", "🟫"]
  found_colors = set()
    
  # Traverse 2D grid
  for row in grid:
      for color in row:
          found_colors.add(color)
    
  # Find missing colors
  missing = []
  for color in all_colors:
      if color not in found_colors:
        missing.append(color)
    
  return missing
