def rot13_cipher(str_in, shift):
    alpha = "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"
    n = len(str_in)
    str_out = ""

    for i in range(n):
        c = str_in[i].upper()
        loc = alpha.find(c)
        newloc = (loc + shift) % 26
        str_out += alpha[newloc]

    return str_out

def rot13(msg):
    return rot13_cipher(msg, 13)
