text = "C Programming Language is Easy"
new_one = text.replace("C","Python")
print(f"Replaced:{new_one}")
print(f"Split:{new_one.split()}")
print(f"Joined Words:{"-".join(new_one.split())}")