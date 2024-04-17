import time
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from scipy.stats import gamma, norm

start_time = time.time()
sns.set()

population = np.concatenate((gamma.rvs(2.0, size=5000), 10.0 + gamma.rvs(2.0, size=5000)))
plt.hist(population, bins=30)
plt.title('Population Distribution (not normal)')
print("--- %s seconds ---" % (time.time() - start_time))
plt.show()
