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
x = np.linspace(-6.0, 6.0)
alpha = 0.05
C = t.ppf(alpha * 0.5, df=n - 1)
xLeft = np.linspace(-5.0, C)
xRight = np.linspace(-C, 5.0)
plt.clf()
plt.plot(x, t.pdf(x, df=n - 1))
plt.vlines(C, 0.0, t.pdf(C, df=n - 1), color='r')
plt.vlines(-C, 0.0, t.pdf(-C, df=n - 1), color='r')
plt.fill_between(xLeft, t.pdf(xLeft, df=n - 1), color='r')
plt.fill_between(xRight, t.pdf(xRight, df=n - 1), color='r')
plt.text(C, 0.1, 'left rejection zone\nt < {:0.4f}'.format(C), ha='right')
plt.text(-C, 0.1, 'right rejection zone\nt > {:0.4f}'.format(-C), ha='left')
t_statistic = (sam_mean - 130.0) / (sam_std / np.sqrt(n))
print('t_statistic = %0.4f' % t_statistic)
r = t.cdf(t_statistic, df=n - 1)
print('P( x < 130.0 ) = %0.4f' % r)
print("--- %s seconds ---" % (time.time() - start_time))
plt.show()
