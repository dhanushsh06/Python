n = int(input("Enter the Starting Number: "))
m = int(input("Enter the Ending Number: "))
print("Even Numbers")
for Even in range(n, m + 1):
    if Even % 2 == 0:
      print(Even)
print("Odd Numbers")    
for Odd in range(n + 1, m + 1):
    if Odd % 2 != 0:
      print(Odd)

