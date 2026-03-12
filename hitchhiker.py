"""
Hitchhiker's Guide Challenge 🪐

Douglas Adams, author of "The Hitchhiker's Guide to the Galaxy", famously
revealed that the Ultimate Answer to Life, the Universe, and Everything is 42.

Problem:
Given a list of component values, find the minimum number of components
whose sum is exactly 42.

If it is impossible to reach exactly 42, return -1.

Each component can be used at most once.

Examples:

Input: [10, 20, 5, 15, 7]
Output: 3
Explanation: 20 + 15 + 7 = 42

Input: [1, 2, 3, 4, 5, 6]
Output: -1
Explanation: No combination sums to 42

Input: [42, 1, 1, 1]
Output: 1
Explanation: The component 42 alone powers the drive
"""

def min_components(components):
    target = 42

    # dp[i] = minimum number of components needed to reach sum i
    dp = [float('inf')] * (target + 1)
    dp[0] = 0

    for c in components:
        # iterate backwards to ensure each element is used only once
        for s in range(target, c - 1, -1):
            dp[s] = min(dp[s], dp[s - c] + 1)

    return dp[target] if dp[target] != float('inf') else -1


# Example usage
print(min_components([10, 20, 5, 15, 7]))  # 3
print(min_components([1, 2, 3, 4, 5, 6]))  # -1
print(min_components([42, 1, 1, 1]))       # 1
