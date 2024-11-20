import numpy as np
from scipy import stats as st
# Mean --> Avg
# Median --> mid Value
# Mode --> most repeated value 
salary = [65000, 85000, 90000,70000,80000,65000]
print(np.mean(salary),"mean")  # mean
print(np.max(salary),"max")   
print(np.min(salary),"min")
print(np.median(salary),"median") # median
print(st.mode(salary),"mode") # mode
        # standard deviation
print(np.std(salary), "standard deviation")  
        # variance
print(np.var(salary), "Variance")