# Wireshark doo dooo do doo... Solution
By looking at `HTTP` requests, we have two responses to `GET` requests that are `text/data`.

We can clearly display them with the `data-text-lines` filter.

One of these responses contain the data:
`Gur synt vf cvpbPGS{c33xno00_1_f33_h_qrnqorrs}\n`

This is clearly encrypted with the ceasar cipher.

We can easily decrypt this with an online tool (https://www.dcode.fr/caesar-cipher for example)

This is the result: `The flag is picoCTF{p33kab00_1_s33_u_deadbeef}\a`