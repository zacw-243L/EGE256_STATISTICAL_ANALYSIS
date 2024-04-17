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
plt.clf()
half_p = 1.0 - t.cdf(t_statistic, df=n - 1)
x = np.linspace(-6.0, 6.0)
plt.plot(x, t.pdf(x, df=n - 1))
plt.vlines(t_statistic, 0.0, 0.3, color='b')
plt.vlines(-t_statistic, 0.0, 0.3, color='b')
xLeft = np.linspace(-6.0, -t_statistic)
plt.fill_between(xLeft, t.pdf(xLeft, df=n - 1), color='g')
plt.text(-t_statistic - 0.5, 0.05, '{:0.4f}'.format(half_p), ha='right')
xRight = np.linspace(t_statistic, 6.0)
plt.fill_between(xRight, t.pdf(xRight, df=n - 1), color='g')
plt.text(t_statistic + 0.5, 0.05, '{:0.4f}'.format(half_p), ha='left')
plt.show()
print('p-value = %0.4f' % (2.0 * half_p))
