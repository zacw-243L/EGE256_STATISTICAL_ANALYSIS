from scipy.stats import binom
import time

start_time = time.time()

n = 100
p = 0.7
expected_x = 0.0
variance = 0.0
for i in range(n):
    variance += (i - expected_x) ** 2 * binom.pmf(i, n=n, p=p)
print('variance = %0.4f' % variance)

expected_x_sqr = 0.0
for i in range(n):
    expected_x_sqr += (i ** 2) * binom.pmf(i, n=n, p=p)
print('E(X^2)-[E(X)]^2 = %0.4f' % (expected_x_sqr - expected_x ** 2))
print("--- %s seconds ---" % (time.time() - start_time))
