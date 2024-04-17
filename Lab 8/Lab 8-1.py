import time
import numpy as np
import seaborn as sns
from scipy.stats import norm
import matplotlib.pyplot as plt

start_time = time.time()
np.random.seed(7)
# generate population of size 10000 with normal distribution
# having mean 50 and standard deviation 30
population = norm.rvs(loc=50.0, scale=30.0, size=10000)
sns.displot(population)
# compute population parameters
pop_mean = population.mean()
pop_std = population.std()
print('population mean = {:0.2f}'.format(pop_mean))
print('population std = {:0.2f}'.format(pop_std))
# sample 30 values
n = 30
sample = np.random.choice(population, 30)
# sample statistics
sam_mean = sample.mean()
sam_std = sample.std(ddof=1)
print('sample mean = {:0.2f}'.format(sam_mean))
print('sample std = {:0.2f}'.format(sam_std))
# compute percentage difference between sample statistics and
# population parameters
err_pop_mean = (pop_mean - sam_mean) / pop_mean * 100
err_pop_std = (pop_std - sam_std) / pop_std * 100
print('error estimating population mean = %0.2f%%' % err_pop_mean)
print('error estimating population std = %0.2f%%' % err_pop_std)
print("--- %s seconds ---" % (time.time() - start_time))
plt.show()
