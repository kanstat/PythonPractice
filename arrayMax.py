arr = [24, 89, 300, 20, 30, 40]
max = arr[0]
for x in range(len(arr)):
    if arr[x] > max:
        max = arr[x]
print("largest number is:", max)
