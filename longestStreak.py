"""
Title: Longest Streak 🔥 (Day 30 - Final Challenge)

Problem Statement:
Given a list representing a user's daily progress:
'✅' = completed the challenge that day
'❌' = missed that day or took 5+ tries
Write a function longest_streak(progress) that returns the length of the longest consecutive streak of '✅'.

Examples:
Input: ['✅', '✅', '✅', '✅', '✅', '✅', '❌']
Output: 6
Input: ['✅', '✅', '❌', '✅', '✅', '✅', '❌', '❌', '✅', '✅']
Output: 3

Constraints:
The list will only contain '✅' and '❌'
Length of list ≥ 1
"""

def longest_streak(progress):
    long_streak = 0
    current = 0

    for day in progress:
        if day == '✅':
            current += 1
            long_streak = max(long_streak, current)
        else:
            current = 0

    return long_streak
