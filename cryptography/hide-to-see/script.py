import string

def atbash_cipher(msg):
    alphabet = string.ascii_lowercase
    reversed_alphabet = alphabet[::-1]
    cipher = ""

    for c in msg:
        if c == '\n':
            continue
        if c.islower():
            cipher += reversed_alphabet[alphabet.index(c)]
        elif c.isupper():
            cipher += reversed_alphabet[alphabet.index(c.lower())].upper()
        else:
            cipher += c

    return cipher

m = open("encrypted.txt", "r").read()
print(atbash_cipher(m))
