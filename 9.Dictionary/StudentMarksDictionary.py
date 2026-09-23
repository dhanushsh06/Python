marks = {}
n = int(input("Number of Subjects:"))
for i in range(1,n+1):
    subject = input(f"Subject {i}:")
    mark = int(input(f"Marks of {subject}:"))
    marks[subject] = mark
print("\nStudent Marks")
total = sum(marks.value())
print(f"Total marks:{sum(marks.value())}")    