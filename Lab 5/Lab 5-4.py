import time
import numpy as np
import pandas as pd
import scipy.stats as stats
import matplotlib.pyplot as plt

start_time = time.time()

n = 1000
p = 0.5
q = 1.0 - p
plt.figure()
x = np.arange(400, 600)
plt.bar(x, stats.binom.pmf(x, n=n, p=p), width=1.0, color='b')
xc = np.linspace(400, 600)
plt.plot(xc, stats.norm.pdf(xc, loc=n * p, scale=np.sqrt(n * p * q)), color='r')
print('P(475<=k<=525) = %0.4f' % (stats.binom.cdf(k=525, n=n, p=p) - stats.binom.cdf(k=474, n=n, p=p)))
print('P(475<=k<=525) = %0.4f' % (stats.norm.cdf(525, loc=n * p, scale=np.sqrt(n * p * q)) - stats.norm.cdf(474, loc=n*p, scale=np.sqrt(n * p * q))))
print("--- %s seconds ---" % (time.time() - start_time))
plt.show()
