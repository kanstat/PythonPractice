#pi*r**2 *h
def volCylinder(r, h):

    pi = 3.14
    vol = pi*(r**2)*h
    return vol


print("r is radius in cm ")
print("h is height in  cm")
print(volCylinder(4, 10))
