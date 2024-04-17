import matplotlib.pyplot as plt
from scipy.stats import norm
import numpy as np
import time

start_time = time.time()

# normal random variable with mean 0.0 and standard deviation 1.0
rv_normal = norm(0.0, 1.0)
# generate 1000 random numbers with the distribution
x = rv_normal.rvs(1000)
print(x)
# calculate the mean and variance
print('mean =', np.mean(x))
print('standard deviation =', np.std(x))
print("--- %s seconds ---" % (time.time() - start_time))
