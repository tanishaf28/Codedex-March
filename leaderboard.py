"""
Task: Given two pieces of a user's data:

The total time spent on challenges, in the format "H:MM:SS"
The number of challenges completed
Convert the total time into seconds and calculate the average time per challenge.

Return the average time per challenge (rounded to the nearest second). ⏱️
"""

def average_time(total, completed):
  # Write code below 💖
  hours, minute, sec = total.split(":")
  total_sec = int(hours) * 3600 + int (minute) *60 + int(sec)
  return round(total_sec / completed)
