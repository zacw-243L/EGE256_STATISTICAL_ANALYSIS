import time
import numpy as np
import pandas as pd
import scipy.stats as stats
import matplotlib.pyplot as plt

start_time = time.time()

n = 10
p = 0.8
q = 1.0 - p

biased_coin_flips = stats.binom.rvs(n=n, p=p, size=10000)
pd.DataFrame(biased_coin_flips).hist(range=(-0.5, 10.5), bins=11)

print(pd.crosstab(index="counts", columns=biased_coin_flips))
print('mean = %0.4f' % biased_coin_flips.mean())
print('np = %0.4f' % (n * p))
print('var = %0.4f' % biased_coin_flips.var())
print('np(1 - p) = %0.4f' % (n * p * q))
print('P(<=5 successes) = %0.4f' % stats.binom.cdf(k=5, n=n, p=p))
print('P(k>8) = %0.4f' % (1.0 - stats.binom.cdf(k=8, n=n, p=p)))
print('P(k=5) = %0.4f' % stats.binom.pmf(k=5, n=n, p=p))
print("--- %s seconds ---" % (time.time() - start_time))

plt.show()
