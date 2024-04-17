import time
import numpy as np
import seaborn as sns
from scipy.stats import norm
import matplotlib.pyplot as plt

start_time = time.time()

np.random.seed(7)
population = norm.rvs(loc=50.0, scale=30.0, size=10000)
pop_mean = population.mean()
pop_std = population.std()

n = 50
sample = np.random.choice(population, n)
sam_mean = sample.mean()
conf_level = 0.95
z_critical = -norm.ppf((1.0 - conf_level) * 0.5)
print("z-critical value = %0.2f" % z_critical)
err_margin = z_critical * pop_std / np.sqrt(n)
conf_interval = (sam_mean - err_margin, sam_mean + err_margin)
print('%0.2f%% confidence interval = (%0.2f,%0.2f)' % (conf_level * 100, *conf_interval))
print("--- %s seconds ---" % (time.time() - start_time))
