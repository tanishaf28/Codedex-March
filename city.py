"""
A dangerous virus is spreading across a city. So it goes... 🦠

Each day, infected people pass the virus to nearby healthy people. Your goal is to determine how many days it takes to infect everyone... or if it’s impossible.

Given a grid representing a city:

' ' = empty space
'👤' = healthy person
'🧟' = infected person
Each day, any infected person '🧟' infects adjacent healthy folks '👤' (up, down, left, right).

Complete the function and return:

The minimum number of days needed to infect all people.
OR -1 if some people can never be infected.
"""
from collections import deque

def days_to_infect(city):
    if not city or not city[0]:
        return 0

    rows, cols = len(city), len(city[0])
    queue = deque()
    healthy = 0

    for r in range(rows):
        for c in range(cols):
            if city[r][c] == '🧟':
                queue.append((r, c, 0))
            elif city[r][c] == '👤':
                healthy += 1

    if healthy == 0:
        return 0

    days = 0
    directions = [(-1,0), (1,0), (0,-1), (0,1)]

    while queue:
        r, c, day = queue.popleft()
        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            if 0 <= nr < rows and 0 <= nc < cols and city[nr][nc] == '👤':
                city[nr][nc] = '🧟'
                healthy -= 1
                days = day + 1
                queue.append((nr, nc, day + 1))

    return days if healthy == 0 else -1
