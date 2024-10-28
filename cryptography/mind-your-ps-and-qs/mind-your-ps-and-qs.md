# Mind your Ps and Qs Writeup

The goal is to factorize `n` to find the inverse of `e` modulo `phi(n) = (p - 1)(q - 1)` where `pq = n`.

Using `primefac` takes way too long so we can use `factordb.com`.

https://factordb.com/index.php?query=1422450808944701344261903748621562998784243662042303391362692043823716783771691667

We get `p` and `q` that we can simply paste into our script.

`script.py` does the rest of the work which is to calculate `phi`, `d`, the inverse of e (using `Crypto.Util.number.inverse`) and decrypt.

The decrypted number must be converted to bytes so the result is readable. To do this we use `Crypto.Util.number.long_to_bytes`.

Output : 
```bash
q * p == n : True
flag : b'picoCTF{sma11_N_n0_g0od_00264570}'
```