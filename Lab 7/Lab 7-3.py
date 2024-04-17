import time
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from scipy.stats import gamma, norm

start_time = time.time()
sns.set()

population = np.concatenate((gamma.rvs(2.0, size=5000), 10.0 + gamma.rvs(2.0, size=5000)))
# sample size n
n = 3
# take 10000 samples of size n
sam_mean_list = []
for i in range(10000):
    s = np.random.choice(population, size=n)
    sam_mean_list.append(s.mean())

# compute the mean and standard deviation of the 1000 sample means
sam_mean = np.array(sam_mean_list).mean()
print('mean of sample means = %0.3f' % sam_mean)
sam_std = np.array(sam_mean_list).std()
print('standard deviation of sample means = %0.3f' % sam_std)
plt.hist(sam_mean_list, bins=30, color='b', density=True)
left, right = plt.xlim()
x = np.linspace(left, right)
rv_normal = norm(loc=sam_mean, scale=sam_std)
plt.plot(x, rv_normal.pdf(x), color='r')
plt.title('Sampling and Normal Distribution (sample size = %d)' % n)
print("--- %s seconds ---" % (time.time() - start_time))
plt.show()
