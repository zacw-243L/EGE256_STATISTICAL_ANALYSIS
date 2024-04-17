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
alpha = 0.05
C = t.ppf(alpha * 0.5, df=n - 1)
xLeft = np.linspace(-5.0, C)
xRight = np.linspace(-C, 5.0)
plt.clf()
plt.plot(x, t.pdf(x, df=n - 1))
plt.vlines(t_statistic, 0.0, 0.3, color='b')
xRight1 = np.linspace(t_statistic, 6.0)
plt.fill_between(xRight1, t.pdf(xRight1, df=n - 1))
half_p = 1.0 - t.cdf(t_statistic, df=n - 1)
plt.text(t_statistic + 0.5, 0.05, '{:0.4f}'.format(half_p), ha='left')
plt.text(0.0, 0.1, '{:0.4f}'.format(t.cdf(t_statistic, df=n - 1)), ha='center')
print("--- %s seconds ---" % (time.time() - start_time))
plt.show()
