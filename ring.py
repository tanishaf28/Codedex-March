# Codédex Daily Challenge – Unique Words in a Phone Transcript
# March 10, 2026
#
# Alexander Graham Bell made the first telephone call on March 10, 1876
# to his assistant Thomas Watson, saying:
# "Mr. Watson, come here, I want to see you."
#
# Task:
# Write a function that counts the number of unique words in a phone
# call transcript.
#
# Rules:
# - Words are separated by spaces
# - Ignore punctuation
# - Treat words as the same regardless of capitalization
#
# Example:
# Input: "Mr. Watson, come here, I want to see you."
# Output: 9

import string

def find_unique_words(transcript):
    # Convert text to lowercase
    transcript = transcript.lower()

    # Remove punctuation
    for p in string.punctuation:
        transcript = transcript.replace(p, "")

    # Split into words
    words = transcript.split()

    # Use a set to keep only unique words
    unique_words = set(words)

    # Return the number of unique words
    return len(unique_words)
