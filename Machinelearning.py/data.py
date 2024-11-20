import numpy as np
import matplotlib.pyplot as plt
data = np.random.uniform(0,10,100)
print(data)
plt.hist(data)
plt.show()
# normal and uniform data 
# plt.uniform(data)