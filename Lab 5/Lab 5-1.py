import time
import numpy as np
import pandas as pd
import scipy.stats as stats
import matplotlib.pyplot as plt

start_time = time.time()

n = 10
p = 0.5
q = 1.0 - p

fair_coin_flips = stats.binom.rvs(n=n, p=p, size=10000)
pd.DataFrame(fair_coin_flips).hist(range=(-0.5, 10.5), bins=11)

print(pd.crosstab(index="counts", columns=fair_coin_flips))
print('mean = %0.4f' % fair_coin_flips.mean())
print('np = %0.4f' % (n * p))
print('var = %0.4f' % fair_coin_flips.var())
print('np(1 - p) = %0.4f' % (n * p * q))
print("--- %s seconds ---" % (time.time() - start_time))

plt.show()
