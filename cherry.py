"""
### 🌸 Cherry Blossoms Rolling Average 

I'm working on a problem inspired by sakura bloom prediction.

We are given a list of daily temperatures, and blossoms bloom on the **first day (1-indexed)** where the **5-day rolling average temperature is ≥ 15°C**.
Input: [10, 11, 13, 14, 16, 17, 18]
Output: 7


#### My Understanding:
- For each day `i ≥ 4`, compute the average of `temps[i-4:i+1]`
- Return the first day where the average ≥ 15
- If no such day exists, return `-1`

#### Question:
Is using a sliding window sum (O(n)) the optimal approach here, or is there a more numerically stable / efficient way when scaling this to large datasets or streaming inputs?

Also, is it better to:
- Compare `window_sum >= 75` (avoid division), or
- Compute the average directly for clarity?

Would appreciate feedback on correctness and best practices!
"""

def cherry_blossoms(temps):
    sum = 0
    k = 5

    for i in range(len(temps)):
        sum += temps[i]

        if i >= k:
            sum -= temps[i - k]

        if i >= k - 1:
            if sum / k >= 15:
                return i + 1  

    return -1
