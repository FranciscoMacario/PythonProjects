import math

n = 10

for y in range(n, -n, -1):
    for x in range(-n, n):
        if((x**2) + ((5*y/4) - math.sqrt(4*abs(x)))**2) <= n**2:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print("")

#testing import libraries 