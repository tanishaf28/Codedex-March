"""
 🏆 Oscars Prediction Challenge

Last night was the Academy Awards and my friends and I ran a small **Oscars Pool** where everyone predicted the winners of several categories.
After the ceremony, we wanted to calculate **who had the most accurate predictions**.

The task is to write a function that:
* Compares each friend's predictions with the actual winners
* Calculates their accuracy
* Returns the friend with the **highest score**
* If two or more friends have the same highest score → return `"Tie"`

---

### Approach
1. Store the **actual winners** in a list.
2. Loop through each friend's predictions.
3. Compare their guesses with the winners.
4. Count how many predictions match.
5. Track the highest score.
6. If another friend gets the same score → mark it as a tie.

---

"""
def oscar_pool(predictions):

    winners = [
        "One Battle After Another",
        "Michael B. Jordan",
        "Jessie Buckley",
        "Paul Thomas Anderson"
    ]

    max_score = -1
    compare_friend = ""
    tie = False

    for friend in predictions:
        name = friend[0]
        guesses = friend[1:]

        score = 0
        for i in range(len(winners)):
            if guesses[i] == winners[i]:
                score += 1

        if score > max_score:
            max_score = score
            compare_friend = name
            tie = False
        elif score == max_score:
            tie = True

    if tie:
        return "Tie"
    return compare_friend
