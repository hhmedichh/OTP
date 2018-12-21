# One Time Pad Enc/Dec Module

# Imports
import random

# Integer to Binary
def i2b(x):
    y = []
    if type(x) == "<class 'list'>":
        for i in range(len(x)):
            if x[i] != ",":
                f = list(str(bin(int(x[i]))))
                f.pop(0)
                f.pop(0)
                y.append("".join(map(str, f)))

            else:
                y.append(",")

    else:
        f = list(bin(int(x)))
        f.pop(0)
        f.pop(0)
        y.append("".join(map(str, f)))

    return "".join(map(str,y))

# String Conversion to Binary
def convert_string(x):
    x = list(x)
    x = list(",".join(format(ord(x), 'b') for x in x))
    for i in range(len(x)):
        if x[i] != ',':
            x[i] = int(x[i])
    return x

# Generating an encryption key
def key_gen(a):
    key = []
    bits = [0, 1]
    for i in range(len(list(a))):
        key.append(random.choice(bits))
    return key

# Encryption using key and binary input
def encrypt(k, m):
    c = []
    for i in range(len(m)):
        if m[i] == ",":
            c.append(",")

        else:
            y = int(k[i]) ^ int(m[i])
            c.append(y)
    return c

# Decryption usin key and binary input
def decrypt(k, c):
    m = []
    for i in range(len(c)):
        if c[i] == ",":
            m.append(",")

        else:
            y = int(k[i]) ^ int(c[i])
            m.append(y)
    return m

 #Compiling the binary string into a string of letters
def string_compile(m):
    x = "".join(map(str, m))
    x = x.split(",")
    string = ""
    for i in range(len(x)):
        char = chr(int(x[i], 2))
        string += char
    return string

 #Performing a character shift on the binary of a given string
def string_shift(x, y):
    global convert_string
    global string_compile
    global i2b

    s = convert_string(x)
    if y > 0:
        for i in range(len(s)):
            if s[i] != ",":
                s[i] = int(str(s[i]), 2)
                s[i] = str(s[i] << y)
                s[i] = i2b(s[i])
    else:
        for i in range(len(s)):
            if s[i] != ",":
                s[i] = int(str(s[i]), 2)
                s[i] = str(s[i] >> (0-y))
                s[i] = i2b(s[i])
    c = string_compile(s)
    return c
    

if __name__ == "__main__":
    import sys
    string = convert_string(sys.argv[1:])
    key = key_gen(string)
    x = encrypt(key, string)
    string = string_compile(x)
    print(string)
    
