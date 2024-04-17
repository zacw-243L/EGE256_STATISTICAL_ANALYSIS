import time
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from scipy.stats import gamma, norm

start_time = time.time()
sns.set()

population = np.concatenate((gamma.rvs(2.0, size=5000), 10.0 + gamma.rvs(2.0, size=5000)))
# sample size n
n = 50
# take 10000 samples of size n
sam_mean_list = []
for i in range(10000):
    s = np.random.choice(population, size=n)
    sam_mean_list.append(s.mean())

sam_mean = np.array(sam_mean_list).mean()
print('mean of sample means = %0.3f' % sam_mean)
sam_std = np.array(sam_mean_list).std()
print('standard deviation of sample means = %0.3f' % sam_std)
plt.hist(sam_mean_list, bins=30, color='b', density=True)
plt.title('Sampling and Normal Distribution (sample size = %d)' % n)
left, right = plt.xlim()
x = np.linspace(left, right)
rv_normal = norm(loc=sam_mean, scale=sam_std)
plt.plot(x, rv_normal.pdf(x), color='r')
print("--- %s seconds ---" % (time.time() - start_time))
plt.show()
