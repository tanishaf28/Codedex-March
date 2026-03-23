"""
Given:
A list/array kittens, where kittens[i] represents the energy level of the i-th kitten
A number limit, the biggest difference between any two kittens in a calm group

A group of kittens is calm and can purr together if:
max energy−min energy≤limit
Return the length of the longest group of consecutive kittens that can stay calm.
  
Approach: O(n) sliding window with two monotonic deques to track window `max` and `min` in O(1).
Instead of rescanning the window for min/max on every step (O(n²)), we maintain:
- `max_dq` — a **decreasing** deque; front always holds the current window max
- `min_dq` — an **increasing** deque; front always holds the current window min

When `max − min > limit`, we shrink from the left until the window is calm again.
"""

from collections import deque

def longest_calm_group(kittens, limit):
    max_dq = deque() 
    min_dq = deque()  
    left = 0
    best = 0

    for right, energy in enumerate(kittens):
        while max_dq and kittens[max_dq[-1]] <= energy:
            max_dq.pop()
        max_dq.append(right)

        while min_dq and kittens[min_dq[-1]] >= energy:
            min_dq.pop()
        min_dq.append(right)

        while kittens[max_dq[0]] - kittens[min_dq[0]] > limit:
            left += 1
            if max_dq[0] < left: max_dq.popleft()
            if min_dq[0] < left: min_dq.popleft()

        best = max(best, right - left + 1)

    return best

