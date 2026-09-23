marks = {
    "MATHS":92,
    "PYTHON":95,
    "DSA":93
}

subject = input("Enter Subject:").upper()
if subject in marks:
    print(f"Subject is found, marks {marks[subject]}")
else:
    print("Subject is not found")    