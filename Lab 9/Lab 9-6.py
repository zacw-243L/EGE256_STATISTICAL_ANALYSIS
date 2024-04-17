import time
from scipy.stats import ttest_1samp, t
import pandas as pd
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt

start_time = time.time()

df = pd.read_csv('Heart.csv')
n = len(df.RestBP)
one_sample = ttest_1samp(a=df.RestBP, popmean=130.0)
print('The t-statistic is %0.4f and the p-value is %0.4f' % one_sample)
print("--- %s seconds ---" % (time.time() - start_time))
