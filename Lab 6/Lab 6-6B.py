import matplotlib.pyplot as plt
from scipy.stats import norm
import numpy as np
import time

start_time = time.time()

# normal random variable with mean 0.0 and standard deviation 1.0
rv_normal = norm(3.0, 5.0)
# generate 1000 random numbers with the distribution
x = rv_normal.rvs(1000)
xmean = np.mean(x)
xstd = np.std(x)
x -= xmean
x /= xstd

print('mean = %0.4f' % np.mean(x))
print('standard deviation = %0.4f' % np.std(x))
print("--- %s seconds ---" % (time.time() - start_time))
