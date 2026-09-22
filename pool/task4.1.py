pi=0
n=2000000
for i in range(n):
    pi+=(-1)**i/(2*i+1)
pi*=4
print(round(pi,6))