n = int(input("Enter the Starting Number: "))
m = int(input("Enter the Ending Number: "))
for i in range(n, m):

    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)            