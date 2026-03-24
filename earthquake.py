"""
solve: Codedex Daily Challenge: Earthquake Anomaly 🌏

Given a list of seismograph magnitude readings, detect anomalies by
flagging any reading that exceeds 1.5x the median of all readings.

Approach:
- Guard against empty input early
- Sort a copy of the list to compute the median (even/odd length handled)
- Threshold = 1.5 * median
- Enumerate the original list to return correct indices

Uses median over mean because earthquake data is skewed, a single
massive quake can inflate the mean and mask real anomalies.
"""

def earthquake_anomaly(readings):
  # Write code below 💖
  if not readings:
    return []
  sortedreads = sorted(readings)
  n = len (sortedreads)

  if n % 2 ==0:
     median = (sortedreads[n // 2 - 1] + sortedreads[n // 2]) / 2
  else:
      median = sortedreads[n // 2]
  threshold = 1.5 * median
  return [i for i, r in enumerate(readings) if r > threshold]
