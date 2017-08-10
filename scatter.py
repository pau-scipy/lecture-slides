# scatter plot example

import matplotlib.pyplot as plt
import random

x = range(0,100)
y = random.sample(range(1000),100)

plt.scatter(x, y, c='g', marker='D')
plt.axis([0,100,0,1000])
plt.show()
