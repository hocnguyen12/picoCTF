# Interencdec solution
The content looks like base64 so we can do:
```bash
base64 -d enc_flag 
```
output: `b'd3BqdkpBTXtqaGx6aHlfazNqeTl3YTNrXzg2a2wzMmsyfQ=='`

The output also seems to be base64.

We want to make sure we remove the `b` and `'` characters with `sed` or the base64 decode function will not work.

```bash
cat enc_flag | base64 -d | sed "s/^b'//;s/'$//" | base64 -d
```
output: `wpjvJAM{jhlzhy_k3jy9wa3k_86kl32k2}`

The flag is clearly encrypted with the caesar cipher, we can decrypt this flag with with an online tool like `https://www.dcode.fr/caesar-cipher`.

We get `picoCTF{caesar_d3cr9pt3d_86de32d2}`.