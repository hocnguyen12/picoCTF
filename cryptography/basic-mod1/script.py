msg = open('message.txt', 'r').read().split()

import string

def decode(m):
    plaintext = ""
    for c in m:
        n = int(c) % 37
        # n is always >= 0
        if n <= 25:
            plaintext += string.ascii_letters[n].upper()
        elif n <= 35:
            plaintext += str(n - 26) # decimal digits -> n is between 26-35 adn corersponds to digits 0-9
        else:
            plaintext += '_'
    return plaintext

print(f"flag : picoCTF{{{decode(msg)}}}")
        