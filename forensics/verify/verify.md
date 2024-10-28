# Verify challenge solution

The `verify.sh` script checks if a files in the given directory has the same sha256 checksum as a reference checksum.

I learned some basics of bash scripting:
- conditions
- for loops
- variable assignation
- integration with unix commands

```bash
bash verify.sh files checksum.txt 
```
output: `files/c6c8b911 has the same hash as the reference checksum.`

We can then use the given `decrypt.sh` script:
```bash
bash decrypt.sh files/c6c8b911 
```

output: `picoCTF{trust_but_verify_c6c8b911}`

