# Caesar Cipher Encryptor

# O(n)
# n = len(string)


def caesarCipherEncryptor(string, key):
    return "".join([shiftN(x, key) for x in string])


def shiftN(character, key):
    newChar = ((ord(character) + key) - 97) % 26
    return chr(newChar + 97)
