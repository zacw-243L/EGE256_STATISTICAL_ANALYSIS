import time
import numpy as np
import seaborn as sns
from scipy.stats import norm
import matplotlib.pyplot as plt

start_time = time.time()

np.random.seed(7)
population = norm.rvs(loc=50.0, scale=30.0, size=10000)

# take only one sample from the population
n = 10
conf_level = 0.95
sample = np.random.choice(population, n)
sam_means = []

for i in range(1000):
    bootstrap = np.random.choice(sample, n)
    sam_means.append(bootstrap.mean())

print('%0.2f%% bootstrap confidence interval = (%0.2f,%0.2f)' % (conf_level * 100, np.percentile(sam_means, 2.5), np.percentile(sam_means, 97.5)))
print("--- %s seconds ---" % (time.time() - start_time))
