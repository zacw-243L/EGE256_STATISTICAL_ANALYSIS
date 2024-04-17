import time
from scipy.stats import norm
import pandas as pd
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt

start_time = time.time()

plt.figure(figsize=(12, 10))
alpha = 0.01
h_null = norm()
critical_value = -h_null.ppf(alpha)
x = np.arange(-4.0, critical_value, 0.01)
plt.fill_between(x, h_null.pdf(x), facecolor='grey', alpha=0.5)
x = np.arange(critical_value, 4.0, 0.01)
plt.fill_between(x, h_null.pdf(x), facecolor='red', alpha=0.5)
h_alt = norm(loc=3.0, scale=2.0)
x = np.arange(-4.0, critical_value, 0.01)
plt.fill_between(x, h_alt.pdf(x), facecolor='blue', alpha=0.5)
x = np.arange(critical_value, 10.0, 0.01)
plt.fill_between(x, h_alt.pdf(x), facecolor='grey', alpha=0.5)
plt.text(x=0.0, y=0.15, s="Null\nHypothesis", ha='center')
plt.text(x=3.0, y=0.15, s="Alternative\nHypothesis", ha='center')
plt.text(x=critical_value + 0.5, y=0.01, s="Type I Error", ha='left')
plt.text(x=critical_value - 0.5, y=0.01, s="Type II Error", ha='right')
plt.text(critical_value, -0.01, 't$_{critical}$', ha='center')
print("--- %s seconds ---" % (time.time() - start_time))
plt.show()
