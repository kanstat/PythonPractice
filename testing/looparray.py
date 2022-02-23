# index = 0, value = 1
# arr = [1, 4, 6, 90, 3, 5, 7, 8, 2]
# for i in range(0, len(arr)):
#     if arr[i] % 2 == 0:

#         print(f"index = {i}, value = {arr[i]}")


arry = ['cat', 'dog', 'ball', 'bat', 'hello', 'ground']
for item in arry:  # 0,1,2,3,4,5
    length = len(item)
    if item[0] == 'b':
        continue
    print(item[length-2::])

print(arry[len(arry)-2][::-1])
