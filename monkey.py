"""
Given a target string and a longer attempt string, return a dictionary/object with:

best_index : the starting index of the most similar window.
similarity : the highest similarity percentage rounded to 2 decimal places, if needed.
attempts : theoretical attempts to hit 100% at that rate, rounded to the nearest whole number. If the best similarity is 0%, set attempts to null. 🐒
*Round similarity to 2 decimal places for the final output only. Use the unrounded similarity value when calculating attempts.

If two windows have the same similarity, return the first one.
"""
def infinite_monkey(target, attempt):
    phrase_len = len(target)
    attempt_len = len(attempt)

    if phrase_len == 0 or attempt_len < phrase_len:
        return {"best_index": 0, "similarity": 0.0, "attempts": None}

    peak_similarity = -1.0
    peak_index = 0

    for slide_pos in range(attempt_len - phrase_len + 1):
        current_window = attempt[slide_pos : slide_pos + phrase_len]
        matched_chars = sum(
            c1 == c2 for c1, c2 in zip(current_window, target)
        )
        window_similarity = (matched_chars / phrase_len) * 100

        if window_similarity > peak_similarity:
            peak_similarity = window_similarity
            peak_index = slide_pos

    if peak_similarity == 0:
        return {"best_index": peak_index, "similarity": 0.0, "attempts": None}

    estimated_attempts = round((100 / peak_similarity) ** phrase_len)

    return {
        "best_index": peak_index,
        "similarity": round(peak_similarity, 2),
        "attempts": estimated_attempts,
    }
