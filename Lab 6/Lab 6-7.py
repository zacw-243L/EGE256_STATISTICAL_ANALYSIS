import matplotlib.pyplot as plt
from scipy.stats import norm
import numpy as np
import time

start_time = time.time()

# normal random variable with mean 0.0 and standard deviation 1.0
rv_normal = norm(0.0, 1.0)
n = 1000
# generate some random numbers with the distribution
x = rv_normal.rvs(n)
# calculate the mean and variance
mu = np.mean(x)
sigma = np.std(x)

# count numbers within one, two and three standard deviations from mean
for i in range(1, 4):
    in_sigma = np.where((x >= mu - i * sigma) & (x <= mu + i * sigma))
    print('numbers within {} sigma = {:.2f}%'.format(i, np.count_nonzero(in_sigma) / n * 100.0))

print("--- %s seconds ---" % (time.time() - start_time))
