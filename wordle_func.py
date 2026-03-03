def wordle_guess(secret, guess):
    """
    🧩 Challenge:
    Given two 5-letter strings (secret and guess),
    return how many letters are correct AND in the exact same position.

    🔎 Example:
    secret = "CODEX"
    guess  = "COINS"
    Output → 2  (C and O match in the same positions)

    💡 How to Solve:
    1. Create a counter variable to track matches.
    2. Loop through index positions 0 to 4 (since both words are 5 letters).
    3. At each index, compare secret[i] with guess[i].
    4. If they are equal, increase the counter.
    5. Return the counter after the loop ends.
    """

    # Step 1: Initialize a counter to track correct-position matches
    count = 0
    
    # Step 2: Loop through each index (0 to 4)
    for i in range(5):
        
        # Step 3: Check if letters at the same position match
        if secret[i] == guess[i]:
            
            # Step 4: If match found, increment counter
            count += 1
    
    # Step 5: Return total matches
    return count
