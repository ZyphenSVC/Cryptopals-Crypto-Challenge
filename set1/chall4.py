from pwn import xor


with open("4.txt") as x:
    for l in x:
        for i in range(0x0, 0xff):
            key = xor(bytes.fromhex(l), i)
            print(key)

# b'Now that the party is jumping\n'
# b'[A-Z][a-z][a-z] '