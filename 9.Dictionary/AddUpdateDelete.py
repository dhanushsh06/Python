student = {
    "Name" : "Dhan",
    "Age" : 20,
    "Course" : "CSE" 
}
print("Before Modifying")
print(student)

student["Course"] = "AIML"
del student["Age"]
student["USN"] = 52

print(f"After Modifying:{student}")