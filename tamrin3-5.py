
number = int(input("please Enter integer number: "))
factorial = 1

for i in range(1, number+1):
    factorial = factorial * i

print("The factorial of {} is: {}".format(number, factorial))