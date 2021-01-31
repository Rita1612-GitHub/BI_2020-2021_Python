import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.DataFrame(np.sort(np.sort(np.random.randn(10, 2), axis=0), axis=1), columns=['randx', 'randy'])
df.plot(kind='line', x='randx', y='randy', legend=False)
plt.title("Line plot", fontsize=22)
plt.xlabel("x random values")
plt.ylabel("y random values")
#plt.show()
plt.savefig('Line_plot.png')
