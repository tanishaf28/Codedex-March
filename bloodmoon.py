"""
🩸 Blood Moon Predictor

Problem:
In The Legend of Zelda: Breath of the Wild, a Blood Moon occurs every
2 hours and 48 minutes (168 minutes). Given a time in "HH:MM" (24-hour format),
predict the next 3 Blood Moon times.

Input:
    time (str): A timestamp in "HH:MM" format.

Output:
    List[str]: A list of 3 timestamps representing the next Blood Moon times.

Rules:
- Time wraps around after 24 hours.
- If hours reach 24 → reset to 00.
- If minutes reach 60 → convert properly to hours.

Approach:
1. Convert input time into total minutes since midnight.
2. Add 168 minutes (2h 48m) repeatedly.
3. Use modulo 1440 (total minutes in a day) to handle wrap-around.
4. Convert back to "HH:MM" format with leading zeros.
"""
def blood_moon(time):
  # Write code below 💖
  hours, minutes = map(int, time.split(":"))
  total_minutes = hours * 60 + minutes
    
  interval = 2 * 60 + 48  # 168 minutes
  result = []
    
  for _ in range(3):
    total_minutes = (total_minutes + interval) % 1440  # wrap around 24h
    next_hour = total_minutes // 60
    next_minute = total_minutes % 60
        
    result.append(f"{next_hour:02d}:{next_minute:02d}")
    
  return result
