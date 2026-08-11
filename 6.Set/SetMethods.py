numbers = {10, 20, 30}

print("Original set:", numbers)

numbers.add(40)
print("After add:", numbers)

numbers.update([50, 60])
print("After update:", numbers)

numbers.remove(20)
print("After remove:", numbers)

numbers.discard(100)
print("After discard:", numbers)