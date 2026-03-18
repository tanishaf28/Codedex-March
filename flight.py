"""
💭 Given multiple flight vouchers and their corresponding delays, how do we pick the best one?

We want to maximize:
    voucher[i] / delay[i]

Constraints:
- delay[i] must be <= max_wait
- If multiple options tie → return the first
- If none qualify → return -1

Can we do this in O(n) without floating point precision issues?
"""

def pick_voucher(vouchers, delays, max_wait):
    best_index = -1

    for i in range(len(vouchers)):
        if delays[i] <= max_wait:
            # Compare ratios without division:
            # vouchers[i]/delays[i] > vouchers[j]/delays[j]
            # ⇔ vouchers[i] * delays[j] > vouchers[j] * delays[i]
            if best_index == -1 or vouchers[i] * delays[best_index] > vouchers[best_index] * delays[i]:
                best_index = i

    return best_index
