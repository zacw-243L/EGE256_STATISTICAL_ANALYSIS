from scipy.stats import uniform, norm
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import time

start_time = time.time()

# rv_uniform is a random variable with uniform distribution
rv_uniform = uniform(loc=0, scale=1)
# plot the uniform probability density function (PDF)
x = np.linspace(-1, 2)
plt.plot(x, rv_uniform.pdf(x))
plt.xlabel('x')
plt.ylabel('f(x)')
print("--- %s seconds ---" % (time.time() - start_time))
plt.show()
