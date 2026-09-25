import random
import time
start = time.time()
big_list = []
for i in range(1000000):
    big_list.append(random.randint(0, 1000000))
big_list.sort()
print(time.time() - start)