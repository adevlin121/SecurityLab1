def ceasar(s, k, decrypt=False):
    if decrypt: k = 26-k

    r = ""
    for i in s:
        if (ord(i) >= 65 and ord(i) <= 90):
            r += chr((ord(i) - 65 + k) % 26 + 65)
        elif (ord(i) >= 97 and ord(i) <= 122):
            r += chr((ord(i) - 97 + k) % 26 + 97)
        else:
            r += i
    return r

def encrypt(p, k):
    return ceasar(p, k)

def decrypt(c, k):
    return ceasar(c, k, decrypt=True)

print encrypt("Aidan Devlin", 15)

print decrypt("Pxspc Stkaxc", 15)
