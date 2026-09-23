text = "Python is easy and Python is human friendly language"
text1 = "12345"
text2 = "Python123"
text3 = " "

print(f"Startswith:{text.startswith("Python")}")
print(f"Endswith:{text.endswith("human")}")
print(f"Alphanumeric:{text1.isalnum()}")
print(f"Only Alphabets:{text2.isalpha()}")
print(f"Only space:{text3.isspace()}")
print(f"Only digitdigit:{text1.isdigit()}")
