student = {}
student["Name"] = input("Enter Name of the student:")
student["Age"] = int(input("Enter age of Student:"))
student["Course"] = input("Enter Course:")

print(f"After user input:{student}")

print(f"Key:{student.keys()}")
print(f"Value:{student.values()}")
print(f"Items:{student.items()}")