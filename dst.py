"""
Daylight Savings ⏰ — Sleep Debt Calculation

When Daylight Saving Time begins, we "spring forward" and lose one hour of sleep.
This contributes to sleep debt, which is the difference between how much sleep
someone planned to get and how much they actually got.

Sleep Debt Formula:
Sleep Debt = max(0, Planned Sleep − Actual Sleep)

Where:
- Planned Sleep: hours someone intended to sleep
- Actual Sleep: hours they actually slept
- max(0, x): ensures debt cannot be negative

Task:
Given two lists representing a week's sleep schedule:
1. Calculate the total sleep debt for the week
2. Add +1 hour to account for Daylight Savings
3. Determine the longest streak of consecutive days where sleep debt > 0

Return:
- Total sleep debt for the week
- Longest consecutive streak of sleep debt days

Example (my sleep data):

planned = [8, 8, 7.5, 8, 6, 7.5, 8]
actual  = [5.5, 6, 5, 6, 5.5, 6, 7]

Sleep debt per day:
2.5 + 2 + 2.5 + 2 + 0.5 + 1.5 + 1 = 12.0 hours
+1 hour (Daylight Savings)

Total Sleep Debt = 13.0 hours
Longest Streak = 7 days
"""


def calculate_sleep_debt(planned, actual):
    total_debt = 0
    current_streak = 0
    longest_streak = 0

    for p, a in zip(planned, actual):
        debt = max(0, p - a)
        total_debt += debt

        if debt > 0:
            current_streak += 1
            longest_streak = max(longest_streak, current_streak)
        else:
            current_streak = 0

    # Add +1 hour due to Daylight Savings
    total_debt += 1

    return total_debt, longest_streak
