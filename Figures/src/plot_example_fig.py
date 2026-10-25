#!/usr/bin/env python3

import matplotlib.pyplot as plt
import numpy as np
import os
os.chdir(os.path.dirname(__file__))

x = np.linspace(0,1,11)
y = x**2

fig, ax = plt.subplots()
ax.plot(x, y)
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_title('Example Plot')
fig.savefig('../Fig_Example.png',
bbox_inches='tight', dpi=100)

plt.show()