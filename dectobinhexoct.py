def conversion(num):
    b = bin(num)
    h = hex(num)
    o = oct(num)
    return b, h, o


print(conversion(8))
