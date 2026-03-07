"""
Daily Challenge: Figure Skating Technical Element Score (TES)

At the 2026 Winter Olympics, Alysa Liu won two gold medals and ended a 24-year
Olympic gold drought for the U.S. in women’s figure skating.

Figure skating scoring has three parts:
1. Technical Element Score (TES)
2. Program Component Score
3. Deductions

In this challenge we calculate only the Technical Element Score.

Rules:
• Each skating element has a Base Value.
• 9 judges assign a Grade of Execution (GOE) from -5 to 5.
• To reduce bias, the highest and lowest GOE are removed.
• The remaining 7 scores are averaged.

Element Score formula:
Element Score = Base Value + (Average GOE × 0.1 × Base Value)

The Technical Element Score (TES) is the sum of all element scores.

Function Input:
elements → list of tuples
(name, base_value, [9 GOE scores])

Function Output:
Return the final TES rounded to ONE decimal place.
"""

def calculate_tes(elements):
    total = 0

    for name, base, goes in elements:
        goes = sorted(goes)

        # remove highest and lowest GOE
        trimmed = goes[1:-1]

        # average of remaining scores
        avg_goe = sum(trimmed) / len(trimmed)

        # element score calculation
        element_score = base + (avg_goe * 0.1 * base)

        total += element_score

    return round(total, 1)
