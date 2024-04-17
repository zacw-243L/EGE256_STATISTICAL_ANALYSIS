import time
import numpy as np
from scipy.stats import norm
import matplotlib.pyplot as plt

A = int(input("Enter number: "))
start_time = time.time()

rv_normal = norm(A, 1.0)
x = np.arange(A-5, A+5, 0.01)
plt.figure()
plt.plot(x, rv_normal.pdf(x))
plt.title(f"Probability Density Function (PDF) of X~N( {A}, 1 )")
plt.xlabel('x')
plt.ylabel('f(x)')
print("--- %s seconds ---" % (time.time() - start_time))
plt.show()
