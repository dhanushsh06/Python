matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
row = int(input("Enter at which row you want to store: "))
column = int(input("Enter at which column you want to store: "))
a = row - 1
b = column - 1
matrix[a][b] = int(input("Enter the Number to Store: "))
print(matrix)