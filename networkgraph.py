#!usr/bin/env python

import matplotlib.pyplot as plt
import numpy as np

x = np.arange(0, 3 * np.pi, 0.1)
y = np.sin(x)

plt.title("sine wave form")

plt.plot(x, y)
plt.show()
