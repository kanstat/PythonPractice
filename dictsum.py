def dictvaluesum(dic):
    sum = 0
    for i in dic.values():
        sum = sum + i
    return sum


dic = {'a': 100, 'b': 200, 'c': 300}
print(dictvaluesum(dic))
