import base64


hexString = "1c0111001f010100061a024b53535009181c"

secondString = "686974207468652062756c6c277320657965"

newString = hex(int(hexString,16) ^ int(secondString, 16))

print(newString)