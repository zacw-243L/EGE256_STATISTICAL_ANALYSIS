import time
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from scipy.stats import gamma, norm

start_time = time.time()
sns.set()

i = 0
while i < 100:
    population = np.concatenate((gamma.rvs(2.0, size=5000), 10.0 + gamma.rvs(2.0, size=5000)))
    pop_std = population.std()
    pop_mean = population.mean()
    print('population mean = %0.3f' % pop_mean)
    print('population standard deviation = %0.3f' % pop_std)
    # plt.hist(population, bins=30)
    # plt.title('Population Distribution (not normal)')
    # plt.show()
    i += 1

print("--- %s seconds ---" % (time.time() - start_time))
