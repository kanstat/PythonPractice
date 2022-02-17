# program make a simple calculator
num1 = 0
num2 = 0


def add(a, b):
    return (a+b)


def sub(x, y):
    return(x-y)


def mul(x, y):
    return(x*y)


def devide(x, y):
    return(x/y)


print("Select operation.")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")

while True:
    choice = (input("enter choice(1 , 2 ,3 ,4) : "))

    if choice in ("1", "2", "3", " 4"):
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
    if choice == "1":
        # print(num1, '+', num2, '=', add(num1, num2))
        print(f"{num1} +{num2} = {add(num1,num2)}")
    elif choice == "2":
        print(num1, '-', num2, '=', sub(num1, num2))
    elif choice == "3":
        print(num1, '*', num2, '=', mul(num1, num2))
    elif choice == "4":
        print(num1, '/',  num2, '=', devide(num1, num2))
    next_calculation = input("Let's do next calculation? (yes/no): ")
    if next_calculation == "no":
        break
