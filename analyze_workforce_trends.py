"""
Happy International Women's Day! 💜

Tech companies publish annual diversity reports showing the percentage of
women in their workforce. Given a list of these yearly percentages, analyze
the trend and return three metrics:

1. Net Change Per Year
   Average yearly increase or decrease.
   Formula:
   (Last Year − First Year) / (Years − 1)

2. Trend
   Compare the average of the first 3 years to the average of the last 3 years:
   - "improving"  → last 3-year average is higher
   - "stagnating" → averages are equal
   - "declining"  → last 3-year average is lower

3. Dips
   The number of years where the percentage decreased compared to
   the previous year.

Function Input:
    percentages (list of floats) – yearly percentages of women in the workforce.

Function Output:
    tuple → (net_change_per_year, trend, dips)

Example:
Input:
[31.0, 31.0, 33.0, 35.0, 36.0, 36.0, 36.2, 36.7, 37.1]

Output:
(0.7625, "improving", 0)
"""

def analyze(percentages):
    n = len(percentages)

    # Net change per year
    net_change = (percentages[-1] - percentages[0]) / (n - 1)
    net_change = float(f"{net_change:.4f}".rstrip('0').rstrip('.'))

    # First and last 3-year averages
    first_avg = sum(percentages[:3]) / 3
    last_avg = sum(percentages[-3:]) / 3

    # Determine trend
    if last_avg > first_avg:
        trend = "improving"
    elif last_avg < first_avg:
        trend = "declining"
    else:
        trend = "stagnating"

    # Count dips
    dips = sum(1 for i in range(1, n) if percentages[i] < percentages[i-1])

    return net_change, trend, dips
