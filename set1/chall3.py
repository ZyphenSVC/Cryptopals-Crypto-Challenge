from pwn import xor
flag_hex = '1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736'
flag_bytes = bytes.fromhex(flag_hex)

for i in range(0x0, 0xff):
    key = xor(flag_bytes, i)
    print(key)

# b"Cooking MC's like a pound of bacon"