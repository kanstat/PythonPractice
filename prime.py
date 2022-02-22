# to print prime numbers between 100 to 200
x = 100
y = 200
flag = 0
for t in range(x, y+1):
    for i in range(2, t):
        if t % i == 0:
            flag = 1
            break
    else:
        print(t)
