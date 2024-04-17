import matplotlib.pyplot as plt
from scipy.stats import norm
import seaborn as sns
import numpy as np
from sklearn.linear_model import LinearRegression
from scipy.stats import pearsonr

np.random.seed(7)
sns.set()
x = np.arange(0.0, 10.0, 0.1)
x += norm.rvs(size=len(x))
y = 2.0 * x - 5.0 + norm.rvs(size=len(x))
model = LinearRegression(fit_intercept=True)
model.fit(x[:, np.newaxis], y)
xpred = 3.0
ypred = model.predict(np.array(3.0).reshape(-1, 1))
yfit = model.predict(x[:, np.newaxis])
plt.figure()
plt.scatter(x, y)
plt.plot(x, yfit, color='g')
plt.plot(xpred, ypred, 'o', color='r')
plt.title('Graph of y vs x')
plt.xlabel('x')
plt.ylabel('y')
print("slope of regression line = %0.4f" % model.coef_[0])
print("y-intercept of regression line = %0.4f" % model.intercept_)
print("y = %0.4f when x = %0.4f" % (ypred[0], xpred))
corr, _ = pearsonr(x, y)
print('Pearsons correlation coefficient, r = %0.4f' % corr)
plt.show()
