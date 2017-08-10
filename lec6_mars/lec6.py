import numpy as np
import matplotlib.pyplot as plt

# Data file obtained from http://pds-geosciences.wustl.edu/missions/mgs/megdr.html

# Read the data from the file as a 1-dimensional array of 16-bit ints
a = np.fromfile("megt90n000cb.img", dtype=np.uint16)
# Reshape the array to have rows and columns
b = a.reshape(720, 1440)
print(b)

# rescale to between 0.0 - 1.0 for plotting with imshow
c = b / 65535.0
# choose a red colourmap, because it's Mars!
plt.imshow(c, cmap="hot")
plt.colorbar()

# If not plotting inline in iPython
plt.show()

