n = int(input("Enter the Starting Number: "))
m = int(input("Enter the Ending Number: "))
sum = 0
for i in range(n, m + 1):
    if i % 2 == 0:
      sum += i
      print(i)
print("Sum of Even NUmbers: ",sum)