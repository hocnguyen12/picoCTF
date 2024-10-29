msg = open('message.txt', 'r').read().split()

import string
from Crypto.Util.number import inverse

def decode(m):
    plaintext = ''
    for c in m:
        n = inverse(int(c), 41)
        if n <= 26: # n betwee 1 and 26
            plaintext += string.ascii_uppercase[n - 1]
        elif n <= 36:
            plaintext += str(n - 27)
        elif n == 37:
            plaintext += '_'
    return plaintext

print(len(string.ascii_uppercase))

print(f"flag : picoCTF{{{decode(msg)}}}")