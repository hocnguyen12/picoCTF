# Hide to See solution

To facilitate the challenge, I wrote an implementation of the atbash cipher in `script.py`.

The data do decipher was hard to find but finding hidden data in the image was the good idea.

Since the format is `.jpg`, steghide is the most appropriate tool to use.

With the command:
```bash
steghide extract -sf atbash.jpg
```
We can extract the hidden data (the password used was the default one -> no password).

The extracted data is automatically written into `encrypted.txt`.

`script.py` takes this data and decrypts it with the atbash cipher.

Output: `picoCTF{atbash_crack_1f84d779}`.