set1 = set(input("Enter elements for Set 1: ").split())
set2 = set(input("Enter elements for Set 2: ").split())

print("Set 1:", set1)
print("Set 2:", set2)

print("Are sets equal?", set1 == set2)
print("Is Set 1 subset of Set 2?", set1.issubset(set2))
print("Is Set 1 superset of Set 2?", set1.issuperset(set2))