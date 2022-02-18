# to find a sum of n natural numbers.
def natnumsum(num):
    sum = 0
    for i in range(num+1):
        sum = sum+i
    return (sum)


print(natnumsum(4))
