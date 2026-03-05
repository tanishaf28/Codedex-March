"""
Homebrew Computer Club – Altair 8800 Music Challenge
-----------------------------------------------------

On March 5, 1975, the Homebrew Computer Club held its first meeting.
Using the Altair 8800 (which had no keyboard or screen), programs were
entered manually using toggle switches representing binary values.

In this challenge, each 10-bit binary string represents a frequency (Hz).
Task:
1. Convert each binary string to its decimal value.
2. Map that decimal frequency to its corresponding musical note.

Frequency → Note Mapping:
    261 → "C4"
    294 → "D4"
    329 → "E4"
    349 → "F4"
    392 → "G4"
    440 → "A4"
    494 → "B4"
    523 → "C5"
      0 → "REST"

Example:
    Input:
        ["0100000101", "0000000000"]

    Conversion:
        0100000101 → 261 → "C4"
        0000000000 → 0   → "REST"

    Output:
        ["C4", "REST"]

Hint:
    - Use int(binary_string, 2) to convert binary to decimal.
    - Ensure returned note strings do NOT contain extra spaces.
"""

def dompier_music(switches):
  # Write code below
  frequency_to_note= {
    261: "C4",
    294: "D4",
    329: "E4",
    349: "F4",
    392: "G4",
    440: "A4",
    494: "B4",
    523: "C5",
    0: "REST"
  }
  
  result = []
  for binary in switches:
    decimal_value = int(binary, 2)
    note = frequency_to_note.get(decimal_value)
    result.append(note)
  return result

  
