import matplotlib.pyplot as plt
import math

x = []
y = []

# create x values
for n in range(0,360):
   x = x + [n]

# create y values
for n in x:
   y = y + [math.sin(n)]

# print chart
plt.plot(x, y)
plt.show()