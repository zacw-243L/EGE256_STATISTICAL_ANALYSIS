import time
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

start_time = time.time()

i = 0
while i < 100:
    # use normal distribution with mean = 50 and std = 30 as population
    np.random.seed = 123
    population = norm.rvs(50.0, 30.0, size=10000)
    pop_mean = population.mean()
    print('population mean = %0.3f' % pop_mean)
    pop_std = population.std()
    print('population standard deviation = %0.3f' % pop_std)
    # plt.hist(population, bins=30)
    # plt.title('Population Distribution (normal)')
    # plt.show()
    i += 1

print("--- %s seconds ---" % (time.time() - start_time))
