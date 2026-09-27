text = input("Enter a sentence: ")

print("\n--- Text Analysis ---")

print("Original:", text)
print("Uppercase:", text.upper())
print("Lowercase:", text.lower())
print("Title:", text.title())
print("Character count:", len(text))
print("Word count:", len(text.split()))
print("Python occurrences:", text.lower().count("python"))
print("Starts with Hello:", text.startswith("Hello"))
print("Ends with .:", text.endswith("."))