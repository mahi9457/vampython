from sklearn.metrics import r2_score
import numpy as np
age = [20,25,45,30,50,40]
salary = [20000,25000,45000,30000,50000,40000]
future_data = np.poly1d(np.polyfit(age,salary,3))
print(r2_score,salary,future_data(35))