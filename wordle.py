
# Online Python - IDE, Editor, Compiler, Interpreter
import random

# ==========================================
# WORDLE GAME - CONSOLE VERSION
# ==========================================
# Rules:
# 🟩 = Correct letter, correct position
# 🟨 = Correct letter, wrong position
# ⬜ = Letter not in the word
# You get 6 attempts to guess a 5-letter word.
# ==========================================


def generate_feedback(secret, guess):
    """
    Compares the guess with the secret word
    and returns a string of colored feedback.
    
    Challenge Question:
    Why do we convert the secret into a list?
    → Because we may need to 'mark' letters as used
      (important when handling duplicate letters).
    """

    feedback = ["⬜"] * 5
    secret_letters = list(secret)

    # Step 1: Check correct positions (🟩)
    for i in range(5):
        if guess[i] == secret[i]:
            feedback[i] = "🟩"
            secret_letters[i] = None  # Mark letter as used

    # Step 2: Check correct letters, wrong position (🟨)
    for i in range(5):
        if feedback[i] == "⬜" and guess[i] in secret_letters:
            feedback[i] = "🟨"
            # Remove first occurrence so duplicates are handled correctly
            secret_letters[secret_letters.index(guess[i])] = None

    return "".join(feedback)


def wordle_game():
    """
    Main game function.
    
    Challenge Question:
    Why do we separate game logic into functions?
    → Cleaner code
    → Easier debugging
    → Reusable logic
    """

    word_list = ["APPLE", "GRAPE", "MANGO", "PEACH", "BERRY", "LEMON"]
    secret = random.choice(word_list)
    attempts = 6

    print("🎮 Welcome to Wordle!")
    print("Guess the 5-letter word. You have 6 attempts.\n")

    for attempt in range(1, attempts + 1):

        guess = input(f"Attempt {attempt}/6: ").upper()

        # Input validation
        if len(guess) != 5 or not guess.isalpha():
            print("⚠️ Enter exactly 5 letters.\n")
            continue

        # Win condition
        if guess == secret:
            print("🟩🟩🟩🟩🟩")
            print("🎉 You guessed the word!")
            return

        # Generate feedback
        result = generate_feedback(secret, guess)
        print(result, "\n")

    print(f"❌ Game Over! The word was: {secret}")


# Run the game
wordle_game()
