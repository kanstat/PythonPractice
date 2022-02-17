# to check whether given number is prime or not.
def primeNum(x):
    flag = 0
    if x > 1:
        for i in range(2, x):
            if(x % i == 0):
                flag = 1
                break

    if flag:
        print("not prime")
    else:
        print('prime')


primeNum(69)
