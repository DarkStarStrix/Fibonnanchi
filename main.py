# code the fibbonacci polynomial and plot it using matplotlib

import matplotlib.pyplot as plt
import numpy as np


# define the fibbonacci polynomial
def fibbonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibbonacci(n - 1) + fibbonacci(n - 2)


# define the range of the x-axis
x = np.arange(0, 10, 1)

# define the y-axis
y = [fibbonacci(i) for i in x]

# plot the graph
plt.plot(x, y)
plt.xlabel('x-axis')
plt.ylabel('y-axis')
plt.title('Fibbonacci Polynomial')
plt.grid(True)
plt
plt.show()

# print the values of the fibbonacci polynomial
print(y)

# print the sum of the fibbonacci polynomial
print(sum(y))

# print the average of the fibbonacci polynomial
print(sum(y) / len(y))
