from scipy.stats import binom
import time

start_time = time.time()

n = 100
p = 0.7
expected_x = 0.0
for i in range(n):
    expected_x += i * binom.pmf(i, n=n, p=p)
print('expected value = %0.4f' % expected_x)
print('np = %0.4f' % (n * p))
print("--- %s seconds ---" % (time.time() - start_time))
