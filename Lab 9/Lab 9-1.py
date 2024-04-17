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
print('sample mean = %0.2f' % sam_mean)
print('sample std = %0.2f' % sam_std)
print('sample size = %d' % n)
sns.displot(df.RestBP, kde=True)
print("--- %s seconds ---" % (time.time() - start_time))
plt.show()
