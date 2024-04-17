import numpy as np
import pandas as pd
from scipy.stats import chi2, chisquare
import matplotlib.pyplot as plt

np.random.seed(7)
# roll die 1000 times
df_die_rolls = pd.DataFrame(np.random.randint(1, 7, 1000))
print(df_die_rolls)
# compute observed frequencies
die_tab = pd.crosstab(index=df_die_rolls[0], columns="observed")
print(die_tab)
# compute expected frequencies
die_tab['expected'] = [1000.0 / 6.0] * 6
print(die_tab)
# compute chi-square statistic
chi_sqr_stat = (((die_tab['observed'] - die_tab['expected']) ** 2) / die_tab['expected']).sum()
print('Chi-Square statistic = %0.4f' % chi_sqr_stat)
# find chi-square critical value for 95% significance level and
# degrees of freedom = 5 since there are 6 categories
crit = chi2.ppf(q=0.95, df=5)
print("Critical value = %0.4f" % crit)
# find the p-value
p_value = 1.0 - chi2.cdf(x=chi_sqr_stat, df=5)
print("p-value = %0.4f" % p_value)
# print chi-square critical value
print(chisquare(f_obs=die_tab['observed'], f_exp=die_tab['expected']))
