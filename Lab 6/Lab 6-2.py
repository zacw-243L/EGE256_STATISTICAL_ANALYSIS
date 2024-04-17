from scipy.stats import uniform, norm
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import time

start_time = time.time()

# rv_uniform is a random variable with uniform distribution
rv_uniform = uniform(loc=0, scale=1)
trials = 1000
n = 100
m = []
for i in range(trials):
    # generate n random numbers with uniform distribution
    y = rv_uniform.rvs(n)
    # find and record their sum
    m.append(sum(y))

# display the histogram
sns.displot(m, kde=True)
print("--- %s seconds ---" % (time.time() - start_time))
plt.show()
