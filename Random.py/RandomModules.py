import random

a = random.randint(1,8)
print(a)
b = random.randrange(1,9)
print(b)
c = random.random()
print(c)
d = random.uniform(1,5)
print(d)
l = [12,23,34,56,78,76]
print("list is: ",l)
e = random.choice(l)
print(e)
m = [12,33,34,50,78,90]
random.shuffle(m)
print(m)