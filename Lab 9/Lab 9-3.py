import time
from scipy.stats import ttest_1samp, t
import pandas as pd
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt

start_time = time.time()

df = pd.read_csv('Heart.csv')
n = len(df.RestBP)
sam_mean = df.RestBP.mean()
sam_std = df.RestBP.std(ddof=1)
t_statistic = (sam_mean - 130.0) / (sam_std / np.sqrt(n))
x = np.linspace(-6.0, 6.0)

plt.clf()
plt.plot(x, t.pdf(x, df=n - 1))
plt.vlines(t_statistic, 0.0, 0.3, color='b')
x = np.linspace(-6.0, t_statistic)
plt.fill_between(x, t.pdf(x, df=n - 1))

plt.text(0.0, 0.1, '{:0.4f}'.format(t.cdf(t_statistic, df=n - 1)), ha='center')
print("--- %s seconds ---" % (time.time() - start_time))
plt.show()
