import time
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

start_time = time.time()

# use normal distribution with mean = 50 and std = 30 as population
np.random.seed = 123
population = norm.rvs(50.0, 30.0, size=10000)
plt.hist(population, bins=30)
plt.title('Population Distribution (normal)')
print("--- %s seconds ---" % (time.time() - start_time))
plt.show()
