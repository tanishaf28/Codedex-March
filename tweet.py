"""
🐦 First Tweet Character Counter (Codédex Daily Challenge)
 Problem Statement: Given a tweet string, compute how many characters remain out of a 140-character limit.

Special counting rules:
Usernames (@something) → 20 characters
URLs (http:// or https://) → 23 characters
Emojis → 2 characters
All other characters → count normally (including spaces & punctuation)

 Output Rules:
-Return remaining characters if within limit
-Return a negative number if the tweet exceeds 140 characters

Approach
Instead of iterating character-by-character over the whole string, we:
1. Split the tweet into words
2. Process each word independently:
3. Detect mentions and URLs via prefix
4. Count emojis using Unicode range (ord(char) > 127)
5. Subtract spaces manually (len(words) - 1)
6. Maintain a running balance from 140

Key Observations
-Splitting by words simplifies token classification (O(n) total complexity)
-Emoji detection via ord(char) > 127 is a practical approximation
-Space handling is explicit, avoiding hidden off-by-one errors
"""

def tweet_balance(tweet):
    LIMIT = 140
    USERNAME_COUNT = 20
    URL_COUNT = 23
    EMOJI_COUNT = 2

    remaining = LIMIT
    words = tweet.split()
    
    for word in words:
        if word.startswith('@'):
            remaining -= USERNAME_COUNT
        elif word.startswith('http://') or word.startswith('https://'):
            remaining -= URL_COUNT
        else:
            char_count = 0
            for char in word:
                if ord(char) > 127:
                    char_count += EMOJI_COUNT
                else:
                    char_count += 1
            remaining -= char_count
    if len(words) > 0:
        remaining -= (len(words) - 1)
    
    return remaining
