import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import chi2, chi2_contingency

# load titanic dataset
titanic = pd.read_csv('titanic.csv')
# print(titanic.columns)
# choose only passenger class and survival
data = titanic[['pclass', 'survived']]
# print(data)
# draw bar plots of passenger class and survival
"""plt.subplot(121)
sns.countplot(x='pclass', data=data)
plt.title('Passenger Class')
plt.subplot(122)
sns.countplot(x='survived', data=data)
plt.title('Survival')
plt.tight_layout()
plt.show() """

pclass_survival = pd.pivot_table(data, index=['pclass'], columns=['survived'], aggfunc='size')
# print(pclass_survival)
total = pclass_survival.sum().sum()
# print(total)
pclass = pclass_survival.sum(axis=1) / total
# print(pclass)
survived = pclass_survival.sum(axis=0) / total
# print(survived)
# compute expected frequencies
expected = pclass.to_frame() @ survived.to_frame().T * total
# print(expected)
chi_table = ((pclass_survival - expected) ** 2) / expected
print(chi_table, "\n")
chi_stat = chi_table.sum().sum()
p_value = chi2.sf(chi_stat, df=2)
critical_value = chi2.ppf(0.95, df=2)
print("Chi-square statistic = %0.4f" % chi_stat)
print("p-value is %0.4f" % p_value)
print('critical value = %0.4f' % critical_value)
chi_stat, p_value, dof, _ = chi2_contingency(pclass_survival)
print('Chi-square statistic = %0.4f' % chi_stat)
print("p-value = %0.4f" % p_value)
print("Degrees of Freedom =", dof)
