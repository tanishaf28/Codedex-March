"""
### Question
Given a list of matchups in the format `["Team A", seedA, "Team B", seedB]` (Team A is always the stronger team), how can we compute the probability that the underdog (Team B) wins, rounded to 2 decimal places?  

For example:

```python
matchups = [["Duke", 1, "Siena", 16], ["Ohio State", 8, "TCU", 9]]
# Expected output: [0.06, 0.47]
"""

def upset_probability(matchups):
    probabiltys = []
    for matchup in matchups:
        seedA = matchup[1] 
        seedB = matchup[3]  
        probability = seedA / (seedA + seedB)
        probabiltys.append(round(probability, 2))
    return probabiltys  
