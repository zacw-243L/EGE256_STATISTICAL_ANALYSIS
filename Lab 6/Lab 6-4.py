import matplotlib.pyplot as plt
from scipy.stats import norm
import numpy as np
import time

start_time = time.time()

rv_normal = norm(0.0, 1.0)
x = np.arange(-5, 5, 0.01)
plt.plot(x, rv_normal.cdf(x))
plt.title("Cumulative Distribution Function (CDF) of X~N( 0, 1 )")
plt.xlabel('x')
plt.ylabel('f(x)')
print("--- %s seconds ---" % (time.time() - start_time))
plt.show()
