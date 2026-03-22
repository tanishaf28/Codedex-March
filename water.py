"""
💧 Water Pipe Leak Simulation

Given:
- A starting volume of water
- A leak percentage per hour
- A number of hours
- A minimum pressure threshold

Each hour, the volume decreases by a fixed percentage of its current value:
new_volume = current_volume * (1 - leak / 100)

If at any point the volume drops below the threshold, the pipe fails and stops working.

Task: Write a function that returns:
- The remaining volume after all hours (rounded to 2 decimal places), OR
- -1 if the pipe fails before the time is up

Example:
Input:volume = 1000
leak = 5
hours = 3
threshold = 100
Output: 857.38
"""

def water_pipe(volume, leak, hours, threshold): 
  for _ in range(hours): 
    volume *= (1 - leak / 100) 
    if volume < threshold: 
      return -1 
  return round(volume, 2)
