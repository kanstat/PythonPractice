#to print this given pattern.
# *
# **

# ****
# *****

for i in range(1, 6):  # 1,2,3,4,5
    for x in range(1, i+1):  # 1,i
        if i == 3:
            continue
        print(f"*", end='')
    print('')
