import numpy as np
import pandas as pd
from scipy.stats import chi2, chisquare
import matplotlib.pyplot as plt

np.random.seed(7)
# roll die 1000 times
df_die_rolls = pd.DataFrame(np.random.randint(1, 7, 1000))
# compute observed frequencies
die_tab = pd.crosstab(index=df_die_rolls[0], columns="observed")
# compute expected frequencies
die_tab['expected'] = [1000.0 / 6.0] * 6
chi_sqr_stat = (((die_tab['observed'] - die_tab['expected']) ** 2) / die_tab['expected']).sum()
# significance level alpha is 5%
alpha = 0.05
# degrees of freedom is 5
df = 5
# set font size to 10
plt.rcParams.update({'font.size': 10})
# set x and y limits
ax = plt.gca()
ax.set_xlim([0, 20])
ax.set_ylim([0, 0.2])
# x-axis ranges from 0 to 20 in increments of 0.001
x = np.arange(0, 20, 0.001)
chi_alpha = chi2.ppf(1.0 - alpha, df=df)
x_fill = np.arange(0, chi_alpha, 0.001)
y_fill = chi2.pdf(x_fill, df=df)
ax.fill_between(x_fill, y_fill, 0, alpha=0.3, color='b')
reject_x = chi_alpha + 0.5
reject_y = chi2.pdf(reject_x, df=df) * 0.5
xt = [chi_alpha]
xt_label = [r'$\chi_c^2$ = ' + '{:0.3f}'.format(chi_alpha)]
plt.xticks(xt, xt_label)
plt.axvline(chi_alpha, color='r')
plt.arrow(chi_alpha, 0.125, 2, 0, width=0.005, head_width=0.02, head_length=0.8, color='r')
plt.plot([reject_x, chi_alpha + 2.5], [reject_y, 0.04], color='b')
plt.title('Chi-Square Probability Density Function ( df = {:d} )'.format(df))
plt.rcParams.update({'font.size': 20})
ax.text(4.5, 0.05, '{:2d}%'.format(int((1.0 - alpha) * 100)), ha="center", va="center")
ax.text(chi_alpha + 3.5, 0.05, '{:2d}%'.format(int(alpha * 100)), ha="center", va="center")
plt.rcParams.update({'font.size': 10})
ax.text(chi_alpha + 1.0, 0.15, 'Rejection Region', ha="left", va="center", color='r')
# plot chi-square distribution with 5 degrees of freedom
plt.plot(x, chi2.pdf(x, df=df), linewidth=4)
# plot chi-square statistic
plt.annotate('Chi-sqr stat\n{:0.4f}'.format(chi_sqr_stat), xy=(chi_sqr_stat, 0.0), xytext=(chi_sqr_stat, 0.02), arrowprops=dict(arrowstyle="->"), ha='center')
plt.show()
