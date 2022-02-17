# arr = [2,4,7,1] target= 3 output = find arr[2]+arr[3]=8      o/p = 2,3

def index(arr, target):
    for i in range(len(arr)):
        for x in range(i, len(arr)):
            if target == arr[i]+arr[x]:
                return(i, x)


print(index(arr=[2, 4, 7, 1], target=8))
