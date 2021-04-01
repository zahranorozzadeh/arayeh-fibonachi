import random

lis = []

for i in range(10):
    r = random.randint(1,20)
    if r not in lis:
        lis.append(r)

i+=1

print(lis)