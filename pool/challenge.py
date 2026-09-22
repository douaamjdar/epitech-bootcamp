n = 1
found = False
while not found:
    found = True
    for i in range(2, 21):
        if n % i != 0:
            found = False
            break
    if not found:
        n += 1

print(n)



import math 
result = 1
for i in range(1, 201):
    result = math.lcm(result, i)
    print(result)



import math
result = 1
for i in range(1, 2001):
    result = math.lcm(result, i)
    print(result)