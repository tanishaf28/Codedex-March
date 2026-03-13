# Palindrome Checker - Day 12 CodeDex Challenge
"""
Day 12 – Palindrome Checker

Today's challenge was to build a function that checks whether a string is a palindrome.
A palindrome reads the same forwards and backwards. The tricky part here was ignoring spaces and capitalization before doing the comparison.

Approach:
Remove spaces using replace()
Convert the string to lowercase
Reverse the string using slicing [::-1]
Compare the cleaned string with its reverse
Python makes this pretty concise thanks to slicing.


Question for others attempting this challenge:
Besides reversing the string with slicing, what other approaches could be used to check for a palindrome?

For example:
• Two-pointer technique from both ends?
• Stack-based comparison?
• Functional programming approach?

Curious what solutions others came up with.
"""

def check_palindrome(sequence):
    clean = sequence.replace(" ", "").lower()
    return clean == clean[::-1]



# Example tests
print(check_palindrome("racecar"))                  # True
print(check_palindrome("Was it a car or a cat I saw"))  # True
print(check_palindrome("11 11"))                    # True
print(check_palindrome("12345"))                    # False

