import time
import numpy as np
import seaborn as sns
from scipy.stats import norm, t
import matplotlib.pyplot as plt

start_time = time.time()

np.random.seed(7)
population = norm.rvs(loc=50.0, scale=30.0, size=10000)
pop_mean = population.mean()
pop_std = population.std()

n = 5
sample = np.random.choice(population, n)
sam_mean = sample.mean()
sam_std = sample.std(ddof=1)
conf_level = 0.95
t_critical = -t.ppf((1.0 - conf_level) * 0.5, df=n - 1)

intervals = []
sam_means = []
for i in range(100):
    sample = np.random.choice(population, n)
    sam_mean = sample.mean()
    sam_std = sample.std(ddof=1)
    err_margin = t_critical * sam_std / np.sqrt(n)
    conf_interval = (sam_mean - err_margin, sam_mean + err_margin)
    sam_means.append(sam_mean)
    intervals.append(conf_interval)

plt.figure(figsize=(18, 9))
err_colors = []
for bot, top in intervals:
    if bot <= pop_mean <= top:
        err_colors.append('g')
    else:
        err_colors.append('r')

err = [(top - bot) / 2 for bot, top in intervals]
plt.errorbar(x=np.arange(0, 100, 1), y=sam_means, yerr=err, fmt='o', ecolor=err_colors)
plt.hlines(xmin=0, xmax=100, y=pop_mean, color="b")
print("t-critical value = %0.2f" % t_critical)
err_margin = t_critical * sam_std / np.sqrt(n)
conf_interval = (sam_mean - err_margin, sam_mean + err_margin)
print('%0.2f%% confidence interval = (%0.2f,%0.2f)' % (conf_level * 100, *conf_interval))
print("--- %s seconds ---" % (time.time() - start_time))
plt.show()
