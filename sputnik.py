# Sputnik 9 Descent Time Calculator
# March 9, 1961 – The Soviet Union launched Sputnik 9 as the final rehearsal
# before sending a human into space. Onboard were a mannequin named
# "Ivan Ivanovich", a dog named Chernushka, mice, and a guinea pig.
# The capsule completed one orbit and all passengers survived.

# Problem
# Given a starting altitude (in km), calculate the total time (in seconds)
# it takes for the capsule to descend to Earth. Return the time rounded
# to one decimal place.

# The Earth's atmosphere layers and descent speeds:
# Exosphere     (700–10000 km) → 2000 m/s
# Thermosphere  (85–700 km)   → 500 m/s
# Mesosphere    (50–85 km)    → 200 m/s
# Stratosphere  (12–50 km)    → 75 m/s
# Troposphere   (0–12 km)     → 20 m/s

# Example
# Input: 200
# Output: 1511.7
#
# Input: 12
# Output: 600.0

def descent_time(altitude):
    layers = [
        (700, 2000),  # Exosphere
        (85, 500),    # Thermosphere
        (50, 200),    # Mesosphere
        (12, 75),     # Stratosphere
        (0, 20)       # Troposphere
    ]

    time = 0.0

    for lower, rate in layers:
        if altitude > lower:
            distance = (altitude - lower) * 1000
            time += distance / rate
            altitude = lower

    return round(time, 1)
