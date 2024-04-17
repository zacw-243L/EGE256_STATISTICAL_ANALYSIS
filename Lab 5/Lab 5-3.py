import time
import numpy as np
import pandas as pd
import scipy.stats as stats
import matplotlib.pyplot as plt

start_time = time.time()

n = 10
p = 0.5
q = 1.0 - p
plt.figure()
x = np.arange(0, 11)
plt.bar(x, stats.binom.pmf(x, n=n, p=p), width=1.0, color='b')
xc = np.linspace(0, 11)
plt.plot(xc, stats.norm.pdf(xc, loc=n * p, scale=np.sqrt(n * p * q)), color='r')
print("--- %s seconds ---" % (time.time() - start_time))
plt.show()
