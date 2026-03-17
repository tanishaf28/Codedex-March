"""
## ☘️ Green River Drift — Approach

This problem can be modeled as a **rightward propagation process** on a 1D array.

### Key Idea
Each ☘️ at index `j` influences positions to its right up to distance `hours`.  
So a position `i` becomes ☘️ if there exists some `j ≤ i` such that:

    i - j ≤ hours

### Optimized Strategy (O(n))
Instead of simulating hour-by-hour, we track the **most recent ☘️ seen so far** while scanning left → right.

- Maintain `last_clover` (index of last ☘️)
- For each position `i`:
  - If current cell is ☘️ → update `last_clover = i`
  - If `i - last_clover ≤ hours` → mark as ☘️
  - Else → 💧

"""

def green_river(river, hours):
    result = ['💧'] * len(river)
    last_clover = float('-inf')
    
    for i in range(len(river)):
        if river[i] == '☘️':
            last_clover = i
        
        if i - last_clover <= hours:
            result[i] = '☘️'
    
    return result
