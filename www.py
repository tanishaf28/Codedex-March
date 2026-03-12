# Codédex Daily Challenge : World Wide Web 🌐 (March 12, 2026)
#
# Given a string representing a web address, determine if it's a valid URL.
#
# Validation rules:
# 1. It must start with "http://" or "https://"
# 2. The domain must contain at least one dot "."
# 3. The domain may only contain letters, digits, hyphens "-", or dots "."
#
# Return "valid" if the URL satisfies all conditions, otherwise return "invalid".
#
# Examples:
# Input: https://codedex.io       -> valid
# Input: https://netflixcom       -> invalid
# Input: http://en.wikipedia.org  -> valid


def check_url(address):
    if address.startswith("http://"):
        domain = address[7:]
    elif address.startswith("https://"):
        domain = address[8:]
    else:
        return "invalid"
    if "." not in domain:
        return "invalid"
    for char in domain:
        if not (char.isalnum() or char in "-."):
            return "invalid"

    return "valid"
