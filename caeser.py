"""
## Caesar Cipher Decoder

A Caesar Cipher is a simple encryption technique where each letter in a message is shifted by a fixed number of positions in the alphabet. To decode the message, we shift each character **backwards** by the given shift value.

### Approach

1. Iterate through each character in the message.
2. If the character is a space, keep it unchanged.
3. Convert the letter to a numerical position using `ord()`.
4. Shift the position backwards by the given shift.
5. Use `% 26` to wrap around the alphabet.
6. Convert the new position back to a character using `chr()`.

### Key Python Functions Used
- `ord()` → converts a character to its ASCII value  
- `chr()` → converts an ASCII value back to a character  
- `% 26` → ensures the alphabet wraps from `a` to `z`
"""

def decode_message(message, shift):
    decoded = ""
    
    for char in message:
        if char == " ":
            decoded += " "
        else:
            pos = ord(char) - ord('a')
            new_pos = (pos - shift) % 26
            decoded += chr(new_pos + ord('a'))

    return decoded
