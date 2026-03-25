"""
⚾ Opening Day Challenge: Longest Winning Strea*

### 🧩 Problem
Given a list of game results, return the **longest winning streak**.
Each game is:
* `"W"` → Win
* `"L"` → Loss (breaks streak)
* `"R"` → Rainout (does NOT break streak, but doesn’t count as a win)

### 📥 Input
An array like:["W", "W", "R", "W", "W", "L", "W"]

### 📤 Output:4
Can you handle the rain and still track the heat? 🔥⚾
"""

def streak_counter(games):
    maxstreak = 0
    current = 0

    for game in games:
        if game == "W":
            current += 1
        elif game == "L":
            current = 0
        maxstreak = max(maxstreak, current)

    return maxstreak
