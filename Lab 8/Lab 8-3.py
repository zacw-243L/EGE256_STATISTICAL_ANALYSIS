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
conf_level = 0.95
z_critical = -norm.ppf((1.0 - conf_level) * 0.5)

intervals = []
sam_means = []
for i in range(100):
    sample = np.random.choice(population, n)
    sam_mean = sample.mean()
    sam_means.append(sam_mean)
    err_margin = z_critical * pop_std / np.sqrt(n)
    conf_interval = (sam_mean - err_margin, sam_mean + err_margin)
    intervals.append(conf_interval)

plt.figure(figsize=(18, 9))
err_colors = []
err = [(top - bot) / 2 for bot, top in intervals]
for bot, top in intervals:
    if top >= pop_mean >= bot:
        err_colors.append('g')
    else:
        err_colors.append('r')

plt.errorbar(x=np.arange(0, 100, 1), y=sam_means, yerr=err, fmt='o', ecolor=err_colors)
plt.hlines(xmin=0, xmax=100, y=pop_mean, color="b")
print("--- %s seconds ---" % (time.time() - start_time))
plt.show()
